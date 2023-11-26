import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello Worlds")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)