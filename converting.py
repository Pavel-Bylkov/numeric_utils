def convert_number(num, base_src=10, base_to=2) -> str:
    """Universal converter system numeric between 2 and 36"""
    alf = [chr(ord("0") + i) for i in range(10)]
    alf += [chr(ord("a") + i) for i in range(26)]
    alf_src = "".join(alf[:base_src])
    alf_out = "".join(alf[:base_to])
    num = str(num).lower().strip().replace(" ", "").replace("_", "")
    minus = num.startswith("-")
    if minus:
        num = num[1:]
    res = ""
    num = num[2:] if num.startswith("0x") else num
    num = num[2:] if num.startswith("0o") else num
    num = num[2:] if num.startswith("0b") else num
    src = list(num)[::-1]
    num = 0
    for i, n in enumerate(src):
        num += alf_src.index(n) * base_src ** i
    if num == 0:
        res = "0"
    while num > 0:
        res = alf_out[num % base_to] + res
        num //= base_to
    if minus:
        res = "-" + res
    return res

if __name__ == '__main__':
    for i in range(10000):
        if convert_number(i, 10, 2) != bin(i)[2:]:
            print(convert_number(i, 10, 2))
            print(bin(i))
        if convert_number(i, 10, 8) != oct(i)[2:]:
            print(convert_number(i, 10, 8))
            print(oct(i))
        if convert_number(i, 10, 16) != hex(i)[2:]:
            print(convert_number(i, 10, 16))
            print(hex(i))
        if convert_number(bin(i), 2, 16) != hex(int(bin(i), 2))[2:]:
            print(convert_number(bin(i), 2, 16))
            print(hex(int(bin(i), 2))[2:])
        if convert_number(oct(i), 8, 10) != str(int(oct(i), 8)):
            print(convert_number(oct(i), 8, 10))
            print(int(oct(i), 8))

    print(convert_number("0xFF", 16, 10))
    print(int("0xFF", 16))
    print(convert_number("-FF", 16, 10))
    print(int("-FF", 16))
    print(convert_number("   - 1_000_345   \n", 10, 16))
