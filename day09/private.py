def _private_1(name):
    return 'Hello, %s' % name

def __private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return __private_2(name)
print greeting("wzy")
