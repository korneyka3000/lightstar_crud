__all__ = ("PasswordManager",)

from bcrypt import checkpw, gensalt, hashpw


class PasswordManager:
    SALT_ROUNDS: int = 12
    SALT_PREFIX: bytes = b"2b"

    @classmethod
    def hash(cls, plain_password: str | bytes) -> str:
        if isinstance(plain_password, str):
            plain_password = plain_password.encode()

        salt = gensalt(rounds=cls.SALT_ROUNDS, prefix=cls.SALT_PREFIX)
        return hashpw(password=plain_password, salt=salt).decode()

    @classmethod
    def check(cls, plain_password: str | bytes, hashed_password: str | bytes) -> bool:
        if isinstance(plain_password, str):
            plain_password = plain_password.encode()

        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode()
        return checkpw(password=plain_password, hashed_password=hashed_password)
