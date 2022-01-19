def greet(name,location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet("Xien","South Africa")
# The above is positional arguments

# The below is an example of keyword arguments
greet(location="Kwa-Zulu Natal",name="Xien")