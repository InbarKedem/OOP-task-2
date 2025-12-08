class HTMLTag:
    def __init__(self, tag):
        self.tag = tag
        self.func = None

    def __call__(self, func=None):
        if func is not None:
            self.func = func
            return self
        else:
            result = self.func()
            return f"<{self.tag}>{result}</{self.tag}>"


@HTMLTag("b")
def say_hello():
    return "Hello Bold World"


@HTMLTag("h1")
def big_title():
    return "I am Important"


print(say_hello())
print(big_title())
