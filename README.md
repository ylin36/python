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
    - [1.2.8 slicing with a step](#128-slicing-with-a-step)
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
  - [4.3 Lambda](#43-lambda)

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

### 1.2.8 slicing with a step
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

## 4.3 Lambda
Lambdas are anonymous functions that RETURNS data

lambda argument(s) : expression 

```
first_input = lambda first, second : first
print(first_input(1, 2)) # 1
```

```
greet_user = lambda name : print('Hey there,', name)
greet_user("ylin") # prints Hey there, ylin
```