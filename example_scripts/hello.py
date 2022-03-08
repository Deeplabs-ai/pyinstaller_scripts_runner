import creopyson

def say_hello():
    try:
        client = creopyson.Client()
        with open('hello.txt', 'w') as f:
            f.write('OK CLIENT')
    except:
        with open('hello.txt', 'w') as f:
            f.write('ERROR')
