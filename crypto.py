def switch_message(message, nums_cols):
    num_rows = len(message) // nums_cols
    remainder = len(message) % nums_cols
    if remainder != 0:
        num_rows += 1

    switched = [''] * nums_cols
    for col in range(nums_cols):
        pointer = col
        while pointer < len(message):
            switched[col] += message[pointer]
            pointer += nums_cols

    return ''.join(switched)
