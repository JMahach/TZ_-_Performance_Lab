import sys

if __name__ == "__main__":
    nums_path = sys.argv[1]

    with open(nums_path, "r") as file:
        nums = [int(line.strip()) for line in file]

    median = nums[len(nums) // 2]
    print(sum(abs(num - median) for num in nums))
