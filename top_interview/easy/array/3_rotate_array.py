# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

def rotateArray(arr):
    length = len(arr)
    if length == 1 or k == 0 or k == len(arr):
        return arr

    if k > length:
        k %= length
        
    arr[length-k:], arr[:length-k] = arr[:length-k], arr[length-k:]
