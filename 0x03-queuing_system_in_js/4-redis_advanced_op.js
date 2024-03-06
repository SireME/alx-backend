import redis from 'redis';

const client = redis.createClient()

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ERROR_MESSAGE');
});


const hashValues = {
 'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

const entries = Object.entries(hashValues);

// add key value pairs to redis hash 
for (let [field, value] of entries) {
  client.hset('HolbertonSchools', field, value, redis.print);
}

// display hash
client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.error(`Error: ${err}`);
    return
  }
  console.log(obj)
});
