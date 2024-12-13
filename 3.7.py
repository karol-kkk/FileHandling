import re

def count_vowels(text):
    # Regular expression to match all vowels (both lowercase and uppercase)
    vowels_pattern = r'[aeiouAEIOU]'
    # Use re.findall to find all occurrences of vowels
    vowels = re.findall(vowels_pattern, text)
    return len(vowels)

# Main program
text = input("Enter the text: ")
vowel_count = count_vowels(text)

print(f"Number of vowels: {vowel_count}")
