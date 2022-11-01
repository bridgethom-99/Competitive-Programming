#User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        max = arr[0]
        sort = 0
        for j in range(1, i+1):
            if arr[j] > max:
                sort = j
                max = arr[j]
        return sort

    def selectionSort(self, arr, n):

        for i in range(n-1, 0, -1):
            j = self.select(arr, i)

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
