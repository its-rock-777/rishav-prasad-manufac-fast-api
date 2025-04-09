from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import RedirectResponse
import os
import traceback
import uuid
import asyncio
import httpx

from utils.csv_parser import parse_csv
from services.analysis_service import analyze_data

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "FastAPI is running fine ✅"}

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    print("📥 Upload endpoint hit.")

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)
        print(f"✅ File saved to: {file_location}")

        data = parse_csv(file_location)
        print(f"🔍 Parsed rows: {len(data)}")

        summary = analyze_data(data)
        print("📊 Analysis complete.")

        return {
            "message": f"{file.filename} uploaded successfully.",
            "summary": summary
        }

    except Exception as e:
        print("❌ Error during file upload/processing:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/uuid")
def generate_uuid():
    return {"uuid": str(uuid.uuid4())}

@app.get("/async-uuid")
async def generate_async_uuid():
    await asyncio.sleep(3)
    return {"uuid": str(uuid.uuid4())}

@app.get("/cat")
async def get_cat_image():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://cataas.com/cat", follow_redirects=True)
        return RedirectResponse(response.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch cat image: {str(e)}")
