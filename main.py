from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import playwright.sync_api
import ollama
import json
import re

app = FastAPI(title="WebScrape AI")

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape")
def scrape(req: ScrapeRequest):
    try:
        with playwright.sync_api.sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(req.url, wait_until="networkidle")
            content = page.content()
            browser.close()

        # Nettoyage HTML → texte
        text = re.sub(r'<[^>]+>', '', content)
        text = re.sub(r'\s+', ' ', text).strip()[:4000]

        # IA structure les données
        prompt = f"Convertis ce texte en JSON structuré (produits, prix, avis, etc.) :\n\n{text}"
        response = ollama.generate(model='llama3:8b', prompt=prompt)
        
        try:
            structured = json.loads(response['response'])
        except:
            structured = {"raw_text": text[:1000], "note": "IA structuring in progress"}

        return {"data": structured, "source": req.url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
