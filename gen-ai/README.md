# Gen AI 101
## Gen AI
### What is Gen AI?
- Generative Artificial Intelligence
- Creates new content based on prompts and large language models (LLMs)

### How does AI work?
- LLMs are trained using natural language processing (NLP) techniques
- NLP is a branch of machine learning that teaches computers to understand, interpret, and generate human language
  - examples: ChatGPT, Claude, Gemini
- LLMs use patterns, sequences, and datasets to generate text, translate languages, and answer questions

#### AI branches visual?
- Machine Learning
  - Natural Language Processing
    - Large Language Models
      - Gen AI

## Language Models
### How do LLMs understand and generate human language?
- Sequences - trained on datasets to recognize sequences, eg. predicting the next letter or word, filling in blanks (Wheel of Fortune)
- NLTK (Natural Language ToolKit) - python library for text generation, spell check, translation

## Tokens
### How are tokens used to train LLMs?
- Tokens: Small units of data used to train gen AI models. could be whole words, subwords, or other content.
  - smallest units of meaning => structure and semantics of text
- Tokenization: Process of making raw data trainable for language models. may include splitting text into individual words.

## N-grams
### How are n-grams used to train LLMs?
- N-grams: sequences of 'n' tokens from a given sample of text. used as patterns to help language models make predictions. analyze sequences to understand how words are commonly used together.
  - analyze the probability of certain word sequences based on their occurrence in a large dataset

### What are the 3 popular models of n-grams?
- Unigram - single character or word
- Bigram - 2 consecutive characters or words
- Trigram - 3 consecutive characters or words

### How can you create n-grams?
- Use the nltk python library to first tokenize a string, and then generate ngrams from the tokens

## Glossary
- Gen AI: Generative Artificial Intelligence
- LLMs: Large Language Models
- NLP: Natural Language Processing