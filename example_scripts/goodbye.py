def say_goodbye():
    with open('hello.txt', 'a') as f:
        f.write('\ngoodbye')


def say_goodbye_2():
    with open('hello.txt', 'a') as f:
        f.write('\ngoodbye again!!')
