# DAY 3
# PROBLEM : Maximize sum(arr[i]*i) of an Array
""" 
Given an array A of N integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n 1.
You are allowed to rearrange the elements of the array.
Note: Since output could be large, hence module 10^9+7 and then print answer.

Example 1:
Input : Arr[] = {5, 3, 2, 4, 1}
Output : 40
Explanation:
If we arrange the array as 1 2 3 4 5 then 
we can see that the minimum index will multiply
with minimum number and maximum index will 
multiply with maximum number. 
So 1*0+2*1+3*2+4*3+5*4=0+2+6+12+20 = 40 mod(109+7) = 40

Example 2:
Input : Arr[] = {1, 2, 3}
Output : 8

Expected Time Complexity: O(nlog(n)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
1 ≤ Ai ≤ N
"""

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        sum = 0
        a.sort()
        for i in range(n):
            sum += a[i] * i
        
        # The remainder obtained after the division operation on two operands is known as modulo operation.
        # The reason of taking Mod is to prevent integer overflows.
        # m = 10^9+7 = 1000000007
        
        mod = 1000000007    
        return sum % mod
      
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))