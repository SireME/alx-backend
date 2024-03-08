import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
    let queue;

    beforeEach(function () {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(function () {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', function () {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });

    it('should create new jobs in the queue', function () {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 5678 to verify your account'
            }
        ];

        createPushNotificationsJobs(list, queue);

        const jobs = queue.testMode.jobs;
        expect(jobs).to.have.lengthOf(2);

        jobs.forEach((job, index) => {
            expect(job.type).to.equal('push_notification_code_3');
            expect(job.data).to.deep.equal(list[index]);
        });
    });
});

