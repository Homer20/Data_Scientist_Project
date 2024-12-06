import pandas as pd
import requests
import json
import os

api_key = os.getenv('X-OAI-API-KEY')
if not api_key:
    raise ValueError("API key not found in environment variables. Please set X-OAI-API-KEY.")

url = "https://api.originality.ai/api/v1/scan/ai"

df = pd.read_csv('sorted_crunchyroll.csv', usecols=['review_text'], encoding='latin1')

original_scores = []
ai_scores = []

for index, row in df.iterrows():
    post_text = row['review_text']

    payload = json.dumps({
        "content": post_text,
        "aiModelVersion": "2",
        "storeScan": "false"
    })

    headers = {
        'X-OAI-API-KEY': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        score = response.json().get('score')
        if score:
            original_scores.append(round(score.get('original') * 100))  # Append int64 score directly
            ai_scores.append(round(score.get('ai') * 100))  # Append int64 score directly
        else:
            # Handle the case where the response doesn't contain the expected JSON structure
            original_scores.append(None)
            ai_scores.append(None)
    else:
        # Handle API errors
        print(f"Error processing post at index {index}: {response.text}")
        original_scores.append(None)
        ai_scores.append(None)

# Convert the lists to regular Python integers after the loop
original_scores = [int(score) if score is not None else None for score in original_scores]
ai_scores = [int(score) if score is not None else None for score in ai_scores]

df['Originality Score (%)'] = original_scores
df['AI Score (%)'] = ai_scores

# Save the DataFrame to a CSV file with both the review content and the scores
df.to_csv('crunchyroll_reviews.csv', index=False)
