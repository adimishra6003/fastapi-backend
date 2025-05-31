from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get('/')
async def root():
    return {"message": "Welcome to my API!"}


@app.get('/posts')
async def get_posts():
    return {"posts": "This is supposed to be a list of posts."}


@app.post('/createpost')
async def create_post(post: Post):
    # print(post)
    return {"new post": f"Title: {post.title} Content: {post.content} Published: {post.published} Rating: {post.rating}"}
