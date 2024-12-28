from App.Controller import Controller
from Config.Config import STORES,STORES_CLASS,STORES_URI

if __name__ == "__main__":
    while True:
        try:
            main_request = input("Активирувать программу?(да/нет)")
            if main_request == "да":
                main_object = Controller(STORES,STORES_CLASS,STORES_URI)
            else:
                break
        except KeyboardInterrupt:
            break