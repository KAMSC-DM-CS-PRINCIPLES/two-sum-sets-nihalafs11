def two_sum_pairs(numbers, target):
    pairs = []

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = {numbers[i], numbers[j]}
                pairs.append(pair)

    return pairs

if __name__ == "__main__":
    pass
