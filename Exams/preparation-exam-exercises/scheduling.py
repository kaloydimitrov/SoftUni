d = {}
nums =  [int(x) for x in input().split(", ")]
stop_index = int(input())

for i in range(len(nums)):
    d[i] = nums[i]

sort = sorted(d.items(), key=lambda x: x[1])

clock_sum = 0
for key, value in sort:
    if key == stop_index:
        clock_sum += value
        break
    clock_sum += value

print(clock_sum)
