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


def word_freq(text_data):
    stop_word = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    wordss = ""
    for c in text_data:
        if c.isalnum():
            wordss += c
        else:
            wordss += " "
    word_list = wordss.split()

    freq = {}
    for i in word_list:
        i = i.lower()
        if i not in stop_word:
            if i in freq:

                freq[i] += 1
            else:
                freq[i] = 1

    return freq


P = 53
M = 2**64
def hashing(word):

    h = 0
    power = 1

    for ch in word:
        h = (h + ord(ch) * power) % M
        power = (power * P) % M

    return h