from models.display import Display

class App:
    def __init__(self):
        self.__url = #CHANGE THIS
        self.__display = Display(self.__url)
        self.run()

    def run(self):
        self.__display.display()


def main():
    app = App()


if __name__ == "__main__":
    main()
