class Monarch:
    def __init__(self, name, previous):
        self.name = name
        self.previous = previous
        self.wife = None
        self.sons = []
        self.daughters = []
        self.hasSons = False
        self.hasDaughters = False
        self.hasChildren = False

    def add_son(self, son):
        self.sons.append(son)
        self.hasSons = True

    def eldest_son(self):
        pass

    def eldest_daughter(self):
        pass


def male_primogeniture(monarch: Monarch):
    # if monarch.hasChildren is False:
    #     return male_primogeniture(monarch.previous)
    #
    # else:
    #     if monarch.hasSons is True:
    #         return monarch.eldest_son()
    #     elif monarch.hasDaughters is True:
    #         return monarch.eldest_daughter()
    #     else:
    #         return None

    if monarch.hasChildren:
        if monarch.hasSons:
            return monarch.eldest_son()
        return monarch.eldest_daughter()

    return male_primogeniture(monarch.previous)

