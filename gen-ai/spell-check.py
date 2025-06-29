from textblob import TextBlob

# sample text to check
text = 'I love progamming and machine learnig.'

# convert text to blob
blob = TextBlob(text)

# correct spelling in blob
corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)