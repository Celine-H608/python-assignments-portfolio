




def apple(x):
    if 0 <= x <= 1:
        approximation = 0
        error_bound = 1
        max_error_allowed = 0.0001
        i = 0

        while error_bound > max_error_allowed:
          approximation += (((-1)**i)*(x**(2*i+1)))/(2*i+1)
          error_bound = (x**(2*i+1))/(2*i+1)
          i += 1

        return approximation,i, error_bound
    else:
        return "error"

x = float(input("Enter a number within or equal to 0 and 1 "))
print(apple(x))






