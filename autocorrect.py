#!/usr/bin/env python3

""" Reads a file with misspelled and corrected words."""

import sys

__author__ = "Lydia Frame"
__date__ = "04/19/2025"

def main():

    """Prompts for a correction file and a line of text."""

    # Prompt the user for the file containing the misspelled and correct words
    filename = input("File? ")
    print()

    # Create a dictionary to store the corrections
    corrections = {}

    # Read the correction file and populate the dictionary
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Process each line to get misspelled and correct words
                misspelled, correct = line.strip().split('=')
                corrections[misspelled] = correct
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    # Prompt the user for the line of text to correct
    line = input("Line? ")
    print()

    # Split the line into words
    words = line.split()

    # Correct the words based on the dictionary
    corrected_line = []

    for word in words:
        # If the word is in the dictionary, replace it; otherwise, leave it as is
        corrected_line.append(corrections.get(word, word))

    # Join the corrected words into a sentence and print it
    print(" ".join(corrected_line) + " ")


if __name__ == "__main__":
    main()
