from gui import *


def main():
    window = Tk()
    window.title('TV Player')
    window.geometry('400x230')
    window.resizable(True, True)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
