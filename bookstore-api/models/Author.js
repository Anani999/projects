// models/Author.js
const mongoose = require('mongoose');

const AuthorSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    bio: String,
    birthdate: Date,
});

module.exports = mongoose.model('Author', AuthorSchema);
