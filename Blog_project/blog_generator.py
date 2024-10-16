import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key is available
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

def generate_blog(paragraph_topic):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Write a paragraph about the following topic: {paragraph_topic}"}
            ],
            max_tokens=400,
            temperature=0.3
        )
        retrieve_blog = response.choices[0].message['content'].strip()
        return retrieve_blog
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    print(generate_blog('Why NYC is better than your city.'))