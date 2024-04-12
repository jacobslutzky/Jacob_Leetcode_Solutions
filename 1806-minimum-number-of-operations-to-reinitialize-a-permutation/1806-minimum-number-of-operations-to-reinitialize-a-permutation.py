class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = [i for i in range(n)]
        og_perm = [i for i in range(n)]
        count = 0
        while perm != og_perm or count == 0:
            for i in range(len(arr)):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n//2+(i-1)//2]

            perm = arr.copy()
            count += 1

        
        return count