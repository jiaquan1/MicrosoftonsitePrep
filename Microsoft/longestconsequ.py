
def longestConsecutive(nums):
    nums= set(nums)
    maxlen = 0
    while nums:
        n = nums.pop()
        l1=0
        l2=0
        i = n+1
        while i in nums:
            nums.remove(i)
            i+=1
            l1+=1
        i = n-1
        while i in nums:
            nums.remove(i)
            i-=1
            l2+=1
        maxlen = max(maxlen,l1+l2+1)
    return maxlen
if __name__=="__main__":
    nums=[100,4,200,1,3,2]
    print(longestConsecutive(nums))
        