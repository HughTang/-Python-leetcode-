from functools import wraps


def singleton(cls):
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class President():
    pass

if __name__ == '__main__':
    p1 = President()
    p2 = President()
    print(p1 is p2)