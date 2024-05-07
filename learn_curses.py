import curses
import time


def main(std_screen: curses.window):
    next_line = 0
    first_col = 0

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    red = curses.color_pair(1) | curses.A_BOLD
    green = curses.color_pair(2) | curses.A_BOLD
    blue = curses.color_pair(3) | curses.A_BOLD

    color_cycle = [red, green, blue]

    pad = curses.newpad(100, 100)

    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x, ord('a') + ((x*x+y*y) % 26))

    pad.refresh(0, 0, 5, 5, 20, 20)

    pad.getch()


if __name__ == '__main__':
    curses.wrapper(main)
