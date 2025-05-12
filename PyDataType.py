# Numeric Types
int_var = 10                 # int: Integer
float_var = 3.14             # float: Floating-point number
complex_var = 2 + 3j         # complex: Complex number
# Sequence Types
str_var = "Hello, Python!"   # str: String
list_var = [1, 2, 3, 4]      # list: Mutable sequence
tuple_var = (5, 6, 7, 8)     # tuple: Immutable sequence
range_var = range(5)         # range: Immutable range of numbers
# Mapping Type
dict_var = {"name": "Alice", "age": 25}  # dict: Key-value pairs
# Set Types
set_var = {1, 2, 3, 4}       # set: Unordered, unique elements
frozenset_var = frozenset([5, 6, 7, 8])  # frozenset: Immutable set
# Boolean Type
bool_var = True              # bool: True or False
# Binary Types
bytes_var = b"hello"         # bytes: Immutable binary data
bytearray_var = bytearray(b"world")  # bytearray: Mutable binary data
memoryview_var = memoryview(bytes_var)  # memoryview: Access binary data without copying
# None Type
none_var = None              # NoneType: Represents "no value"
# Printing all variables with their types
print("int_var:", int_var, "| Type:", type(int_var))
print("float_var:", float_var, "| Type:", type(float_var))
print("complex_var:", complex_var, "| Type:", type(complex_var))
print("str_var:", str_var, "| Type:", type(str_var))
print("list_var:", list_var, "| Type:", type(list_var))
print("tuple_var:", tuple_var, "| Type:", type(tuple_var))
print("range_var:", list(range_var), "| Type:", type(range_var))  # Convert range to list for display
print("dict_var:", dict_var, "| Type:", type(dict_var))
print("set_var:", set_var, "| Type:", type(set_var))
print("frozenset_var:", frozenset_var, "| Type:", type(frozenset_var))
print("bool_var:", bool_var, "| Type:", type(bool_var))
print("bytes_var:", bytes_var, "| Type:", type(bytes_var))
print("bytearray_var:", bytearray_var, "| Type:", type(bytearray_var))
print("memoryview_var:", memoryview_var, "| Type:", type(memoryview_var))
print("none_var:", none_var, "| Type:", type(none_var))


