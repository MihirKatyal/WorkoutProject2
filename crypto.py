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

def encrypt(input_file_path, output_file_path, key):

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            plaintext = input_file.read()

        ciphertext = switch_message(plaintext, key)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(ciphertext)
    except IOError as e:
        print(f"An error occurred while processing files: {e}")

def decrypt(input_file_path, output_file_path, key):
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            plaintext = input_file.read()

        ciphertext = switch_message(plaintext, key)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(ciphertext)
    except IOError as e:
        print(f"An error occurred while processing files: {e}")