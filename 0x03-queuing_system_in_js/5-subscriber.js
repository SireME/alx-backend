import redis from 'redis';

const client = redis.createClient()

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ERROR_MESSAGE');
});

// subsribe to channel: 'HolbertonSchools'
client.subscribe('holberton school channel')

// log message to console when received
// or unsubribe based on message type
client.on('message', (channel, message) => {
  console.log(message)
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel)
    client.quit()
  }
})

