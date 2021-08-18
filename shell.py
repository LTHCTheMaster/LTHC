import lthc

status = True

while status:
    text = input('lthc > ')
    if text.strip() == '':
        continue

    if text == 'exit': status = False
    else:
        result, error = lthc.run('<stdin>', text)

        if error: print(error.as_string())
        elif result: 
            if len(result.elements) == 1: print(repr(result.elements[0]))
            else: print(repr(result))
