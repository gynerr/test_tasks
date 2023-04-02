def byte_digit(digit: int) -> int:
    return ((digit & 0xff) << 8) | ((digit >> 8) & 0xff)
