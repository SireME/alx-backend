import redis from 'redis';
import { promisify } from 'util'

const client = redis.createClient()

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ERROR_MESSAGE');
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
    try {
        const reply = await setAsync(schoolName, value);
        console.log(`Reply: ${reply}`);
    } catch (error) {
        console.error(error);
    }
}


async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

// Call the functions
(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
