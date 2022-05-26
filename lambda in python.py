# lambda in python is used to declare function in a single line
# lambda parameters:expression
var1 = "APPLE"
simplify_numbers = lambda x, y, z: x * y + z
check_case = lambda: True if var1.isupper() else False
print(check_case())
print(simplify_numbers(10, 11, 12))
