// index.js
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI)
.then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('Error connecting to MongoDB', err);
});


// Import routes
const booksRouter = require('./routes/books');
const authorsRouter = require('./routes/authors');

// Use routes
app.use('/books', booksRouter);
app.use('/authors', authorsRouter);


// Routes
app.get('/', (req, res) => {
    res.send('Welcome to the Bookstore API');
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
