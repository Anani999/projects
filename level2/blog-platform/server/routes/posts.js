// /server/routes/posts.js
const express = require('express');
const { createPost, getPosts, getPost, updatePost, deletePost } = require('../controllers/postController');
const auth = require('../middleware/auth');

const router = express.Router();

router.post('/', auth, createPost);
router.get('/', getPosts);
router.get('/:id', getPost);
router.put('/:id', auth, updatePost);
router.delete('/:id', auth, deletePost);

module.exports = router;
