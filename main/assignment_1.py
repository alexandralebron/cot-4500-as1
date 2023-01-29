from decimal import Decimal

#1 for converting
float = "010000000111111010111001"

decimal = int(float, 2)
print("{:.5f}".format(decimal))

#2 for chopping
print('%.3f'% decimal)

#3 for rounding
print(round(decimal, 3))

#4 for absolute and relative error
def absolute_error(precise:float, approximate: float):

    sub_operation = precise - approximate

    return abs(sub_operation)

def relative_error(precise:float, approximate: float):

    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise

    return div_operation

if __name__ == "__main__":
    x: float = 4/9
    y: float = 1/3
    z: float = 7/3

    precise_val: float = (x - y) * z

    print(absolute_error(precise_val, .259))

    print(relative_error(precise_val, .259))


#6 for bisection method
def bisection_method(left: float, right: float, given_function: str):
   
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .003
    diff: float = right - left

   
    max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1

        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

    
        print(mid_point)

if __name__ == "__main__":

    
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_string)

#6 for Newton Raphson method
def custom_derivative(value):
    return (3 * value* value) - (2 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1


if __name__ == "__main__":
    # newton_raphson method
    initial_approximation: float = -4
    tolerance: float = .000004
    sequence: str = "x**3 + (4*(x**2)) - 10"

    newton_raphson(initial_approximation, tolerance, sequence)
