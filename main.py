from fastapi import FastAPI, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

my_posts = [{"id": 1, "title": "Post 1", "content": "Content 1", "published": True, "rating": 3},
            {"id": 2, "title": "Post 2", "content": "Content 2", "published": True, "rating": 4}]


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
    return {"posts": my_posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    my_posts.append({"id": len(my_posts)+1, "title": post.title,
                    "content": post.content, "published": post.published, "rating": post.rating})
    return {"posts": my_posts}
