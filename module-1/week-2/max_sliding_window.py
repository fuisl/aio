input_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

output_list = [max(input_list[i : i + k]) for i in range(len(input_list) - k + 1)]

print(output_list)
