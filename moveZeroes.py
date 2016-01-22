class Solution(object):
	def moveZeroes(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: void Do not return anything, modify nums in-place instead.
    	"""
    	swap_length = len(nums)-1
    	position = 0
    	print 'swap length = ' , swap_length
    	for index in nums:
        	print 'current value in index', nums[position]
        	print 'current position', position
        	if nums[position] == 0:
        		for i in range (position, swap_length):
        			print 'i= ', i
        			nums[i] == nums[i+1]
        		
        		nums[swap_length] == 0 #move 0 to the end of the list
        		print 'position = ', position
        		swap_length -= 1 #next round swap 1 less item in the list
        		print 'swap length= ', swap_length
        	
        	print 'sssss'
        	if nums[postion] != 0:
		    	position += 1
		    	print ' after incrment position',posision
				
	#def printList(self,nums):
	#	for value in nums:
	#		print value

solution = Solution()
nums = [1,2,0,0,0,2,2,0,0,9,9]
solution.moveZeroes(nums)
for value in nums:
	print value
#solution.printList(nums)