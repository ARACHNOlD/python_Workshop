def greet(*name):
    for x in name:
        print(f'hello {x} ')


greet('john', 'sumit')


def greet(name, msg="good morning"):
    print(f"Hello {name} {msg}")


greet("Ram", "goodAfternoon")
