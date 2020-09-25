'''
Swap the frst and the last word

Given an string, you need to swap the first and last word in linear time.
Everything between should stay in same order.

Sample input: 'i like this program very much'
Sample output: 'much like this program very i'
'''

# Finish the below function

def swap_first_and_last_word(sentence):
    words = sentence.split(' ')
    first = words.pop(0)
    last = words.pop(-1)
    words.append(first)
    words.insert(0, last)
    swapped = ' '.join(words)
    return swapped





###########
# Testing #
###########

# Test 1
# Correct result => 'practice makes perfect
print(swap_first_and_last_word('perfect makes practice'))

# Test 2
# Correct result => 'much like this program very i'
print(swap_first_and_last_word('i like this program very much'))