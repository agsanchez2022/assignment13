# app/auth/redis.py

async def add_to_blacklist(jti: str, exp: int):
    """No-op blacklist function for assignment/testing."""
    return None

async def is_blacklisted(jti: str) -> bool:
    """Always return False so tokens are treated as valid."""
    return False