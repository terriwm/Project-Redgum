import escaping as test1

def runtests(fp: str):
    passed = {}
    passed.update(test1.tests(fp))

    if passed != {}:
        print(passed)