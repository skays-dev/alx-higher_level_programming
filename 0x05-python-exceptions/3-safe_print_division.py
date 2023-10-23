#!/usr/bin/python3
def safe_print_division(a, b):
    rst = 0
    try:
        rst = a / b
    except ZeroDivisionError:
        rst = None
    finally:
        print('Inside result: {}'.format(rst))
        return rst