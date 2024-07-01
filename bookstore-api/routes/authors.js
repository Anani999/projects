// routes/authors.js
const express = require('express');
const router = express.Router();
const Author = require('../models/Author');

// Create a new author
router.post('/', async (req, res) => {
    const { name, bio, birthdate } = req.body;
    try {
        const author = new Author({ name, bio, birthdate });
        await author.save();
        res.status(201).json(author);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Get all authors
router.get('/', async (req, res) => {
    try {
        const authors = await Author.find();
        res.json(authors);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Get an author by ID
router.get('/:id', async (req, res) => {
    try {
        const author = await Author.findById(req.params.id);
        if (!author) {
            return res.status(404).json({ message: 'Author not found' });
        }
        res.json(author);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Update an author by ID
router.put('/:id', async (req, res) => {
    try {
        const { name, bio, birthdate } = req.body;
        const author = await Author.findByIdAndUpdate(
            req.params.id,
            { name, bio, birthdate },
            { new: true }
        );
        if (!author) {
            return res.status(404).json({ message: 'Author not found' });
        }
        res.json(author);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Delete an author by ID
router.delete('/:id', async (req, res) => {
    try {
        const author = await Author.findByIdAndDelete(req.params.id);
        if (!author) {
            return res.status(404).json({ message: 'Author not found' });
        }
        res.json({ message: 'Author deleted' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

module.exports = router;
