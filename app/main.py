from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "F-Off backend is running!"}

# --- placeholder endpoints we will fill later ---

@app.post("/deletion/draft")
def draft_placeholder():
    return {"subject": "placeholder subject", "body": "placeholder body"}

@app.post("/deletion/send")
def send_placeholder():
    return {"message": "placeholder - sending disabled"}
