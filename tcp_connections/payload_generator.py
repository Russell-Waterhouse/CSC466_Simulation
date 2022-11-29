def generate_payload(mode: int) -> str:
    if mode == 0:
        payload = "00"  # 0b00000000
    elif mode == 1:
        payload = "FF"  # 0b11111111
    elif mode == 2:
        payload = "55"  # 0b01010101
    else:
        raise ValueError(f"Mode in client.py must be 0, 1, or 2, but instead was {mode}")
    return payload
