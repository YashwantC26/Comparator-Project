from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

@app.get("/api")
def handler():
    return {"status" : "ok"}

class BenchmarkRequest(BaseModel):
    prompt: str
    
   

@app.post("/api/benchmark")
def handler2(param : BenchmarkRequest):
    categories = classify_task(param.prompt)
    return {"prompt" : param.prompt, "categories" : categories}


def classify_task(prompt : str):
    words = {"code" : "coding" , "read" : "reading", "write" : "writing", "think" : "reasoning"}
    list_of_categories = []
    prompt = prompt.casefold()
    for word in words:
        if word in prompt:
            list_of_categories.append(words.get(word))
    return list_of_categories
            
    
    

