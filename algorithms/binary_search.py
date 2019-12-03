def binary_search(list_nums, target_num):
    first_index = 0 # initialise first index as 0
    last_index = len(list_nums) - 1 # initialise the last index as the lenght of list minus 1
    found = False # initialise found as false

    # loop through list_nums until the target_num is found or first is > last
    while first_index <= last_index and found == False:

        middle_index = (first_index + last_index) // 2

        if list_nums[middle_index] == target_num:
            found = True

        else:
            # if the value at the middle index is less than the target value reset first_index
            if list_nums[middle_index] < target_num:
                first_index = middle_index + 1
            # else reset the last_index to the middle_index - 1
            else:
                last_index = middle_index - 1

    return found

print(binary_search([1,2,3,5,8,13,21], 5))
print(binary_search([1,2,3,5,8,13,21], 11))
