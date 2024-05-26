from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def list_users():
    return [{"username": "Jim"}, {"username": "Pam"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
