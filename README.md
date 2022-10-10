# Daily-Coding-Challenge

## DAY 1
PROBLEM : Cyclically rotate an array by one
Given an array, rotate the array by one position in clock-wise direction.
 
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
 
Example 2:
Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=105
0<=a[i]<=105


## DAY 2
PROBLEM : First and last occurrences of x
Given a sorted array arr containing n elements with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Example 1:
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last
             occurrence of 5 is at index 5.  

Example 2:
Input:
n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  6 6 

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107


## DAY 3
PROBLEM : Maximize sum(arr[i]*i) of an Array
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
