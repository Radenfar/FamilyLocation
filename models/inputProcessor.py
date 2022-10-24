from models.Person import Person
from models.Repository import personRepository

def file_to_list(filename):
    lines = []
    with open(filename) as file:
        for line in file: 
            line = line.strip()
            lines.append(line)
    return lines


class inputProcessor:
    def __init__(self, filename) -> None:
        self.__rawData = file_to_list(filename)
        self.__personRepository = personRepository()

    def process(self):
        '''
        Info needed:
        Given names -> p
        Surname at birth -> q
        dob -> b
        dod -> d
        pob -> v
        pod -> y
        
        Person code:
        firstName, surname, dob = None, dod = None, pob = None, pod = None
        '''
        for rawLine in self.__rawData:
            if rawLine[0] == 'i':
                splitLine = rawLine.split('\t')
                firstName = None
                surname = None
                dob = None
                dod = None
                pob = None
                pod = None
                for info in splitLine:
                    if info[0] == "p":
                        firstName = info[1:]
                    elif info[0] == "q":
                        surname = info[1:]
                    elif info[0] == "b":
                        dob = info[1:]
                    elif info[0] == "d":
                        dod = info[1:]
                    elif info[0] == "v":
                        pob = info[1:]
                    elif info[0] == "y":
                        pod = info[1:]
                newPerson = Person(firstName, surname, dob, dod, pob, pod)
                self.__personRepository.add(newPerson)
            else:
                pass
        return self.__personRepository

    def __str__(self):
        return str(self.__personRepository)