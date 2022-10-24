class Person:
    def __init__(self, firstName, surname, dob = None, dod = None, pob = None, pod = None) -> None:
        self.__firstName = firstName
        self.__surname = surname
        self.__dob = dob
        self.__dod = dod
        self.__pob = pob
        self.__pod = pod
    
    @property
    def surname(self):
        return self.__surname

    @property
    def fullname(self):
        if not self.__firstName == None:
            if not self.__surname == None:
                return self.__firstName + ' ' + self.__surname
            else:
                return self.__firstName + ' None'
        else:
            if not self.__surname == None:
                return 'None ' + self.__surname
            else:
                return 'None None'

    @property
    def yob(self):
        if not (self.__dob ==  None):
            return int(self.__dob[:4])
        else:
            return None

    def get_location(self):
        if not self.__pob and not self.__pod:
            return None
        else:
            if not self.__pob:
                return self.__pod
            else:
                return self.__pob
    
    def __str__(self):
        if self.__firstName == None:
            if self.__surname == None:
                return "None None \n"
            else:
                return "None " + self.__surname + '\n'
        elif self.__surname == None:
            return self.__firstName + " None \n"
        else:
            return self.__firstName + ' ' + self.__surname + '\n'