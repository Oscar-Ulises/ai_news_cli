import os
import requests

from ai_news_cli.chat_session import openai_function
from ai_news_cli.image_generator import image_creator

def headlines_creator():
    url = "https://api.currentsapi.services/v1/latest-news?apiKey=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"
    try:
        response = requests.get(url)
        headlines = [news['title'] for news in response.json().get("news", [])]
        
        return headlines if headlines else ["No headlines found."]
    except Exception as e:
        return [f"Error fetching headlines: {e}"]

def main():
    headlines = headlines_creator()

    os.makedirs("images", exist_ok=True)

    print("\nWelcome to News\n")
    for i, headline in enumerate(headlines):
        print(f"Headline {i+1}: {headline}")
        image_creator(headline, f"headline_{i+1}")

        while True:
            user_input = input("Ask a question or press Enter to continue: ")
            if user_input.strip() == "":
                break
            response = openai_function(f"{user_input} (related to: {headline})")
            print(f"{response}\n")

if __name__ == "__main__":
    main()