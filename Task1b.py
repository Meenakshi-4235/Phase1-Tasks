
import demoji

# Initialize the demoji module (this may download a dataset the first time it runs)
demoji.download_codes()

# Function to convert emojis to text descriptions
def convert_emojis_to_text(text):
    return demoji.replace(text, "")

# Sample text with emojis
text_with_emojis = "I love playing cricket 🏏 and ludo 🎲!"

# Convert emojis to text
text_without_emojis = convert_emojis_to_text(text_with_emojis)

print(text_without_emojis)
