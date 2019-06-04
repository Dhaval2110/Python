#decorators


def check(fun):
    def inner(a, b):
        if b == 0:
            print("Invalid operation")
            return
        fun(a, b)
    return inner


@check
def div(a, b):
    print(a/b)


div(4,0)
