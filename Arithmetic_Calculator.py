import math

print("Welcome to my calculator!")
print("\nYou can do +(add), -(subtract), *(multiply), /(divide), ^ (exponent), % (remainder), sqrt() (square root)")
print("\nuse format : sqrt(number) to calculate squares")
print("\nType 'exit' to stop")

while True:
    problem = input("\nEnter your problem: ")

    if problem == "exit":
        print("\nThank you!")
        break

    try:
         # Handle power
        problem = problem.replace("^", "**")
        # Handle square root
        if "sqrt" in problem:
            problem = problem.replace("sqrt", "math.sqrt")

        result = eval(problem , {"__builtins__" : None , "math" : math})
        print("Result:", result)

    except ZeroDivisionError:
         print("You cannot divide by zero!")
    except:
        print("Oops! Something is wrong with your input. Try again.")
