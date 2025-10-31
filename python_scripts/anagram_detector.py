# Anagram Detector

# An anagram is formed by rearranging the letters of another word, 
# using all the original letters exactly once.

# Assume both strings s and t contain only lowercase letters
def is_anagram(s, t):

    # Check lengths (O(1))
    if len(s) != len(t):
        return False

    char_counts = {}    # empty dictionary

    # Count frequencies in s (O(n))
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Decrement frequencies using t (O(n))
    for char in t:
        # check if char is in dictionary AND count > 0
        if char_counts.get(char, 0) > 0:
            char_counts[char] -= 1
        else:
            return False
    
    return True
    

if __name__ == "__main__":
    print(f"Is 'listen' an anagram of 'silent'? {is_anagram('listen', 'silent')}")
    print(f"Is 'rat' an anagram of 'car'? {is_anagram('rat', 'car')}")
    print(f"Is 'cat' an anagram of 'cat'? {is_anagram('cat', 'cat')}")

    
