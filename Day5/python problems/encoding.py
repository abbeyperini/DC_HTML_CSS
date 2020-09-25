'''
Encoding string

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

Input: 'AAAABBBCCDAA'
Output: '4A3B2C1D2A'
'''
'''
Finish the function below
'''



def encoding(word):
    output = []
    num = 0
    letter = ''
    
    for i in range(0, len(word)):
        if i == 0:
            num = 1
            letter = word[0]
        else:
            if word[i] == letter:
                num += 1
            elif word[i] != letter:
                output.append(str(num))
                output.append(letter)
                num = 1
                letter = word[i]
    
    output.append(str(num))
    output.append(letter)

    output_str = ''.join(output)
    return output_str


###########
# Testing #
###########

# Correct result => '4A3B2C1D2A'
print(encoding('AAAABBBCCDAA'))