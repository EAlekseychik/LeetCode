# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

def singleNumber(arr):
	return len(set(arr)) < len(arr)
