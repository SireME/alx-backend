
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');
const queue = kue.createQueue();

const app = express();
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return await getAsync('available_seats');
};

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservation are blocked" });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: "Reservation failed" });
    }
    res.json({ status: "Reservation in process" });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats = availableSeats - 1;

    if (availableSeats < 0) {
      return done(new Error("Not enough seats available"));
    }

    await reserveSeat(availableSeats);

    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

const init = async () => {
  await reserveSeat(50);
};

init().then(() => {
  app.listen(1245, () => {
    console.log('Server is running on port 1245');
  });
});
