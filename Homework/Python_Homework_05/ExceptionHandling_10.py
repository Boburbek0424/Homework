def test_list_operation(nums):
    try:
        r = len(nums)  
        print("Length of the list:", r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

nums = [1, 2, 3, 4, 5]
test_list_operation(nums)
