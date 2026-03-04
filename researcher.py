import asyncio
from crawl4ai import AsyncWebCrawler
import ollama
from time import time

async def research_item(url):
    print(f"🔍 Researching item from: {url}")
    start_time = time()
    async with AsyncWebCrawler() as crawl:
        content = await crawl.arun(url)
        raw_markdown = content.markdown

        print("🧠 Generating report using LLama...")
        response = ollama.chat(
            model="llama3.1:8b",
            messages=[{
                'role':'user',
                'content':f"Extract the current market price, key specs and 'pros' and 'cons' from this text. Format as a clean report:\n\n{raw_markdown[:4000]}" #content limit because of VRAM
            }]
        )
        report = response['message']['content']
        duration = time() - start_time
        print(f"✅ Research completed in {duration:.2f} seconds")
        print("\n--- ITEM REPORT ---")
        print(report)

        # Save to local mem
        with open("research_report.md","w",encoding="utf-8") as f:
            f.write(report)
        
        print("💾 Report saved to research_report.md")
    
if __name__ == "__main__":
    example_url = "https://www.example.com/product-page"
    asyncio.run(research_item(example_url))