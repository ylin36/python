- [1. data types](#1-data-types)
  - [1.1 numbers](#11-numbers)
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
  - [2.1 Addition](#21-addition)
  - [2.2 Subtraction](#22-subtraction)
  - [2.3 Multiplication](#23-multiplication)
  - [2.4 Division](#24-division)
    - [2.4.1 Floor Division](#241-floor-division)
  - [2.5 Modulo](#25-modulo)
  - [2.6 Precedence](#26-precedence)
  - [2.7 Parantheses](#27-parantheses)

# 1. data types
## 1.1 numbers
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
## 2.1 Addition
summing int with float results in float
```
print(20 + 10.5) # 30.5
```
## 2.2 Subtraction
```
print (20 - 10.5) # 9.5
```
## 2.3 Multiplication

```
print(5.5 * 2) # 11
```

## 2.4 Division
Division always results in float

```
print(30/10) # 3.0
```

### 2.4.1 Floor Division

Divison is floored to smallest integer 

```
print(31 // 10) # 3

print(5.5 // 4.5) # 1.0
```

## 2.5 Modulo
basically remainder. When negative then think about it like a modulo (clock)

```
print(10 % 2) # remainder is 0
print(28 % 10) # remainder is 8
print(-28 % 10) # think of -28 keep adding 10 until it reaches positive. what is it? 2
# or do remainder, but its positive
print(28 % -10) # think of 28 keep minus 10 until it reaches negative, what is it? -2
# or take the remainder, but its negative
```

## 2.6 Precedence

## 2.7 Parantheses
