# Levenshtein Distance CLI

This project is a command-line interface (CLI) that calculates the Levenshtein distance between an input word and words from an English dictionary. It then returns the closest matching words based on the Levenshtein distance.

## Features

- Takes an input word from the user.
- Downloads an English dictionary and compares the input word to the dictionary.
- Calculates the Levenshtein distance for each word in the dictionary.
- Outputs the top n closest words based on the Levenshtein distance.

## How It Works

1. The script downloads a dictionary of English words from an online source.
2. The user enters a word to be compared.
3. For each word in the dictionary, the Levenshtein distance is calculated.
4. The script sorts the words based on the calculated distances and returns the 10 closest matches.

## Levenshtein Distance

The **Levenshtein distance** is a measure of the difference between two sequences. It calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

### Example

For example, the Levenshtein distance between `"kitten"` and `"sitting"` is 3 because the following three edits change one word into the other:
- kitten → sitten (substitution of 'k' with 's')
- sitten → sittin (substitution of 'e' with 'i')
- sittin → sitting (insertion of 'g')

## Installation

1. Make sure you have Python installed (version 3.6 or higher).
2. Clone this repository or download the code.
3. Install the required libraries, if any. The script uses the `requests` library to download the dictionary.

   You can install `requests` using pip:
   ```bash
   pip install requests
