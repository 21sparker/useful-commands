#!/usr/bin/env python3.9
import requests
from bs4 import BeautifulSoup
import re

def search_google(search_str):
    # Check if search_str is not valid
    if not search_str:
        print("None str")
        return
    if search_str.strip() == "":
        print("Empyt string")
        return
    
    # Request the html page from google
    r = requests.get("https://www.google.com/search", {"q": search_str})
    pattern = re.compile(r"</style>([\s\S]*)<footer>")
    match = pattern.search(r.text).groups()[0]

    soup = BeautifulSoup(match, 'html.parser')
    

if __name__ == '__main__':
    response = input("Search for:\n")
    search_google(response)
    