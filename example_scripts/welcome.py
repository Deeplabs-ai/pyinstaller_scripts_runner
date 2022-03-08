def say_welcome():
    with open('hello.txt', 'a') as f:
        f.write('\nwelcome')
