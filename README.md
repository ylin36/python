- [1. Data types](#1-data-types)
  - [1.1 Numbers](#11-numbers)
    - [1.1.1 integer](#111-integer)
    - [1.1.2 float](#112-float)
    - [1.1.3 complex number](#113-complex-number)
  - [1.2 string](#12-string)
    - [1.2.1 quotes](#121-quotes)
    - [1.2.2 len()](#122-len)
    - [1.2.3 index access](#123-index-access)
    - [1.2.4 reverse indexing](#124-reverse-indexing)
    - [1.2.5 string immutability](#125-string-immutability)
    - [1.2.6 string ascii](#126-string-ascii)
    - [1.2.7 string slicing](#127-string-slicing)
    - [1.2.8 slicing wgit fth a step](#128-slicing-wgit-fth-a-step)
    - [1.2.9 reverse slicing](#129-reverse-slicing)
    - [1.2.10 partial slicing](#1210-partial-slicing)
  - [1.3 booleans](#13-booleans)
- [2. Operators](#2-operators)
  - [2.1 Arithmetic](#21-arithmetic)
    - [2.1.1 Addition](#211-addition)
    - [2.1.2 Subtraction](#212-subtraction)
    - [2.1.3 Multiplication](#213-multiplication)
    - [2.1.4 Division](#214-division)
      - [2.1.4.1 Floor Division](#2141-floor-division)
    - [2.1.5 Modulo](#215-modulo)
    - [2.1.6 Precedence](#216-precedence)
    - [2.1.7 Parantheses](#217-parantheses)
  - [2.2 Comparison](#22-comparison)
  - [2.3 Assignment](#23-assignment)
  - [2.4 Logical operators](#24-logical-operators)
  - [2.5 Bitwise operators](#25-bitwise-operators)
  - [2.6 String Operations](#26-string-operations)
    - [2.6.1 String comparison](#261-string-comparison)
    - [2.6.2 String Concatenation](#262-string-concatenation)
    - [2.6.3 String search](#263-string-search)
  - [2.6 Grouping Values](#26-grouping-values)
- [3. If statements](#3-if-statements)
  - [3.1 Variable scoping in if statements](#31-variable-scoping-in-if-statements)
  - [3.2 Conditional expression](#32-conditional-expression)
- [4. Functions](#4-functions)
  - [4.1 Function variable scope](#41-function-variable-scope)
  - [4.2 Built in string functions](#42-built-in-string-functions)
    - [4.2.1 string.find()](#421-stringfind)
    - [4.2.2 string.replace](#422-stringreplace)
    - [4.2.3 string.upper() and string.lower()](#423-stringupper-and-stringlower)
    - [4.2.4 string.join()](#424-stringjoin)
    - [4.2.5 string.format()](#425-stringformat)
  - [4.3 Lambda](#43-lambda)
  - [4.4 Function as argument](#44-function-as-argument)
    - [4.4.1 map(function, list)](#441-mapfunction-list)
    - [4.4.2 filter(function, list)](#442-filterfunction-list)
    - [4.4.3 reduce(function, list)](#443-reducefunction-list)
- [5. Loops](#5-loops)
  - [5.1 for loop](#51-for-loop)
  - [5.2 while loop](#52-while-loop)
- [6. OOP](#6-oop)
  - [6.1 Classes](#61-classes)
    - [6.1.1 Class properties](#611-class-properties)
    - [6.1.2 Class initializer](#612-class-initializer)
    - [6.1.3 Class variable vs Instance variable](#613-class-variable-vs-instance-variable)
  - [6.2 methods](#62-methods)
    - [6.2.1 instance methods](#621-instance-methods)
      - [6.2.1.1 overloading method](#6211-overloading-method)
    - [6.2.2 class method](#622-class-method)
    - [6.2.3 static method](#623-static-method)
  - [6.3 access modifiers](#63-access-modifiers)
    - [6.3.1 private attributes](#631-private-attributes)
      - [6.3.1.1 private property](#6311-private-property)
      - [6.3.1.2 private method](#6312-private-method)
    - [6.3.2 accessing private in main code](#632-accessing-private-in-main-code)
  - [6.4 encapsulation and abstraction](#64-encapsulation-and-abstraction)
    - [6.4.1 properties annotation](#641-properties-annotation)
  - [6.5 inheritance](#65-inheritance)
    - [6.5.1 super() function](#651-super-function)
    - [6.5.2 multiple inheritance](#652-multiple-inheritance)
  - [6.6 polymorphism](#66-polymorphism)
    - [6.6.1 polymorphism using just methods](#661-polymorphism-using-just-methods)
    - [6.6.2 polymorphism using inheritance](#662-polymorphism-using-inheritance)
    - [6.6.3 method overriding and abstract class](#663-method-overriding-and-abstract-class)
    - [6.6.3 abstract class](#663-abstract-class)

# 1. Data types
## 1.1 Numbers
### 1.1.1 integer
```
num = 11
```
### 1.1.2 float
```
111
num  = 1.1
111
```
### 1.1.3 complex number
1+2j
1.5-2.9j
```
complex_num = complex(1, 2)
complex_num2 = complex(1.5, -2.9)
```
## 1.2 string
strings can be single quote or multiple
### 1.2.1 quotes
single quote and double quote are the same. use triple quote to do multiple lines
```
single_quote = 'single quote'

double_quote = "double quote"

empty_string = ""

multiple_lines = '''triple quote will produce
multiple line string'''
```

### 1.2.2 len()
length of the string
```
some_words = "some words"
print(len(some_words))
```

### 1.2.3 index access
test_string = "test string"
first = test_string[0]
print(first)

### 1.2.4 reverse indexing
negative indices start from the opposite end of the string. -1 = last character.
```
test_string = "test string"
print(test_string[10])
print(test_string[-1])
```

### 1.2.5 string immutability
```
string = "Immutable"
string[0] = '0' # ERROR
```

### 1.2.6 string ascii
python 3.x all strings are unicode. older versions of python only support ascii and to make it unicode preceed a string with u

### 1.2.7 string slicing
start = index where to start
end = index where to end (not inclusive)
```
string[start:end]
test_string = "hello world"
print(test_string[0:4]) #hell
print(test_string[1:len(test_string)]) # ello world
```

### 1.2.8 slicing wgit fth a step
```
test_string = "hello world"
print(test_string[0:7]) # " hello "
print(test_string[0:7:2]) # 
"hlo"
```
### 1.2.9 reverse slicing

goes back by one, starting at 8th character and ends at index position 2, but not including 2.
```
test_string = "hello world"
print(test_string[8:2:-1]) # row ol
```

### 1.2.10 partial slicing
```
test_string = "hello world"
print(test_string[:8]) # hello wo
print(test_string[8:]) # rld
print(test_string[:]) # hello world
```
## 1.3 booleans
```
f_bool = False
t_bool = True
```

# 2. Operators
## 2.1 Arithmetic
### 2.1.1 Addition
summing int with float results in float
```
print(20 + 10.5) # 30.5
```
### 2.1.2 Subtraction
```
print (20 - 10.5) # 9.5
```
### 2.1.3 Multiplication

```
print(5.5 * 2) # 11
```

### 2.1.4 Division
Division always results in float

```
print(30/10) # 3.0
```

#### 2.1.4.1 Floor Division

Divison is floored to smallest integer 

```
print(31 // 10) # 3

print(5.5 // 4.5) # 1.0
```

### 2.1.5 Modulo
basically remainder. When negative then think about it like a modulo (clock)

```
print(10 % 2) # remainder is 0
print(28 % 10) # remainder is 8
print(-28 % 10) # think of -28 keep adding 10 until it reaches positive. what is it? 2
# or do remainder, but its positive
print(28 % -10) # think of 28 keep minus 10 until it reaches negative, what is it? -2
# or take the remainder, but its negative
```

### 2.1.6 Precedence

Standard programming precedence
### 2.1.7 Parantheses

Use brackets to gain precedence like standard programming

## 2.2 Comparison
operator|desc
-|-
\>|greater than
<|less than
\>=|greater than or equal
<=|less than or equal
==|equal
!=|not equal
is|equal to identity
is not|not equal to identity

```
num1 = 1
num2 = 2
num3 = 3

list1 = [1,2,3]
list2 = [1,2,3]
print(num2 is num3) # True, same objects because basic type
print(list1 is list2) # False, diff objects
```

## 2.3 Assignment
operator|desc|
-|-
=|assign
+=|add and assign (use this += 1 instead of ++)
-=|subtract and assign
*=|multiply and assign
/=|divide and assign
//=|divide, floor, and assign
**=|power of and assign
%=|mudolo and assign
\|=|OR and assign
&=|AND and assign
^=|XOR and assign
\>>=|right shift and assign
<<=|left shift and assign

## 2.4 Logical operators
operator|desc
and|AND
or|OR
not|NOT (instead of !)

```
print(True or False) # True
print(True and False) # False

# True == 1 and False == 0, but the ids arent the same
print(True == 1) # True
print(True is 1) # False
print(False == 0) # True
print(False is 0) # False
```

## 2.5 Bitwise operators
operator|desc
-|-
&|Bitwise AND
\||Bitwise OR
^|Bitwise XOR
~|Bitwise NOT
<<|Shift Bits Left
\>>|Shift Bits Right

## 2.6 String Operations
### 2.6.1 String comparison
```
print('a' < 'b') # True
print("hello" == "hello") # True

print("ab" < "ba") # True
print("A" < "a") # True
```

### 2.6.2 String Concatenation
```
first = "hello"
second = "world"
print(first + second) # helloworld
print(first * 3) # "hellohellohello
```

### 2.6.3 String search
some_text = "hello world"
print("hello" in some_text) # True

## 2.6 Grouping Values
```
list = [1, 1.5, "two", True]
print(list) # [1, 1.5, 'two', True]
print(list[1]) # 1.5
print(len(list)) # 4
```

# 3. If statements
```
if a and b:
  indentedstatement1
  indentedstatement2
elif c or d:
  indentedstatement3
elif not e
  indentedstatement4
else:
  indentedstatement5
```

## 3.1 Variable scoping in if statements

Be careful about scoping, because there is no explicit variable declaration. Variable initialized inside if block can be used outside if blocks as long as inside block is executed
```
if (True)
  num = 20

print(num) # 20

if (False)
  num = 20
print(num) # NameError: name 'num' is not defined
```

## 3.2 Conditional expression

contrarity to other languages where they use statemnent ? a : b
Python writes it like below
```
num = 1 if True else 2
```

# 4. Functions
2 basic types
* Built in like len(), min(), print()
* User defined

```
def no_param_function():
  print("hello world")
```
```
def param_function(first, second):
  print(first, second) # first second
```
```
def return_first_input(first, second):
  return first

print(return_first_input(1, 2)) # 1
```

no return means None will be returned if used
```
def return_nothing(first, second):
  pass

print(return_nothing(1,2)) # None
```

## 4.1 Function variable scope
variables ARE scoped in functions
mutation of data behave the same as any other programming languages
```
some_string = "hello"

def func():
  some_string = "world"

func()
print(some_string) # hello
```

## 4.2 Built in string functions

### 4.2.1 string.find() 
returns index of found string, -1 if not found
```
some_string = "hello world"
print(some_string.find("el")) # 1
print(some_string.find("earth")) # -1
```

### 4.2.2 string.replace
```
some_string = "hello world"
new_string = some_string.replace("hello", "ola")
```

### 4.2.3 string.upper() and string.lower()
```
print("Hello".lower())
print("hello".upper())
```

### 4.2.4 string.join()

```
list = ["a","b","c"]
print(",".join(list)) # a,b,c
```

### 4.2.5 string.format()
```
some_string = "hello {0}".format("world")
print(some_string) # "hello world"

some_string = "{} {}".format("hello", "world")
print(some_string) # "hello world"

some_string = "{first_string} {second_string}".format(first_string = "hello", second_string="world")
print(some_string) # "hello world"
```


## 4.3 Lambda
Lambdas are anonymous functions that RETURNS data

lambda argument(s) : expression 

```
first_input = lambda first, second : first
print(first_input(1, 2)) # 1
```

```
greet_user = lambda your_name : print('Hey there,', your_name)
greet_user("ylin") # prints Hey there, ylin
```

## 4.4 Function as argument
```
def add(n1, n2):
  return n1 + n2

def calculate(operation, n1, n2):
  return operation(n1, n2)

print(calculate(add, 1, 1)) # 2
```

pass in lambda as the function
```
print(calculate(lambda n1, n2 : n1 + n2, 1, 1)) # 2
```

### 4.4.1 map(function, list)
creates a *map* object using a function to operate on elements of a iterator and a iterator
```
some_list = [1, 1, 1]
some_map = map(lambda n: n + 1, some_list)

# convert back to list so it can be printed
print(list(some_map)) # [2, 2, 2]
```

### 4.4.2 filter(function, list)
create a *filter* object from a iterator where element satisfies condition in the function
```
some_list = [1, 2, 3, 4]
less_than_3 = filter(lambda n: n < 3, some_list)

print(list(less_than_3)) # [1, 2]
```

### 4.4.3 reduce(function, list)
part of functools, but it takes function, and a iterator
```
from functools import reduce

some_list = [1, 2, 3, 4]
sum = reduce(lambda n1, n2: n1 + n2, some_list)
print(sum) # 10
```

# 5. Loops
2 types
* for
* while

loops can contain break, continue, pass (same as continue in this case)
## 5.1 for loop
can be used with range(start, end, step), range(start, end) where end is not included
```
for i in range(0, 10):
  print(i) 

# 1
# 2
# ..
# 9
```

```
some_list = [1, 2, 3, 4]
for i in range(0, len(some_list)):
  print(some_list[i])

# 1
# 2
# 3
# 4
```

## 5.2 while loop
```
i = 0
while i < 50:
  i += 1
print(i) # 50
```

# 6. OOP
## 6.1 Classes
class naming convention is UpperCaseCamel
```
class MyClass:
  pass

obj = MyClass()
```
### 6.1.1 Class properties
* class properties are lower_case_snake
* class properties must be initialized or it will not compile
* you can assign properties after whether they're defined in the class or not, but only that instance will have that property
```
class Foo:
  bar = None

obj = Foo()
Foo.bar = "hello world"
Foo.another_property = "ola world"

print(Foo.bar) # "hello world"
print(Foo.another_property) # "ola world"
```

### 6.1.2 Class initializer
Basically a constructor with a predefined name, and it must take a input called self for intialization.
```
class Foo:
  def __init__(self, bar):
    self.bar = bar

obj = Foo("hello")
print(obj.bar) # hello
```

initializer with operation params
```
class Foo:
  def __init__(self, bar = "hello world"):
    self.bar = bar

obj = Foo()
print(obj.bar) # "hello world"

obj = Foo("ola world")
print(obj.bar) # "ola world"
```

### 6.1.3 Class variable vs Instance variable
* Class variables are shared by all class objects and can be modified using any of them. (kind of like static in C3, but you still access it with the object instance instead of class name). 
* Instance variables are unique
* when class variable is reassigned instead of just mutated, it becomes an instance variable for that object

```
class Foo:
  bar = []

obj1 = Foo()
obj2 = Foo()
obj1.bar.append('hello')
obj2.bar.append('world')

print(obj1.bar) # hello world
print(obj2.bar) # hello world

obj1.bar = []
print(obj1.bar) # []
print(obj2.bar) # hello world
```

## 6.2 methods
3 types
* instance methods
* class methods
* static methods

### 6.2.1 instance methods
all methods should have self as the first argument. it doesn't have to be called self, but it's a good practice to just use self
```
class Foo:
  def __init__(self, some_value):
    self.some_var = some_value

  def print_some_var(self):
    print(self.some_var)

obj = Foo("hello world")
obj.print_some_var() # hello world
```
#### 6.2.1.1 overloading method
Python methods *cannot* be explicitly overloaded like C#. It can only be implicitly overloaded through *optional* arguments
```
class Foo:
  def __init__(self):
    pass

  def print(self, var1, var2 = "world"):
    print("{} {}".format(var1, var2))
  
obj = Foo()
obj.print("hello", "world") # hello world
obj.print("hello") # hello world
```

### 6.2.2 class method
* class methods uses class variables and are accessible using the ClassName instead of the object.
* uses @classmethod decorator
* takes cls instead of self as first parameter.

```
class Foo:
  bar_class_variable = "bar"

  @classmethod
  def print_bar(cls):
    print(cls.bar_class_variable)

Foo.print_bar()
```

### 6.2.3 static method
* pass as many args as needed, and use this method to perform any function without interfering with instance or class variables
* static methods do not know anything about state of the class or the object instance. its' useful for only using its parameters to determine output.
* uses @staticmethod annotation

```
class Foo:

  def __init__(self, some_var):
    self.some_var = some_var

  @staticmethod
  def print_bar():
    print("bar")

obj = Foo('hi')
obj.print_bar() # bar
Foo.print_bar() # bar
```

## 6.3 access modifiers
2 types in python
* private
* public (default)

NOTE python does not have protected modifier

By default its all public, so you can override properties of object.
```
class Foo:
  def __init__(self):
    self.id = 1
  
  def print_id(self):
    print(self.id)

obj = Foo()
obj.print_id() # 1
obj.id = 2
obj.print_id() # 2
```


### 6.3.1 private attributes
* use double underscore prefix to make it private

#### 6.3.1.1 private property
```
class Foo:
  def __init__(self):
    self.__id = 1
  
  def print_id(self):
    print(self.__id)

obj = Foo()
obj.print_id() # 1
obj.__id = 2 # this actually creates a new public instance property
obj.print_id() # 1
print(obj.__id) # 2 Because __id that was assigned is not the same as the private one
# if we didn't assign __id earlier, then the last print would have caused an exception
```

#### 6.3.1.2 private method
```
class Foo:
  def __init__(self, id):
    self.__id = id
  
  def __print_id(self):
    print(self.__id)

  def print_id(self):
    self.__print_id()

obj = Foo(1)
obj.print_id() # 1
obj.__print_id() # AttributeError: 'Foo' object has no attribute '__print_id'
```

### 6.3.2 accessing private in main code
It's not common to have private variable in python. They're obfusticated to ensure no mistakes can be made, however they can still be accessed with workarounds
```
object._ClassName__property
```

```
class Foo:
  def __init__(self, id):
    self.__id = id

obj = Foo(1)
print(obj._Foo__id) # 1
```

## 6.4 encapsulation and abstraction

getters and setters
```
class Foo:
  def __init__(self, id):
    self.__id = id
  
  def get_id(self):
    return self.__id

  def set_id(self, id):
    self.__id = id

obj = Foo(1)
print(obj.get_id()) # 1
obj.set_id(2)
print(obj.get_id()) # 2
```

### 6.4.1 properties annotation
Property annotation can be used 
```
class Foo:
  def __init__(self, id):
    self.__id = id
  
  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, id):
    self.__id = id

  @id.deleter
  def id(self):
    del self.__id

  def print(self):
    print(self.__id)

obj = Foo(1)
print(obj.id) # 1
obj.id = 2
print(obj.id) # 2
obj.print() # 2
```

## 6.5 inheritance
* By default all python class inherit object class.
* To inherit a class, just put the parent ClassName in the child class' declaration in brackets
```
class ParentClass:
  def __init__(self)
    pass

class ChildClass(ParentClass)
  def __init__(self)
    pass
```

practical example
```
class Cat:
  def __init__(self, feet, cry):
    self.feet = feet
    self.cry = cry

  def describe_cat(self):
    print("This cat has {} feet and cry like {}".format(self.feet, self.cry))

class Tiger(Cat):
  def __init__(self, feet, cry, lethality):
    Cat.__init__(self, feet, cry)
    self.lethality = 100
  
  def describe_tiger(self):
    self.describe_cat()
    print("tiger is {}% lethal".format(self.lethality))

tiger = Tiger(4, "roar", 100)
tiger.describe_tiger()

# This cat has 4 feet and cry like roar
# tiger is 100% lethal
```

### 6.5.1 super() function
refer to property of the parent object if the child object override it

```
class Cat:
  def __init__(self, lethality):
    self.lethality = lethality

  def print_lethality(self):
    print(self.lethality)

class Tiger(Cat):
  def __init__(self, lethality):
    Cat.__init__(self, lethality)

  def print_lethality(self):
    print("base lethality is ")
    super().print_lethality()
    print("actual lethality is ")
    print(self.lethality * 100)

tiger = Tiger(1)
tiger.print_lethality()

# base lethality is 
# 1
# actual lethality is 
# 100
```

### 6.5.2 multiple inheritance
python allows for multiple inheritance, as well as diamond

```
class Matter:
  def __init__(self):
    self.particles = 1000

class Human(Matter):
  def __init__(self):
    Matter.__init__(self)
    self.brain = 1

class Machine(Matter):
  def __init__(self):
    Matter.__init__(self)
    self.battery = 1
  
class Android(Human, Machine):
  def __init__(self):
    Human.__init__(self)
    Machine.__init__(self)

  def describe(self):
    print("brain:{}, battery:{}, particles:{}".format(self.brain, self.battery, self.particles))

android1 = Android()
android1.describe() # brain:1, battery:1, particles:1000
```

## 6.6 polymorphism
Can be achieved in 2 ways
* using methods
* using inheritance

### 6.6.1 polymorphism using just methods
python is dynamic, so polymorphism can be achieved just by iterating different things with same method names

```
class Square:
  def __init__(self, length):
    self.length = length

  def print_area(self):
    print(self.length**2)

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def print_area(self):
    print(self.length * self.width)

shapes = [Square(2), Rectangle(2, 4)]

for shape in shapes:
  shape.print_area()

# 4
# 8
```

### 6.6.2 polymorphism using inheritance
this seems kind of redudent since array was going to let you put anything in there anyway and iterate through it like above

```
class Shape:
  def __init__(self):
    pass

  def print_area(self):
    pass

class Square(Shape):
  def __init__(self, length):
    Shape.__init__(self)
    self.length = length
  
  def print_area(self):
    print(self.length ** 2)

class Rectangle(Shape):
  def __init__(self, length, width):
    Shape.__init__(self)
    self.length = length
    self.width = width

  def print_area(self):
    print(self.length * self.width)

shapes = [Square(2), Rectangle(2, 4)]

for shape in shapes:
  shape.print_area()

# 4
# 8
```

### 6.6.3 method overriding and abstract class
this is the *default* behavior if child class declares same method as parent, unless other languages where override keyword must be used

see above example, where base print_area is overridden

### 6.6.3 abstract class
above Shape class can be abstract if init function isn't defined like so
```
class Shape:
  def print_area(self):
    pass

class Square(Shape):
  def __init__(self, length):
    self.length = length
  
  def print_area(self):
    print(self.length ** 2)

class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def print_area(self):
    print(self.length * self.width)

shapes = [Square(2), Rectangle(2, 4)]

for shape in shapes:
  shape.print_area()

# 4
# 8
```
