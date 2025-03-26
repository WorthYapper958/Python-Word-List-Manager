# Python-Word-List-Manager
This Python script manages a word list stored in a text file (word_list.txt). It ensures that the list is always sorted alphabetically and free of duplicates. Upon starting, the script checks for duplicate entries and sorts the list, reporting the number of duplicates found and the total number of unique words. Users can interactively add new words to the list, with the script preventing the addition of duplicate words and maintaining the alphabetical order. If the word list file does not exist, the script automatically creates it.

# Usage
1. Preparation:
   - Ensure you have a file named `word_list.txt` in the same directory as the script.
   - If the file doesn't exist, the script will create it automatically.

2. Running the Script:
   - Execute the script `word_list.py`.
   - Upon starting, the script will:
     - Check for duplicate entries in `word_list.txt`.
     - Remove any duplicates and sort the remaining words alphabetically.
     - Display the number of duplicates found and the total number of unique words.

3. Adding Words:
   - The script will prompt you to enter new words. Type a word and press Enter.
   - If the word is already in the list, the script will notify you and prevent adding it again.
   - If the word is new, it will be added to the list, and the list will be automatically sorted alphabetically.

4. Exiting the Program:
   - Type `x` and press Enter to stop the program.

# Word List Format
- Words in `word_list.txt` are listed one per line.
- The list is always sorted alphabetically.
- Duplicates are automatically removed from the list.
