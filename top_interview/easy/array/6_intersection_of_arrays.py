# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

def intersect(arr1, arr2):
    result = []

    for i in arr1:
        if i in arr2:
            result.append(i)
            arr2.remove(i)
                
    return result
