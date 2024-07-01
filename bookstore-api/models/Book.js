// models/Book.js
const mongoose = require('mongoose');

const BookSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    author: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Author',
        required: true,
    },
    publishedDate: Date,
    pages: Number,
});

module.exports = mongoose.model('Book', BookSchema);
