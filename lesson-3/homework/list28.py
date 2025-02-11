main_list = [1, 3, 5, 2, 8, 6, 4]

start_index = 2  # inclusive
end_index = 6    # exclusive

sublist = main_list[start_index:end_index]

min_element = max(sublist)

print(f"The sublist is: {sublist}")
print(f"The minimum element in the sublist is: {min_element}")