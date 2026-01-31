import secrets
import string

def generate_api_key(length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits
    return "ss_" + "".join(secrets.choice(alphabet) for _ in range(length))
