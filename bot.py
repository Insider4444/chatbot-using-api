import requests
import json

url = "https://ai-chatbot.p.rapidapi.com/chat/free"

headers = {
  "Your Rapid Api Headers Here" # Get Your Api Keys Here https://rapidapi.com/farish978/api/ai-chatbot/
}

while True:
  message = input("\nEnter your message (or type 'q' to quit): ")
  if message == 'q':
    break

  querystring = {"message": message, "uid": "user1"}

  response = requests.request("GET", url, headers=headers, params=querystring)

  # parse the JSON response
  parsed_response = json.loads(response.text)

  # extract the "response" field
  response_text = parsed_response['chatbot']['response']

  # print the response text
  print("\n" + response_text)