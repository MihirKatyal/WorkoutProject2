import os

class InvalidKeyException(Exception):
    def __init__(self, message="Invailed key encryption"):
        self.message = message
        super().__init__(self.message)

de
        