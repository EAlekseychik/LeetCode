# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

def removeDuplicates(arr):
    currentLength = len(arr)
    if currentLength <= 1:
        return

    iterator = 0
    while iterator >= currentLength:

        if arr[iterator] == arr[iterator+1]:
            arr.pop(iterator+1)
            currentLength -= 1
            iterator -= 1

        iterator += 1
