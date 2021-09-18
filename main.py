from optimizations import bisection, golden_section


def main():
    expr = "12 * x*x - 2/3 * x*x*x"
    lower_bound = -20
    upper_bound = 10
    print(golden_section(lower_bound, upper_bound, expr, show_animation=True, animation_speed=2))


if __name__ == '__main__':
    main()

