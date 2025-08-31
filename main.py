from fastapi import FastAPI

app = FastAPI()

@app.get("/blog")
def index(limit: int, published: bool,sort):
    if published:
        return {"data": f"Blog list {limit} published blogs from the database"}
    else:
        return {"data": f"Blog list {limit} unpublished blogs from the database"}
    

@app.get("/blog/{id}")
def show(id: int):
    return {"data": f"Blog number {id}"}
@app.get("/blog/unpublished")
def unpublished():
        return {"data": "all unpublished blogs"}
@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": ["Comment 1", "Comment 2"]}



