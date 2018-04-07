import sys
import tty
import termios


class Keyboard:

    def __init__(self, data_buffer_length=3):
        self.data_buffer_length = data_buffer_length
        self.key_value = None

    def __get_key_value(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key_value = sys.stdin.read(self.data_buffer_length)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key_value

    def get_key_value(self):
        while True:
            key_value = self.__get_key_value()
            if key_value:
                break
        self.key_value = key_value.encode()
        return self.key_value


def main():
    keyboard = Keyboard()
    for i in range(4):
        print(keyboard.get_key_value())

if __name__=='__main__':
        main()
