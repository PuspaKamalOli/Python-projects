def print_data(data):
    print("Printing data:", data)

def print_data_with_label(data, label):
    print("Printing data with label:", label, "Data:", data)

def print_data_with_color(data, color="black"):
    print("Printing data with color:", color, "Data:", data)

def print_data_with_format(data, *args):
    print("Printing data with format:", args, "Data:", data)

# Function with default arguments
print_data("Hello")  # Output: Printing data: Hello

# Function with additional parameter
print_data_with_label("World", "Label")  # Output: Printing data with label: Label Data: World

# Function with default argument
print_data_with_color("Python")  # Output: Printing data with color: black Data: Python
print_data_with_color("Java", "blue")  # Output: Printing data with color: blue Data: Java

# Function with variable-length argument list
print_data_with_format("Data", 1, 2, 3, 4)  # Output: Printing data with format: (1, 2, 3, 4) Data: Data
