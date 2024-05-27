
### Blog API
* Fetch all the Posts
```
query posts{
  posts{
    id
    title
    description
    publishDate
    author
  }
}
```

Example response below
```
{
  "data": {
    "posts": [
      {
        "id": "1",
        "title": "First Post",
        "description": "Hey guys here is my first post",
        "publishDate": "2023-08-19",
        "author": "Jerry"
      },
      {
        "id": "2",
        "title": "Second post through graphql",
        "description": "Second post description",
        "publishDate": "2023-08-22",
        "author": "Mr Me"
      }
    ]
  }
}
```

****

* Create Post
```
mutation createPost($title: String!, $description: String!, $publishDate: String, $author: String){
  createPost(title: $title, description: $description, publishDate:$publishDate, author:$author){
    error
    success
  }
}
```

Input Variable:
```
{
   "title": "My First Post",
  "description": "Hey Hi hello",
  "publishDate": "2023-08-19",
  "author": "Mr Me"
}

```

Example response below
```
{
  "data": {
    "createPost": {
      "error": true,
      "success": false
    }
  }
}
```

*****


* Update Post
```
mutation updatePost($id: Int!,$title: String!, $description: String!, $publishDate: String, $author: String){
  updatePost(id: $id,title: $title, description: $description, publishDate:$publishDate, author:$author){
    error
    success
  }
}
```

Input Variable:
```
{
  "id": 5,
   "title": "New Post",
  "description": "Hey hello, this is new post",
  "publishDate": "2023-08-19",
  "author": "Mr Me"
}

```

Example response below
```
{
  "data": {
    "createPost": {
      "error": true,
      "success": false
    }
  }
}
```
*****



* Create Comment
```
mutation createComment($text: String!, $post: Int!, $author: String){
  createComment(text: $text, post: $post,  author:$author){
    error
    success
  }
}
```

Input Variable:
```
{
   "text": "Hey This looks nice",
  "post": 1,
  "author": "It's Me"
}

```

Example response below
```
{
  "data": {
    "createComment": {
      "error": null,
      "success": true
    }
  }
}
```
*****


* Get Post by ID
```
query post($id: Int!){
  post(id: $id){
    description
    commentSet{
      text
      author
    }
    
  }
}
```

Input Variable:
```
{
   "id": 1
}

```

Example response below
```
{
  "data": {
    "post": [
      {
        "description": "Hey guys here is my first post",
        "commentSet": [
          {
            "text": "Adding my first comment for the first post",
            "author": "Jerry"
          },
          {
            "text": "Hey This looks nice",
            "author": "It's Me"
          },
          {
            "text": "Hey This looks nice",
            "author": "It's Me"
          }
        ]
      }
    ]
  }
}
```
*****
