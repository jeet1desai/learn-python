# Function
def print_number(num, msg):
    print(f"{num} {msg}")
print_number(10, "msg")

# Check Local Scope
name="John Deo"
def check_scope(num):
    local_var="Hello"
    print(f"{name} {num} {local_var}")
check_scope(13)

# Return val Function
def return_val(val):
    return val;
val = return_val(20);
print(val)