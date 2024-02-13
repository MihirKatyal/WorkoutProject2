import os

class InvalidKeyException(Exception):
    def __init__(self, message="Invailed key encryption"):
        self.message = message
        super().__init__(self.message)

def validate_key(key, input_file_path):
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"File {input_file_path} not found")
    
    file_size = os.path.getsize(input_file_path)

    if not isinstance(key, int):
        raise InvalidKeyException("Key must be an integer")
    
    if key <= 0:
        raise InvalidKeyException("Key must be a positive integer")
    
    if key >= file_size:
        raise InvalidKeyException("Key must be less than the file size")
    
    return file_size
    
        