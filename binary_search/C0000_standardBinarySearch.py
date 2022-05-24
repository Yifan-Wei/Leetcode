

def binary_search(left, right, num_target, numbers):
    while left <= right:
        mid = (left + right) >> 1
        if numbers[mid] == num_target:
            return True, mid
        if numbers[mid] < num_target:
            left = mid + 1
        else:
            right = mid - 1
    return False, mid
