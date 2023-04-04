import bcrypt

def password_hash(password: str):
    password = password.encode(encoding="utf-8")
    salt = bcrypt.gensalt(prefix=b"2b")
    return bcrypt.hashpw(password=password, salt=salt)

def password_verify(password: str, hashed: bytes):
    password = password.encode(encoding="utf-8")
    return bcrypt.checkpw(password=password, hashed_password=hashed)