import sys
from key_validation import validate_key, InvalidKeyExecption
from crypto import encrypt, decrypt

def procces_arg(args):
    if len(args) != 5:
        print("Usage: python main.py -e/-d input_file output_file key")
        sys.exit(1)

    mode = args[1]
    input_file = args[2]
    output_file = args[3]
    try:
        key = int(args[4])
    except ValueError:
        print("Key must be an integer")
        sys.exit(1)
    
    if mode not in ["-e", "-d"]:
        print("Invalid mode")
        sys.exit(1)

    return mode, input_file, output_file, key

def main():
    mode, intput_file, output_file, key = procces_arg(sys.argv)

    #validate the key
    try:
        file_size = validate_key(key, intput_file) #implement this to check the file size vs key
    except InvalidKeyExecption as e:
        print(f"Invalid key: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Input File {intput_file} not found")
        sys.exit(1)
