# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

def containsDuplicate(arr):
    return len(set(arr)) < len(arr)
