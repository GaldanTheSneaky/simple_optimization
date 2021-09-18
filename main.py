from optimizations import bisection, golden_section


def main():
    expr = "12 * x*x - 2/3 * x*x*x"
    lower_bound = -100
    upper_bound = 16
    print(bisection(lower_bound, upper_bound, expr))


if __name__ == '__main__':
    main()

