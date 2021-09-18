import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(lower_bound, upper_bound, function: str, eps=1e-6, precision=1e-4,
              show_animation=False, animation_speed=1) -> float:
    """"Bisection/dichotomy optimization

        Args:
            lower_bound:lower value of interval
            upper_bound:upper value of interval
            function: function to minimize in form of arithmetical expression "x*x+5", variable name 'x' only
            eps: distance from middle of interval to points
            precision: precision, must be greater than eps*5
            show_animation: shows animated plot if True
            animation_speed: rate of animation
    """
    if show_animation:
        x_axis = np.linspace(lower_bound, upper_bound, (upper_bound-lower_bound)*50)
        x = x_axis
        y_axis = eval(function)
        iteration = 1
    while True:
        lower = (lower_bound + upper_bound - eps) / 2
        upper = (lower_bound + upper_bound + eps) / 2
        x = lower
        lower_val = eval(function)
        x = upper
        upper_val = eval(function)

        if show_animation:
            plt.clf()
            plt.title(f"Bisection search. Iteration {iteration}")
            iteration += 1
            plt.plot(x_axis, y_axis)
            plt.plot(lower, lower_val, 'ro')
            plt.plot(upper, upper_val, 'ro')
            plt.axvline(x=lower_bound, linestyle='dashed', color='red')
            plt.axvline(x=upper_bound, linestyle='dashed', color='red')
            plt.pause(1/animation_speed)

        if lower_val <= upper_val:
            upper_bound = upper
        else:
            lower_bound = lower

        if math.fabs(upper_bound - lower_bound) < precision:
            break
    if show_animation:
        plt.show()

    return (lower_bound + upper_bound) / 2


def golden_section(lower_bound, upper_bound, function: str, precision=1e-4,
                   show_animation=False, animation_speed=1) -> float:
    """"Golden section optimization

        Args:
            lower_bound:lower value of interval
            upper_bound:upper value of interval
            function: function to minimize in form of arithmetical expression "x*x+5", variable name 'x' only
            precision: precision
            show_animation: shows animated plot if True
            animation_speed: rate of animation
    """
    if show_animation:
        x_axis = np.linspace(lower_bound, upper_bound, (upper_bound-lower_bound)*50)
        x = x_axis
        y_axis = eval(function)
        iteration = 1

    lower = lower_bound + (3 - math.sqrt(5))/2 * (upper_bound - lower_bound)
    upper = lower_bound + upper_bound - lower

    while True:
        x = lower
        lower_val = eval(function)
        x = upper
        upper_val = eval(function)

        if show_animation:
            plt.clf()
            plt.title(f"Golden section search. Iteration {iteration}")
            iteration += 1
            plt.plot(x_axis, y_axis)
            plt.plot(lower, lower_val, 'ro')
            plt.plot(upper, upper_val, 'ro')
            plt.axvline(x=lower_bound, linestyle='dashed', color='red')
            plt.axvline(x=upper_bound, linestyle='dashed', color='red')
            plt.pause(1/animation_speed)

        if lower_val <= upper_val:
            upper_bound = upper
            upper = lower
            lower = lower_bound + upper_bound - lower
        else:
            lower_bound = lower
            lower = upper
            upper = lower_bound + upper_bound - upper

        if math.fabs(upper_bound - lower_bound) < precision:
            break

    if show_animation:
        plt.show()

    return (lower_bound + upper_bound) / 2
