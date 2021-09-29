<div align="center">

# Tutorial

Welcome on the tutorial, here you can learn the basics of LTHC

<div align="left">

## The shell

Before running a program, you have to run the shell (lthc.py)

<div align="center">
<img src="./images/shell_default.png">

The shell after starting

<div align="left">

Here you can use the language instructions, and this shell have an exclusive function (only shell): ``exit`` , this command stop the shell

## Doing some maths

addition:       ``1 + 3``

substraction:   ``2.9 - 17``

multiplication: ``-17 * 19.5783``

division:       ``-3 / -4.2``


arithmetical negation:             ``-5``

quotient of an euclidean division: ``17.3 // 2.2``

modulo:                            ``15 % 7``

power operator:                    ``2 ^ 4``

## Playing with 'var'

With the ``var`` keyword, you can create and modify variables, there are 3 direct variables types and 2 more special types

Use: ``var the_name_of_the_variable = <expression>``

You can create a 'NUM' type variable with a number

You can create a 'STRING' type variable with a string, a string is created by surrounding a text with ``"`` , the escape charater is ``\``

You can create a 'LIST' type variable with value ('LIST' are separed as more simple values in other 'LIST') between square brackets (``[]``)

You can assign to an other variable a 'FUNCTION' (created with ``func``) or a 'BUILT-IN_FUNCTION'

<div align="center">
<img src="./images/list_clue.png">

Example of list simplifying

<div align="left">

## String manipulation

You can concatenate two strings with the ``+`` operator

You can replicate a string multiple times with the ``*`` operator and a number (or a 'NUM')

You can get the element at index b in your string by using: ``your_string / b``

<div align="center">
<img src="./images/examples_repli_str.png">

Example of replication

<div align="left">

## List manipulation

Append and extend: ``listA + listB``

Extend: ``listA % listB``

Get the element at index b in a list: ``listA / b``

Remove (pop) the element at index b in a list: ``listA - b``

Replicate a list multiple times: ``listA * b``

Multiply each value of a list by an other value: ``listA ^ b`` (b is the other value)

You can reverse a list by using: ``not listA``

<div align="center">
<img src="./images/examples_list.png">

Examples of list manipulation

<div align="left">

## Info

In the shell you can simulate multiple lines with ``;``

## Conditions

one line syntax: ``if <condition> then <expression> ?(elif <condition> then <expression>) ?(else <expression>)``

multiple lines syntax: ``if <condition> then {new_line} <expressions> {new_line} end|?(elif <condition> then {new_line} <expressions> {new_line} end|(else {new_line} <expressions> {new_line} end))|?(else {new_line} <expressions> {new_line} end)``

<div align="center">
<img src="./images/if_elif_else.png">

Examples of simple conditions

<div align="left">

### Logic and comparison operator

#### Logic

``a and b`` ; ``a or b`` ; ``not a``

#### Comparison

``a == b`` ; ``a != b`` ; ``a =! b`` ; ``a > b`` ; ``a < b`` ; ``a >= b`` ; ``a => b`` ; ``a <= b`` ; ``a =< b``

## Loops

### For Loop

one line default syntax: ``for var_name = start_value to end_value then <expression>``

multiple lines default syntax: ``for var_name = start_value to end_value then {new_line} <expressions> {new_line} end``

one line with ``step`` syntax: ``for var_name = start_value to end_value step step_value then <expression>``

multiple lines with ``step`` syntax: ``for var_name = start_value to end_value step step_value then {new_line} <expressions> {new_line} end``

### While Loop

one line syntax: ``while <condition> then <expression>``

multiple lines syntax: ``while <condition> then {new_line} <expressions> {new_line} end``

### Break and Continue

``break`` Stop the current loop

``continue`` Jump to the next iteration of the current loop

## Functions

one line default syntax: ``func func_name(?(<args>)) -> <expression>``

multiple line syntax: ``func func_name(?(<args>)) {new_line} <expressions> {new_line} end``

one line by assignement syntax: ``var a_var_name = func (?(<args>)) -> <expression>``

``var`` assignement syntax: ``var a_var_name = a_defined_function_name``

calling function: ``a_defined_or_assigned_function_name(<the_required_args>)``

### Return

you can add a ``return <something_to_return>`` to your function for customize the returned value

## Builtins

### Functions

``print(val)`` ; ``print_ret(val)`` (output)

``input(msg)`` ; ``input_num(msg)`` (input)

``clear()`` (clear the screen)

``is_num(var)`` ; ``is_str(var)`` ; ``is_list(var)`` ; ``is_func(var)`` (type checking function)

``pop(list, index)`` ; ``append(list, val)`` ; ``extend(list1, list2)`` (list manipulation function)

``len(val)`` (len of 'val')

``randint(a, b)`` (random value between a and b both included)

``str(val)`` (cast to 'STRING' type)

``sleep(ts)`` (sleep ts seconds)

``RUN(path)`` (run a .lthc file (LTHC Script))

### Variables

``NULL`` ; ``TRUE`` ; ``FALSE`` ; ``PHI`` ; ``E`` ; ``PI`` ; ``TAU`` ('NUM' type)

``DIGITS`` ('STRING' type)

## Run Usage

To run a file, tou have to type in the shell ``RUN(file_path_between_quotes)``

For example, to run the <a href="./example.lthc">example file</a> you have to type ``RUN("example.lthc")``

<div align="center">

# Guided work

Welcome on the second part of the tutorial, here you can do a guided work

<div align="left">

## Upgrade the example script

You can found the example script <a href="./example.lthc">here</a>

In this work, we have to upgrade the script with more tests in functions to avoid all potential error

<br>

First function to upgrade:

``func oopify(prefix) -> prefix + "oop"``

-> We want to cast prefix to 'STRING' type so we replace ``prefix`` by ``str(prefix)`` and we obtain:

``func oopify(prefix) -> str(prefix) + "oop"``

<br>

Now we have to upgrade the map function:

```
func map(elements, function)
    var new_elements = []
    var len_ = len(elements)

    for i = 0 to len_ then
        append(new_elements, function(elements/i))
    end
    
    return new_elements
end
```

First point, if elements is a 'LIST' type variable, assign the len variable to the len of elements else return a list with one single string which represent a space (so ``[" "]`` ),

second point, if function is a 'FUNCTION' type variable, assign the len2 variable to the len of function else return a list with one single string which represent a space (so ``[" "]`` ),

third point, if len2 is not equals to 1 return a list with one single string which represent a space (so ``[" "]`` )

Now we have this function:

```
func map(elements, function)
    var new_elements = []
    if is_list(elements) then var len_ = len(elements) else return [" "]

    if is_func(function) then var len2 = len(function) else return [" "]

    if len2 != 1 then return [" "]

    for i = 0 to len_ then
        append(new_elements, function(elements/i))
    end
    
    return new_elements
end
```

<br>

The last function to upgrade is the join function:

```
func join(elements, separator)
    var result = ""
    var len_ = len(elements)

    for i = 0 to len_ then
        var result = result + elements/i
        if i != len_ - 1 then var result = result + separator
    end

    return result
end
```

To check the if elements is a list we have to add between the firt result var assignement and the loop: ``if is_list(elements) then var len_ = len(elements) else return " "`` , with this line you check the type of elements if it isn't a list you return a space

Replace the content of the loop by:

```
var result = result + str(elements/i)
if i != len_ - 1 then var result = result + str(separator)
```

In this line we only add a ``str`` casting

So now we have this function:

```
func join(elements, separator)
    var result = ""
    
    if is_list(elements) then var len_ = len(elements) else return " "

    for i = 0 to len_ then
        var result = result + str(elements/i)
        if i != len_ - 1 then var result = result + str(separator)
    end

    return result
end
```

<a href="./tutorial_work/upgraded_example.lthc">link</a> to the upgraded file
