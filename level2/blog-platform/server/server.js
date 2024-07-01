// /server/server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const config = require('./config');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(bodyParser.json());
app.use(cors());

mongoose.connect(config.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

app.get('/', (req, res) => {
  res.send('Welcome to the Blog Platform API');
});

// /server/server.js
const authRoutes = require('./routes/auth');

app.use('/api/auth', authRoutes);

// /server/server.js
const postRoutes = require('./routes/posts');

app.use('/api/posts', postRoutes);



app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
