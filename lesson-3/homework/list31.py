original_list = [1, 2, 3]
repeat_count = 3

repeated_list = [element for element in original_list for _ in range(repeat_count)]

print(repeated_list)