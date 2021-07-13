import lthc

status = True

while status:
    text = input('lthc > ')

    if text == 'exit': status = False
    else:
        result, error = lthc.run('<stdin>', text)

        if error: print(error.as_string())
        elif result: print(result)
