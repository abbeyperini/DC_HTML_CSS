'''
Reverse string
Reverse string, in linear time complexity.
Input: 'i like this program very much'
Output: 'hcum yrev margorp siht ekil i'
Input: 'how are you'
Output: 'uoy era woh'
'''
'''
Finish the function
'''
def reverse_sentence(sentence):
    reverse = []
    
    for i in range((len(sentence) - 1), -1, -1):
        reverse.append(sentence[i])

    reverse_str = ''.join(reverse)
    
    return(reverse_str)



###########
# Testing #
###########

# Test 1
# Correct result => 'hcum yrev margorp siht ekil i'
print(reverse_sentence('i like this program very much'))

# Test 2
# Correct result => 'uoy era woh'
print(reverse_sentence('how are you'))