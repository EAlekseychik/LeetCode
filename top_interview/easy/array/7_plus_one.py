# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

def plusOne(digits):
    num = int("".join([str(i) for i in digits])) + 1
        
    return [int(i) for i in str(num)]
