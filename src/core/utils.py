import base64
import re
import uuid

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def uuid_to_base32(uuid_code: uuid.UUID) -> str:
    uuid_bytes = uuid_code.bytes
    base32_key = base64.b32encode(uuid_bytes).decode().rstrip("=")
    return base32_key


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    The function compares the plain-text password against the hashed one stored
    in the database and returns a boolean.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    The function takes a plain-text password as a parameter and hashes it with a algorithm,
    salt size, and cost factor before returning the hashed string.
    """
    return pwd_context.hash(password)


def checking_received_username(username: str) -> str:
    """Checking what username is, it can be like username, phone or email.

    Args:
        username (str): The received username.

    Returns:
        str: What field is the received username. E.g.: "phone", "email" or "username".
    """
    number_pattern = "^\\d+$"
    if username[0] == "+" and re.match(number_pattern, username[1:]) is not None:
        return "phone"

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.match(email_pattern, username) is not None:
        return "email"

    return "username"


def get_phone_from_string(string: str) -> str:
    """Get the phone number from the string without extra characters.

    Args:
        string (str): Target string.

    Returns:
        str: Phone number. E.g.: +71112223344
    """
    new_row = re.sub("[^0-9]", "", string)
    return f"+{new_row}"
