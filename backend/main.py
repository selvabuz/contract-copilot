from fastapi import FastAPI, UploadFile, File
from parser import extract_chunks
from contract_llm import analyze_chunks

app = FastAPI()

@app.post("/analyze")
async def analyze_contract(file: UploadFile = File(...)):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    chunks = extract_chunks(path)
    results = analyze_chunks(chunks)
    return {"results": results}