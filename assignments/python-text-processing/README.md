# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice string operations, file input/output, and text manipulation by building a small text analysis tool in Python.

## 📝 Tasks

### 🛠️ Read and Clean Text File

#### Description

Create a function to read contents from a text file and clean the data for analysis.

#### Requirements
Completed program should:

- Open a specified text file in read mode using `with open(..., 'r')`.
- Read the file contents into a string.
- Normalize whitespace by removing extra spaces and converting line breaks to single spaces.
- Convert text to lowercase and strip punctuation from words.
- Return a cleaned list of words.

### 🛠️ Word Frequency Analysis

#### Description

Count how often each word appears in the cleaned text and display the most common words.

#### Requirements
Completed program should:

- Accept the cleaned list of words as input.
- Use a dictionary (or `collections.Counter`) to count word frequency.
- Print the top 10 most common words with their counts.
- Handle ties in frequency by sorting alphabetically within equal counts.

### 🛠️ Save Results to File

#### Description

Write analysis results to an output file with formatting for easy review.

#### Requirements
Completed program should:

- Create or overwrite an output text file using `with open(..., 'w')`.
- Write a header line with analyzed filename and date/time.
- Write each word + frequency on separate lines.
- Save a summary line with total unique words and total words processed.

### 🛠️ Optional: Search and Replace Tool

#### Description

Implement a utility function that searches for a user-specified word in the text and optionally replaces it.

#### Requirements
Completed program should:

- Prompt user for a search term and replacement term.
- Count occurrences of the search term in the cleaned text.
- Optionally perform replacement and save updated text to a new output file.
- Confirm action with a printed message, e.g., `Replaced 5 instances of "old" with "new"`.
