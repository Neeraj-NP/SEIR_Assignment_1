import sys
import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    return response.text


def parsing(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string if soup.title else "Title not found"

    body_content = soup.get_text(separator=" ")

    all_links = []
    for tag in soup.find_all("a", href=True):
        all_links.append(tag["href"])

    return title.strip(), body_content.strip(), all_links


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Link is not provided. Please provide one URL as an argument.")
        exit()

    url = sys.argv[1]
    html = fetch_page(url)

    title, body, links = parsing(html)

    print("\npage title:\n", title)
    print("\npage body:\n", body[:])
    print("\nLinks:")
    for l in links:
        print(l)