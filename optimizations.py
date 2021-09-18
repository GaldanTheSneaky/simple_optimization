import math
import numpy as np
import matplotlib


def bisection(lower_bound, upper_bound, function: str, eps=1e-6, precision=1e-4) -> float:
    """"Bisection/dichotomy optimization

        Args:
            lower_bound:lower value of interval
            upper_bound:upper value of interval
            function: function to minimize in form of arithmetical expression "x*x+5", variable name 'x' only
            eps: distance from middle of interval to points
            precision: precision, must be greater than eps*5
    """
    while True:
        lower = (lower_bound + upper_bound - eps) / 2
        upper = (lower_bound + upper_bound + eps) / 2

        x = lower
        lower_val = eval(function)
        x = upper
        upper_val = eval(function)

        if lower_val <= upper_val:
            upper_bound = upper
        else:
            lower_bound = lower

        if math.fabs(upper_bound - lower_bound) < precision:
            break

    return (lower_bound + upper_bound) / 2


def golden_section(lower_bound, upper_bound, function: str, precision=1e-4) -> float:
    """"Golden section optimization

        Args:
            lower_bound:lower value of interval
            upper_bound:upper value of interval
            function: function to minimize in form of arithmetical expression "x*x+5", variable name 'x' only
            precision: precision
    """
    lower = lower_bound + (3 - math.sqrt(5))/2 * (upper_bound - lower_bound)
    upper = lower_bound + upper_bound - lower

    while True:
        x = lower
        lower_val = eval(function)
        x = upper
        upper_val = eval(function)

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

    return (lower_bound + upper_bound) / 2
