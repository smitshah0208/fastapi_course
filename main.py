from fastapi import FastAPI


# Create an instance of the class FastApi
app = FastAPI()

@app.get('/')
def index():
    return {
        "data": {"name": "SMIT","age":26}
    }

@app.get("/about")
def about():
    return {"data": "about page"}
