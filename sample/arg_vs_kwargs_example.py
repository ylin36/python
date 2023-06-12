# single # -> tuple, double ## -> dict

# *args
def team(*members):
    print(type(members)) # <class <class 'tuple'>
    for member in members:
        print(member)
        
team("Red", "Blue")

# **kwargs
def team(**details):
    print(type(details))  # <class 'dict>
    
    for key,value in details.items():
        print("{}: {}".format(key,value))
team(Name = "Red", Project = "X", Number = "Three")