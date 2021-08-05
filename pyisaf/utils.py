import typing


def int_to_digits(number: int) -> typing.List[int]:
    number = abs(number)
    if not isinstance(number, int):
        raise TypeError("Only integers are supported")
    if number == 0:
        return [0]
    digits = []
    while number:
        number, digit = divmod(number, 10)
        digits.append(digit)
    return digits[::-1]
