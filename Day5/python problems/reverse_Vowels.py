'''
Reverse Vowels

Given a text string, create and return a new string constructed by finding all its vowels (for
simplicity, in this problem vowels are the letters in the string 'aeiouAEIOU') and reversing their
order, while keeping all non-vowel characters exactly as they were in their original positions.

Input: 'Hello world'
Output: 'Hollo werld' 
'''
'''
Finish The function below
'''

def reverse_vowels(sentence):
    sentence_array = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    popped_vowels = []
    indices = []

    for i in range(0, len(sentence)):
        sentence_array.append(sentence[i])

    for i in range(0, len(sentence_array)):
        if sentence_array[i] in vowels:
            popped_vowels.append(sentence_array[i])
            indices.append(i)

    indices.reverse()

    for i in range(0, len(indices)):
        sentence_array.pop(indices[i])
        sentence_array.insert(indices[i], popped_vowels[i])

    sentence_str = ''.join(sentence_array)

    return sentence_str


###########
# Testing #
###########

# Test 1
# Correct result => 'ubcdofghijklmnepqrstavwxyz'
print(reverse_vowels('abcdefghijklmnopqrstuvwxyz'))

# Test 2
# Correct result => 'Hollo werld'
print(reverse_vowels('Hello world'))