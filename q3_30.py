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

@HTMLTag("b")       # same as: say_hello = HTMLTag("b")(say_hello)
def say_hello():
    return "Hello Bold World"

@HTMLTag("h1")      # same as: big_title = HTMLTag("h1")(big_title)
def big_title():
    return "I am Important"

print(say_hello())  # <b>Hello Bold World</b>
print(big_title())  # <h1>I am Important</h1>
