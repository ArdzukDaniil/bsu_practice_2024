expression = input()

variables = set(char for char in expression if char.isalpha())
variables = sorted(variables)

column_names = " ".join(variables) + " F"
print(column_names)

for values in product([0, 1], repeat=len(variables)):
    globals_dict = {var: value for var, value in zip(variables, values)}

    result = eval(expression, globals_dict)
    print(" ".join(str(value) for value in values) + f" {result}")
