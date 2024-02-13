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
        