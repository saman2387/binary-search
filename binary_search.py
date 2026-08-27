nums = [1, 3, 5, 7, 9, 11]
target = int(input("Find: "))
low, high = 0, len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print("Found at index", mid)
        break
    if nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
