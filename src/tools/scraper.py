import requests
from bs4 import BeautifulSoup

def scrape_page(url: str) -> str:
    """
    Fetch and extract readable text from a webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(separator=" ")
        return text[:3000]  # limit length for agent processing

    except Exception as e:
        return f"Error scraping {url}: {e}"
