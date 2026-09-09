from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash


# =========================
# JWT SETTINGS
# =========================

SECRET_KEY = "my-super-secret-key-change-this"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =========================
# PASSWORD HASHING
# =========================

password_hash = PasswordHash.recommended()


def hash_password(password: str):
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_hash.verify(
        password,
        hashed_password
    )


# =========================
# CREATE JWT
# =========================

def create_access_token(username: str):

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload, 
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# =========================
# DECODE JWT
# =========================

def decode_access_token(token: str):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload