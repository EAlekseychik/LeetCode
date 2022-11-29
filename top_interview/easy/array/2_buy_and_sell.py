# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

def countProfit(arr):
    if len(arr) == 1:
        return 0

    maxProfit = 0
    prev = arr[0]

    for i in arr:
        diff = i - prev

        if diff > 0:
            maxProfit += diff

    return maxProfit
