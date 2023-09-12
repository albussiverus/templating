def partition(nums, low, high):
    pivot = nums[(high + low) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]




def qsort(nums):
    def _qsort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _qsort(items, low, split_index)
            _qsort(items, split_index + 1, high)

    return _qsort(nums, 0, len(nums)-1)



if __name__ == "__main__":
    import random
    numbers = [random.randint(2, 100) \
         for _ in range(1, random.randint(2, 100))
    ]
    print( f"Generated list with length {len(numbers) }")

    print(f"random numbers:\n{numbers}")
    qsort(numbers)
    print(f"sorted numbers:\n{numbers}")

