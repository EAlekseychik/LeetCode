# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

def moveZeroes(nums):
	lastPointer = 0

	for i in range(len(nums)):
		if nums[i] != 0:
			nums[lastPointer] = nums[i]
			lastPointer += 1

	for i in range(lastPointer, len(nums)):
		nums[i] = 0
