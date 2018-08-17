def reverse(text):
    if text == '':
        return ''
    else:
        arr = list(text)
        arr.reverse()
        return ''.join(arr)