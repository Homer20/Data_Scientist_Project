import pandas as pd
import re
import emoji

# Read the CSV file into a DataFrame
df = pd.read_csv('crunchyroll_modified.csv')

# Function to remove emojis from text
def remove_emojis(text):
    if pd.isna(text):  # Check if the text is NaN
        return ''  # Return an empty string for NaN values
    return emoji.demojize(text)

# Remove emojis from the review_text column
df['review_text'] = df['review_text'].apply(remove_emojis)

# Function to count words in text
def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

# Ensure review_text has at least 50 words
df['word_count'] = df['review_text'].apply(count_words)
df = df[df['word_count'] >= 50]

# Drop the word_count column if you don't need it anymore
df = df.drop(columns=['word_count'])

# Save the modified DataFrame back to a CSV file
df.to_csv('new_crunchyroll.csv', index=False)
