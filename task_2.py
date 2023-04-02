def baskets(N: int, w: int, d: int, P: int) -> int:
    fake_weight = (((1 + (N - 1)) * (N - 1)) * w) // 2 - P

    if fake_weight // d == 0:
        return N
    else:
        return fake_weight // d
