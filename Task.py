class Task:
    """Task class. Foundation building block """

    def __init__(self, description, longText):
        self.__desc = description
        self.__longText = longText

    def get_Desc():
        return self.__desc

    def get_longText():
        return selg.__longText

    def get_taskDetails():
        return "%s - %s" % (self.__desc, self.__longText)
