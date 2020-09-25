'''
Reverse words in sentence

Reverse words in a given string, in linear time complexity.

Input: 'i like this program very much'
Output: 'much very program this like i'

Input: 'how are you'
Output: 'you are how'
'''

'''
Finish the function
'''


def reverse_words_in_sentence(sentence):
    words = sentence.split(' ')
    reverse_words = []

    for i in range((len(words) - 1), -1, -1):
        reverse_words.append(words[i])

    reverse_str = ' '.join(reverse_words)

    return reverse_str




###########
# Testing #
###########

# Test 1
# Correct result => 'much very program this like i'
print(reverse_words_in_sentence('i like this program very much'))

# Test 2
# Correct result => 'you are how'
print(reverse_words_in_sentence('how are you'))