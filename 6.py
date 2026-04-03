# Find longest fragment of equal elements

nums = []
while True:
    n = int(input("Enter number (0 to end): "))
    if n == 0:
        break
    nums.append(n)

max_len = 1
current_len = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 1

max_len = max(max_len, current_len)
print(f"Longest fragment length: {max_len}")