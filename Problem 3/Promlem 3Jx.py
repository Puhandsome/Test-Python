def find_largest_x(y):
    # Binary search to find the largest x that satisfies the condition
    left, right = 0, y
    while left <= right:
        mid = (left + right) // 2
        if mid * mid + mid <= y:
            left = mid + 1
        else:
            right = mid - 1
    return right