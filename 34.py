def count_word_occurrences(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store word occurrences
    word_count = {}

    # Count occurrences of each word
    for word in words:
        # Remove punctuation and convert to lowercase for better matching
        cleaned_word = word.strip(".,!?").lower()

        # Update the count in the dictionary
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
        # word_count.get(cleaned_word, 0): The get method is used to retrieve the value associated with the key
        # cleaned_word from the dictionary word_count. If the key is not present, it returns the default value 0.

    return word_count

# Example usage:
input_sentence = input("Enter sentence : ")
result = count_word_occurrences(input_sentence)

# Print the word occurrences
for word, count in result.items():
    print(f"{word}: {count}")
