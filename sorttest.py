class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    #def __repr__(self):
    #    return '[{},{},{}]'.format(self.__class__.__name__,
    #                              self.name,
    #                              self.number)

customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)
]


def getKey(custom):
    return custom.number

print sorted(customlist, key=getKey)[0].number,sorted(customlist, key=getKey)[0].name
