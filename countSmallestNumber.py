class Solution:
    def countSmallest(self, arr):
        ara = []
        for i in range(len(arr)):
            count = 0
            if arr[i] < 0:
                ara.append(0)
            else:
                for j in range(i + 1, len(arr)):
                    if arr[i] > arr[j]:
                        count += 1
                ara.append(count)
        return ara

if __name__ == "__main__":
    size = int(input("enter the array size: "))
    arr = []
    for i in range(size):
        arr.append(int(input()))
    answer = Solution()
    print(answer.countSmallest(arr))
