from fastapi import FastAPI

app = FastAPI()

@app.get("/is_palindrome/{word}")
def is_palindrome(word: str):
    return word == word[::-1]