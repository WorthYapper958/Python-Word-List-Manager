import os

def remove_duplicates_and_sort(filepath):
    # Check if the file exists
    if not os.path.exists(filepath):
        # Create a new file if it does not exist
        with open(filepath, 'w', encoding='utf-8') as file:
            pass
        print(f"The file '{filepath}' was created because it was not found.")
        return 0, 0

    # Read the words from the file
    with open(filepath, 'r', encoding='utf-8') as file:
        words = file.readlines()

    # Remove whitespace and newlines
    words = [word.strip() for word in words]

    # Count the number of duplicates
    count_before = len(words)
    words = sorted(set(words))
    duplicate_count = count_before - len(words)

    # Write the sorted words back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

    return duplicate_count, len(words)

def add_word(filepath, new_word):
    # Read the current words from the file
    with open(filepath, 'r', encoding='utf-8') as file:
        words = file.readlines()

    # Remove whitespace and newlines
    words = [word.strip() for word in words]

    # Check if the new word already exists
    if new_word in words:
        print(f"The word '{new_word}' is already in the word list and cannot be added.")
        return

    # Add the new word to the list
    words.append(new_word)

    # Sort the list alphabetically
    words = sorted(words)

    # Write the updated list back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def main():
    filepath = 'word_list.txt'

    # Remove duplicate words and sort at the start
    duplicate_count, word_count = remove_duplicates_and_sort(filepath)
    print(f"Number of duplicates found: {duplicate_count}")
    print(f"Number of words after sorting and removing duplicates: {word_count}")

    # User can add new words
    while True:
        new_word = input("Enter a new word (or 'x' to quit): ")
        if new_word.lower() == 'x':
            break
        add_word(filepath, new_word)

if __name__ == "__main__":
    main()
 
