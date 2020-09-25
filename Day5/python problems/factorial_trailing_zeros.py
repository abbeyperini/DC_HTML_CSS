'''
Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
Input: 3
Output: 0
Output explanation: 3! = 6, no trailing zero.
Input: 5
Output: 1
Output explanation: 5! = 120, one trailing zero.
'''

# Finish below function

def trailing_zeroes(n):
    just_nums = []
    total = n

    for i in range((n - 1), 0, -1):
            just_nums.append(i)
    
    for i in range(0, len(just_nums)):
        total *= just_nums[i]

    total_str = str(total)
    zeros = 0

    for i in range(((len(total_str)) - 1), -1, -1):
        if total_str[i] == "0":
            zeros += 1
        else:
            break
    
    return total, zeros

print(trailing_zeroes(300))

    



    