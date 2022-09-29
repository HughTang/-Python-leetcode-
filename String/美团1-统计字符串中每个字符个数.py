def func(s:str) -> dict:
    return {c:s.count(c) for c in s}