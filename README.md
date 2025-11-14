# WebScrape AI – Scraper IA Universel

> **Challenge PlayHub** : Web Scrapper Utility  
> **Récompense** : 25 000 PLAI

## Fonctionnalités
- Entre une URL → scrape automatique
- IA détecte et structure les données (produits, prix, avis…)
- Nettoyage intelligent (supprime pubs, doublons)
- Export JSON/CSV + Google Sheets
- Anti-blocage (rotations IP, delays)

## Stack
- Python + Playwright + Llama 3 (via Ollama)
- Frontend simple (HTML + Tailwind)
- API FastAPI

## Lancer localement
```bash
pip install -r requirements.txt
playwright install
uvicorn main:app --reload
