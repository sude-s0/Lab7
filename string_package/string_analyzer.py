from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

def main():
    sentence = input("Enter a sentence: ")

    print("\n--- Operation started ---")
    print("Reversed:", reverse_string(sentence))
    print("Capitilized:", capitalize_words(sentence))

    no_punc = remove_punctuation(sentence)
    print("without punctuation:", no_punc)

    print("Character count:", count_characters(no_punc))
    print("Word count:", count_words(no_punc))
    print("avg word count:", round(average_word_length(no_punc), 2))

if __name__ == "__main__":
    main()
