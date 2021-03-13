def solution(numbers):
    numbers = list(map(str, numbers))
    mlen = max(map(lambda x: len(x), numbers))
    sorted_numbers = sorted(
        numbers, key=lambda x: x * (mlen // len(x)) + x[: mlen % len(x)], reverse=True
    )
    str_numbers = "".join(sorted_numbers)
    return str(int(str_numbers))
