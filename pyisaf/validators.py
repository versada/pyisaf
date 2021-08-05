import typing

from .utils import int_to_digits

_StrValidator = typing.Callable[[str], bool]
_IntValidator = typing.Callable[[int], bool]


def decimal(total_digits: int, fraction_digits: int = 2) -> _StrValidator:
    def validator(v: str) -> bool:
        v = v.lstrip("-")
        if "." in v:
            d, f = v.split(".")
        else:
            d, f = v, ""
        total = len(d) + len(f)
        return total <= total_digits and len(f) <= fraction_digits

    return validator


def max_int_digits(max_digits: int) -> _IntValidator:
    def validator(v: int) -> bool:
        return len(int_to_digits(v)) <= max_digits

    return validator


def max_length(max_len: int) -> _StrValidator:
    def validator(v: str) -> bool:
        return len(v) <= max_len

    return validator


def min_length(min_len: int) -> _StrValidator:
    def validator(v: str) -> bool:
        return len(v) >= min_len

    return validator


def non_negative(v: int) -> bool:
    return v >= 0
