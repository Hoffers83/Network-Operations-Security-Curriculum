import requests
from bs4 import BeautifulSoup

def get_search_results(query):
    # Bing search URL (you can sign up for the Bing Search API to get an API key)
    search_url = "https://www.bing.com/search"
    params = {"q": query}

    # Make the HTTP request to the search engine
    response = requests.get(search_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all search result titles
        titles = soup.find_all('h2')

        # Extract and display the top 10 search result titles
        for i, title in enumerate(titles[:10], start=1):
            print(f"{i}. {title.get_text(strip=True)}")
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")


def main():
    # Prompt the user to enter a search prompt
    query = input("Enter a search prompt: ")

    # Get and display the search results
    get_search_results(query)

if __name__ == "__main__":
    main()
