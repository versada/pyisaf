import xml.dom.minidom


def pretty_print_xml(s, encoding='utf-8'):
    root = xml.dom.minidom.parseString(s)
    return root.toprettyxml(encoding=encoding)


def int_to_digits(number):
    number = abs(number)
    if not isinstance(number, int):
        raise TypeError('Only integers are supported')
    if number == 0:
        return [0]
    digits = []
    while number:
        number, digit = divmod(number, 10)
        digits.append(digit)
    return digits[::-1]
