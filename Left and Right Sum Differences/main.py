def solution(nums):
    max_len = len(nums)

    left = [0] * max_len
    right = [0] * max_len

    for i in range(max_len):
        if i != 0:
            left[i] = left[i - 1] + nums[i - 1]

    for i in range(max_len - 1, -1, -1):
        if i != max_len - 1:
            right[i] = right[i + 1] + nums[i + 1]

    result = [0] * max_len
    for i in range(max_len):
        result[i] = abs(right[i] - left[i])

    return result


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5])
    print(result)
