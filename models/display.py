import time
import webbrowser
import folium
import os
from models.inputProcessor import inputProcessor
from models.getCoordinates import getCoordinates

def get_colour_century(aPerson):
    if (aPerson.yob) == None:
        return "black"
    else:
        if aPerson.yob < 1300:
            return "purple"
        elif aPerson.yob < 1400:
            return "darkblue"
        elif aPerson.yob < 1500:
            return "blue"
        elif aPerson.yob < 1600:
            return "darkgreen"
        elif aPerson.yob < 1700:
            return "green"
        elif aPerson.yob < 1800:
            return "lightgreen"
        elif aPerson.yob < 1900:
            return "orange"
        elif aPerson.yob < 2000:
            return "red"
        else:
            return "darkred"

class Display:
    def __init__(self, url):
        self.__url = url
        self.__personRepository = inputProcessor(self.__url).process()
        self.__getCoordinates = getCoordinates()
        self.__map = folium.Map()

    def display(self):
        print(self.__personRepository.size())
        for i in range(0, (self.__personRepository.size()-1)):
            os.system('clear')
            print(str(i) + " out of " + str(self.__personRepository.size()))
            person = self.__personRepository.get_from_index(i)
            if self.__getCoordinates.get(person.get_location()) == None:
                pass
            else:
                colour = get_colour_century(person)
                folium.Marker(location=self.__getCoordinates.get(person.get_location()), popup=person.fullname, icon=folium.Icon(color = colour)).add_to(self.__map)
            time.sleep(1)
        self.__map.save("map.html")
        webbrowser.open("map.html")
