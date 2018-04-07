import sys
import tty


class Keyboard:

    def __init__(self, data_buffer_length=3):
        self.data_buffer_length = data_buffer_length
        self.key_value = None

    def __get_key_value(self):
        # STDIN_FILENO - Standard input, stdin (value 0)
        fd = sys.stdin.fileno()
        # Set cbreak end of line
        tty.setcbreak(fd)
        key_value = sys.stdin.read(self.data_buffer_length)
        return key_value


    def get(self):
        while True:
            key_value = self.__get_key_value()
            if key_value:
                break
        self.key_value = key_value.encode()

    def direction(self):
        direct ={
            b"\x1b[A": "up",
            b"\x1b[B": "down",
            b"\x1b[C": "right",
            b"\x1b[D": "left"
        }
        return direct[self.key_value]


def main():
    keyboard = Keyboard()
    for i in range(4):
        keyboard.get()
        print(keyboard.direction())

if __name__=='__main__':
        main()
