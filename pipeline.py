from time import time

import ollama
from ddgs import DDGS
from pydantic import BaseModel
import json

class ImageAnalysis(BaseModel):
    item_name: str
    brand: str
    search_query: str

def run_pipeline(image_path):
    start_time = time()
    print("Phase 1:👀 Analyzing Image...")

    response = ollama.chat(
        model="llama3.2-vision",
        format=ImageAnalysis.model_json_schema(),
        messages=[{
            'role':'user',
            'content':'Analyze this image. Create a search query to find the current market price of this item.',
            'images':[image_path]
        }]
    )

    analysis = ImageAnalysis.model_validate_json(response['message']['content'])
    
    print(f"✅ Identified: {analysis.item_name} by {analysis.brand}")
    print(f"🔍 Generated Query: {analysis.search_query}")

    print("Phase 2:🌐 Searching the web...")
    
    with DDGS() as ddgs:
        results = list(ddgs.text(analysis.search_query,max_results=3))
    duration = time() - start_time
    print("--- TOP RESULTS ---")
    for i, res in enumerate(results,1):
        print(f"{i}. {res['title']}\n   Link: {res['href']}")
    print(f"⏱️  Pipeline completed in {duration:.2f} seconds")

if __name__ == "__main__":
    run_pipeline('test.jpg')