# main.py

from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint that returns 'Hello, World!'.

    Returns:
        dict: A dictionary with a 'message' key and 'Hello, World!' as value.
    """
    return {"message": "Hello, World!"}
