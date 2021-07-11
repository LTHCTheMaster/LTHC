import lthc

status = True

while status:
    text = input('lthc > ')
    if text == 'exit':
        status = False
    else:
        result, error = lthc.run(text, '<stdin>', 1)
        if error: print(error.as_string())
        else: print(result)
