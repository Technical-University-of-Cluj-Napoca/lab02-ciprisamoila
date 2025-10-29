def multiply_all(*args: int) -> int:
    res = 1
    for i in args:
        res *= i
    return res

# if __name__ == "__main__":
#     print(multiply_all(1, 2, 3, 4, 5))
#     print(multiply_all())
#     print(multiply_all(7))