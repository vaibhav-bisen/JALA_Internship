# Local Scope :-
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Global Scope :-
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

enemies = 1   # Global scope


def increase_enemies():
    enemies = 2  # Local scope
    print(f"enemies inside function: {enemies} ")


increase_enemies()
print(f"enemies outside function: {enemies}")
