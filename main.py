from fastapi import FastAPI
from typing import Optional


# Create an instance of the class FastApi
app = FastAPI()

@app.get('/blog')
def index(limit:int= 10,published:bool=True,sort: Optional[str]=None):
    #Only get 10 published blogs
    if published:
        return {
            "data": f"{limit} published blogs from the db"
        }
    else:
        return{
            "data": f"{limit} all blogs from the db"
        }


@app.get("/blog/unpublished")
def unpublished():
    return {
        "data": "all unpublished blogs."
    }


@app.get("/blog/{id}")
def show(id:int):
    # fetch blog with id = id 
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id:int):
    #fecth comments of blog with id = id
    return {
        "data": {id: f"This is the comment number {id}."}
        }

