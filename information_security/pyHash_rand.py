import hashlib
import secrets

salt = secrets.token_bytes(32)
password = input()

key = hashlib.pbkdf2_hmac(
    'sha512', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt.encode('utf-8'), # Provide the salt
    200000  # It is recommended to use at least 100,000 iterations of SHA-256 
)

print(key.hex())