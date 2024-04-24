const express = require('express') 
const bcrypt = require('bcrypt')  
const mongoose = require('mongoose')  

const app = express() 
app.use(express.json()) 

mongoose.connect('mongodb://127.0.0.1:27017/DSproject') 

// model for users
const USER = mongoose.model('user', new mongoose.Schema({
  Username: String,
  Password: String,
  LikedPosts: Array
})) 

// model for posts 
const POST = mongoose.model('posts', new mongoose.Schema({
  Title: String,
  Poster: String,
  Text: String,
  Timestamp: Date, 
  Hashtags: Array, 
  Likes: Number, 
  Comments: Array
})) 


// route for adding a user
app.post('/create_user', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10) 
    const user = new USER({
      Username: req.body.username,
      Password: hashedPassword,
      LikedPosts: []
    }) 

    await user.save()
    res.status(201).send(user) 

  } catch(error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
  
}) 

// checking if username already exists in database
app.get('/is_username_unique', async (req, res) => {
  try {
    let user_count = await USER.countDocuments({Username: req.query.username})
    const isUnique = user_count === 0 
    res.status(200).json({ isUnique: isUnique }) 
  } catch(error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// route for logging in
app.post('/login', async (req, res) => {
  try {
    const user = await USER.findOne({ Username: req.body.username }) 
    if (!user) {
      return res.status(404).send({ message: "User not found" }) 
    }

    const passwordIsValid = bcrypt.compare(req.body.password, user.Password) 
    if (!passwordIsValid) {
      return res.status(401).send({ message: "Invalid password" }) 
    }

    res.status(200).send({ message: "User authenticated successfully" }) 
  } catch (error) {
    return res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// route for creating a post
app.post('/create_post', async (req, res) => {
  try {
    

    const post = new POST({
      Title: req.body.title,
      Poster: req.body.poster,
      Text: req.body.text,
      Timestamp: new Date(), 
      Hashtags: req.body.hashtags, 
      Likes: 0, 
      Comments: []
    }) 

    await post.save() 

    res.status(201).send({ message: "Post created successfully" }) 
  } catch (error) {
      console.log(error)
      res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// checking if title already exists when creating a new post
app.get('/is_title_unique', async (req, res) => {

  try {
    let post_count = await POST.countDocuments({ Title: req.query.title })
    const isUnique = post_count === 0 
    res.json({ isUnique: isUnique }) 
  } catch(error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// route for getting posts from database
app.get('/posts', async (req, res) => {
  try {
    const posts = await POST.find().sort({ Timestamp: -1 }).limit(10) 
    res.status(200).json(posts) 
  } catch (error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// route for getting posts with specific hashtag
app.get('/posts_hashtag', async (req, res) => {
  try {
    const posts = await POST.find({ Hashtags : {"$in" : [req.query.hashtag]}})
    res.status(200).json(posts) 
  } catch (error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
}) 

// route for liking/removing like for a post
app.post('/like', async (req, res) => {
  try {
    const title = req.body.title
    const username = req.body.username

    let post = await POST.findOne({ Title: title })
    let user = await USER.findOne({ Username: username})

    if (!post) {
      return res.status(404).send({ message: "Post not found" }) 
    }
    // Check if user has liked already by checking the liked posts id in the liked posts
    const alreadyLiked = user.LikedPosts.indexOf(post._id)

    // If they have liked the post already, removing the post from user's liked posts
    if (alreadyLiked != -1) {
      await POST.findOneAndUpdate(
        { Title: title },
        { "$inc": { Likes: -1} },
      )
      user.LikedPosts.splice(alreadyLiked, 1) 
      await user.save() 
      res.status(204).send({message: "Like removed"})
    } else { // user has not liked, adding the post to user's liked posts array
      await POST.findOneAndUpdate(
        { Title: title },
        {"$inc": { Likes: 1} },
      )
      user.LikedPosts.push(post._id)
      await user.save() 
      res.status(201).send({message: "Like added"})
    }
    
    
  } catch (error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
})

// route for adding a comment to post
app.post('/comment', async (req, res) => {
  try {
    const title = req.body.title
    const username = req.body.username
    const comment = req.body.comment

    let post = await POST.findOne({ Title: title }) 

    if (!post) {
      return res.status(404).send({ message: "Post not found" }) 
    }

    await POST.findOneAndUpdate(
      { Title: title },
      { "$push": { Comments: { Username: username, Text: comment} }}
    )
      res.status(201).send({ message: "Comment added"}) 
    
  } catch (error) {
    res.status(500).send({ message: "Server error", error: error.toString() }) 
  }
})


const PORT = 5000 
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`) 
}) 
