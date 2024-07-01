const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/weather', async (req, res) => {
  const { latitude, longitude } = req.query;
  const apiUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`;
  // const apiUrl = `https://api.open-meteo.com/v1/forecast?latitude=90&longitude=39&current_weather=true`;

  try {
    const response = await axios.get(apiUrl);
    res.json(response.data.current_weather);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching weather data' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
