#!/usr/bin/python3
def magic_calculation(a, b):
    rst = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rst += a ** b / i
        except:
            rst = b + a
            break
    return rst