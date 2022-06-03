#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    av = sys.argv
    op = av[2]
    if len(av) != 4:
        print("Usage: {} <a> <operator> <b>".format(av[0]))
        sys.exit(1)
    if (op == "+" or op == "-" or op == "*" or op == "/") is False:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(av[1])
    b = int(av[3])
    if op == "+":
        c = add(a, b)
    elif op == "-":
        c = sub(a, b)
    elif op == "*":
        c = mul(a, b)
    elif op == "/":
        c = div(a, b)
    print("{} {} {} = {}".format(a, op, b, c))
