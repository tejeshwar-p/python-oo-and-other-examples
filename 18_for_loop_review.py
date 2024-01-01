def first_example():
    for i in range(1, 10):
        print(i)
        print("Done")


def second_example():
    for i in range(1, 10):
        print(i*i)


def third_example():
    for ch in 'Hello World':
        print(ch)


def fourth_example():
    for word in 'Hello World'.split():
        print(word)


def fifth_example():
    for item in (3, 9, 0, 2, 4, 5, 7, 6):
        print(item)


first_example()
second_example()
third_example()
fourth_example()
fifth_example()
