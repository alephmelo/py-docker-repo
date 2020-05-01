"""Entrypoint for {{cookiecutter.app_name}}"""

def greet(person="{{cookiecutter.greeting_recipient}}"):
    print("Hello, %s" % person)
    return True


if __name__ == "__main__":
    greet()
