# DAY 6
# PROBLEM : Arranging the array
"""
You are given an array of size N. Rearrange the given array in-place such that all the negative numbers occur before positive numbers.(Maintain the order of all -ve and +ve numbers as given in the original array).

Example 1:
Input:
N = 4
Arr[] = {-3, 3, -2, 2}
Output:
-3 -2 3 2
Explanation:
In the given array, negative numbers
are -3, -2 and positive numbers are 3, 2. 
 
Example 2:
Input:
N = 5
Arr[] = {2, -4, 7, -3, 4}
Output:
-4 -3 2 7 4

Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(Log(N))

Constraints:
1 ≤ N ≤ 107
-1018 ≤ Elements of array ≤ 1018
"""

def Rearrange( a, n):
    pos = []
    neg = []
    ans = a
    a = []
    
    
    for i in range(n):
        
        if(ans[i] < 0):
            neg.append(ans[i])
        else:
            pos.append(ans[i])
            
    for i in range(len(neg)):
        a.append(neg[i])
        
    for j in range(len(pos)):
        a.append(pos[j])
    
    print(*a)


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Rearrange(a, n)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends