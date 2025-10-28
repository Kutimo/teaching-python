nums: list[int] = [1, 2, 3, 4]

evens: list[int] = list(filter(lambda x: x % 2 == 0, nums))

print(nums)

print(evens)
