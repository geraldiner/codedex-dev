from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Prepare the Data
# Create a dataset of text and their corresponding labels.

texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
]

# Convert Text to Numerical Data
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

# Split the Data into Training
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# Train the Naive Bayes Classifier
model = MultinomialNB()
model.fit(x_train, y_train)

# Make Predictions on the Test Set
y_pred = model.predict(x_test)

# Evaluate the Model's Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
