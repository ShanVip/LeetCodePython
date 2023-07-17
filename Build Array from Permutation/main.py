def solution(array):
    answer = [0] * len(array)

    for i in range(len(answer)):
        answer[i] = array[array[i]]

    return answer


if __name__ == '__main__':
    answer = solution([0, 2, 1, 5, 3, 4])
    print(answer)
