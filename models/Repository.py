class personRepository:
    def __init__(self):
        self.__repository = []

    def add(self, aPerson):
        self.__repository.append(aPerson)

    def get_from_index(self, index):
        return self.__repository[index]
    
    def get_index(self, aPerson):
        if aPerson in self.__repository:
            return self.__repository.index(aPerson)
        else:
            return None
    
    def size(self):
        return len(self.__repository)
    
    def __str__(self):
        ret_str = ""
        for person in self.__repository:
            ret_str += str(person)
        return ret_str