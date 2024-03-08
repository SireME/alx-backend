function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const qJob = queue.create('push_notification_code_3', job).save((err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Notification job created: ${qJob.id}`);
      }
    });

    qJob.on('complete', () => {
      console.log(`Notification job ${qJob.id} completed`);
    });

    qJob.on('failed', (errorMessage) => {
      console.log(`Notification job ${qJob.id} failed: ${errorMessage}`);
    });

    qJob.on('progress', (progress) => {
      console.log(`Notification job ${qJob.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
