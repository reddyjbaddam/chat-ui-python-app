import requests
import json

# Replace with your Hugging Face API token
api_token = "XYX"

# Set the API endpoint and headers
endpoint = "https://api-inference.huggingface.co/models/fka/awesome-chatgpt-prompts"
endpoint = "https://api-inference.huggingface.co/models/ansumanpandey/codgen-finetuned-SQLQueryGeneration"


headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Define the prompt
prompt = "Give me sql query to find min and max salary from employee table"

# Send the POST request
response = requests.post(endpoint, headers=headers, json={"inputs": prompt})

# Check if the response was successful
if response.status_code == 200:
    # Get the response text
    response_text = response.json()[0]["generated_text"]
    print("Response:")
    print(response_text)
else:
    print("Error:", response.text)
