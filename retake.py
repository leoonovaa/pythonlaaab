import requests
from bs4 import BeautifulSoup
import csv

class PubMedParser:
    def __init__(self, search_query, download_folder):
        self.base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={search_query}"
        self.download_folder = download_folder
    
    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_articles(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        articles = []
        for article in soup.select(".docsum-content"):
            try:
                title = article.select_one(".docsum-title").text.strip()
                authors = article.select_one(".docsum-authors").text.strip()
                journal = article.select_one(".docsum-journal-citation").text.strip()
                link = "https://pubmed.ncbi.nlm.nih.gov" + article.select_one(".docsum-title")['href']
                articles.append((title, authors, journal, link))
            except AttributeError:
                print("Error parsing article metadata.")
        return articles

    def save_metadata(self, articles):
        csv_file = f"{self.download_folder}/pubmed_articles.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Authors", "Journal", "Link"])
            writer.writerows(articles)
        print(f"Metadata saved to {csv_file}")

    def run(self):
        page_content = self.fetch_page(self.base_url)
        if page_content:
            articles = self.parse_articles(page_content)
            self.save_metadata(articles)
            
            # Вивід знайдених статей у термінал
            print("\nЗнайдені статті на PubMed:\n")
            for i, (title, authors, journal, link) in enumerate(articles, start=1):
                print(f"{i}. {title}")
                print(f"   Authors: {authors}")
                print(f"   Journal: {journal}")
                print(f"   Link: {link}\n")


if __name__ == "__main__":
    search_query = "machine+learning+health"
    download_folder = "downloads"
    parser = PubMedParser(search_query, download_folder)
    parser.run()