from typing import List

def count_unique_words(words: List[str]) -> int:
        if words:
            words_set = set(words)
            my_list_no_duplicates = list(words_set)
            return len(my_list_no_duplicates)
        else: 
            return 0
        

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
