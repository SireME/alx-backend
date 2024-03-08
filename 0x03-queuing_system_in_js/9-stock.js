// rv
const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
]

function getItemById(id) {
    return listProducts.find(obj_v => obj_v.id === id);
}

const express = require('express');
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(formattedProducts);
});

const redis = require('redis');
const { promisify } = require('util');
const redisClient = redis.createClient();

redisClient.on('error', (err) => console.log('Redis Client Error', err));

// Connecting to the Redis server
(async () => {
  await redisClient.connect();
})();

function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(redisClient.get).bind(redisClient);
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const currentStock = await getCurrentReservedStockById(itemId) || item.stock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: parseInt(currentStock)
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({status: "Product not found"});
  }

  const reservedStock = parseInt(await getCurrentReservedStockById(itemId)) || 0;
  const availableStock = item.stock - reservedStock;

  if (availableStock < 1) {
    return res.json({status: "Not enough stock available", itemId});
  }

  await reserveStockById(itemId, reservedStock + 1);

  res.json({status: "Reservation confirmed", itemId});
});


app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});


