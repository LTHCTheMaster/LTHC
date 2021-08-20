<div align="center">

# Tutorial

Welcome on the tutorial, here you can learn the basics of LTHC

<div align="left">

## The shell

Before running a program, you have to run the shell (shell.py)

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

## Playing with 'VAR'

With the ``VAR`` keyword, you can create and modify variables, there are 3 direct variables types and 2 more special types

Use: ``VAR the_name_of_the_variable = <expression>``

You can create a 'NUM' type variable with a number

You can create a 'STRING' type variable with a string, a string is created by surrounding a text with ``"`` , the escape charater is ``\``

You can create a 'LIST' type variable with value ('LIST' are separed as more simple values in other 'LIST') between square brackets (``[]``)

You can assign to an other variable a 'FUNCTION' (created with ``FUNC``) or a 'BUILT-IN_FUNCTION'

<div align="center">
<img src="./images/list_clue.png">

Example of list simplifying

<div align="left">

## String manipulation

You can concatenate two strings with the ``+`` operator

You can replicate a string multiple times with the ``*`` operator and a number (or a 'NUM')

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

<div align="center">
<img src="./images/examples_list.png">

Examples of list manipulation

<div align="left">

## Info

In the shell you can simulate multiple lines with ``;``

## Conditions

one line syntax: ``IF <condition> THEN <expression> ?(ELIF <condition> THEN <expression>) ?(ELSE <expression>)``

multiple lines syntax: ``IF <condition> THEN {new_line} <expressions> {new_line} END|?(ELIF <condition> THEN {new_line} <expressions> {new_line} END|(ELSE {new_line} <expressions> {new_line} END))|?(ELSE {new_line} <expressions> {new_line} END)``

<div align="center">
<img src="./images/if_elif_else.png">

Examples of simple conditions

<div align="left">

### Logic and comparison operator

#### Logic

``a AND b`` ; ``a OR b`` ; ``NOT a``

#### Comparison

``a == b`` ; ``a != b`` ; ``a =! b`` ; ``a > b`` ; ``a < b`` ; ``a >= b`` ; ``a => b`` ; ``a <= b`` ; ``a =< b``

## Loops

### For Loop

one line default syntax: ``FOR var_name = start_value TO end_value THEN <expression>``

multiple lines default syntax: ``FOR var_name = start_value TO end_value THEN {new_line} <expressions> {new_line} END``

one line with ``STEP`` syntax: ``FOR var_name = start_value TO end_value STEP step_value THEN <expression>``

multiple lines with ``STEP`` syntax: ``FOR var_name = start_value TO end_value STEP step_value THEN {new_line} <expressions> {new_line} END``

### While Loop

one line syntax: ``WHILE <condition> THEN <expression>``

multiple lines syntax: ``WHILE <condition> THEN {new_line} <expressions> {new_line} END``

### Break and Continue

``BREAK`` Stop the current loop

``CONTINUE`` Jump to the next iteration of the current loop

## Functions

one line default syntax: ``FUNC func_name(?(<args>)) -> <expression>``

multiple line syntax: ``FUNC func_name(?(<args>)) {new_line} <expressions> {new_line} END``

one line by assignement syntax: ``VAR a_var_name = FUNC (?(<args>)) -> <expression>``

``VAR`` assignement syntax: ``VAR a_var_name = a_defined_function_name``

calling function: ``a_defined_or_assigned_function_name(<the_required_args>)``

### Return

you can add a ``RETURN <something_to_return>`` to your function for customize the returned value

## Builtins

### Functions

``PRINT(val)`` ; ``PRINT_RET(val)`` (output)

``INPUT(msg)`` ; ``INPUT_NUM(msg)`` (input)

``CLEAR()`` (clear the screen)

``IS_NUM(var)`` ; ``IS_STR(var)`` ; ``IS_LIST(var)`` ; ``IS_FUNC(var)`` (type checking function)

``POP(list, index)`` ; ``APPEND(list, val)`` ; ``EXTEND(list1, list2)`` (list manipulation function)

``LEN(val)`` (len of 'val')

``STR(val)`` (cast to 'STRING' type)

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

``FUNC oopify(prefix) -> prefix + "oop"``

-> We want to cast prefix to 'STRING' type so we replace ``prefix`` by ``STR(prefix)`` and we obtain:

``FUNC oopify(prefix) -> STR(prefix) + "oop"``

<br>

Now we have to upgrade the map function:

```
FUNC map(elements, function)
    VAR new_elements = []
    VAR len = LEN(elements)

    FOR i = 0 TO len THEN
        APPEND(new_elements, function(elements/i))
    END
    
    RETURN new_elements
END
```

First point, if elements is a 'LIST' type variable, assign the len variable to the len of elements else return a list with one single string which represent a space (so ``[" "]`` ),

second point, if function is a 'FUNCTION' type variable, assign the len2 variable to the len of function else return a list with one single string which represent a space (so ``[" "]`` ),

third point, if len2 is not equals to 1 return a list with one single string which represent a space (so ``[" "]`` )

Now we have this function:

```
FUNC map(elements, function)
    VAR new_elements = []
    IF IS_LIST(elements) THEN VAR len = LEN(elements) ELSE RETURN [" "]

    IF IS_FUNC(function) THEN VAR len2 = LEN(function) ELSE RETURN [" "]

    IF len2 != 1 THEN RETURN [" "]

    FOR i = 0 TO len THEN
        APPEND(new_elements, function(elements/i))
    END
    
    RETURN new_elements
END
```

<br>

The last function to upgrade is the join function:

```
FUNC join(elements, separator)
    VAR result = ""
    VAR len = LEN(elements)

    FOR i = 0 TO len THEN
        VAR result = result + elements/i
        IF i != len - 1 THEN VAR result = result + separator
    END

    RETURN result
END
```

To check the if elements is a list we have to add between the firt result var assignement and the loop: ``IF IS_LIST(elements) THEN VAR len = LEN(elements) ELSE RETURN " "`` , with this line you check the type of elements if it isn't a list you return a space

Replace the content of the loop by:

```
VAR result = result + STR(elements/i)
IF i != len - 1 THEN VAR result = result + STR(separator)
```

In this line we only add a ``STR`` casting

So now we have this function:

```
FUNC join(elements, separator)
    VAR result = ""
    
    IF IS_LIST(elements) THEN VAR len = LEN(elements) ELSE RETURN " "

    FOR i = 0 TO len THEN
        VAR result = result + STR(elements/i)
        IF i != len - 1 THEN VAR result = result + STR(separator)
    END

    RETURN result
END
```

<a href="./tutorial_work/upgraded_example.lthc">link</a> to the upgraded file
