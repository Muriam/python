mistakes = {
    'HTTP_404': 404,
    'HTTP_500': 500,
}

response = (500, 'error')
code, content = response

if code == mistakes['HTTP_404']:    # Достаю значение из словаря
    print('Not found')
elif code == mistakes['HTTP_500']:
    print('Server error')
    