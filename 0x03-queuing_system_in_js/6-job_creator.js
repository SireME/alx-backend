import kue from 'kue';

const queue  = kue.createQueue();


const objData = {
  phoneNumber: '0000000000',
  message: 'nemo dat core non habet',
}

const job = queue.create('push_notification_code', objData).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.log('Notification job failed');
    return
  }
  console.log('Notification job completed');
});
