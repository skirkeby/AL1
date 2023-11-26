import curses
import sys

def main(argv):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()

    caughtExceptions = ""

    try:
        stdscr.addstr(0, 0, "Hello, world!")
        screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
        startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
        stdscr.addstr(3, startingXPos, screenDetailText)
        stdscr.addstr(5, curses.COLS - len("Press a key to quit."), "Press a key to quit.")
    except Exception as err:
        caughtExceptions = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
    
    # Turn off cbreak mode...
    curses.nocbreak()

    # Turn echo back on.
    curses.echo()

    # Restore cursor blinking.
    curses.curs_set(True)

    # Turn off the keypad...
    # stdscr.keypad(False)

    # Restore Terminal to original state.
    curses.endwin()

    if "" != caughtExceptions:
        print ("Got error(s) [" + caughtExceptions + "]")

if __name__ == "__main__":
    main(sys.argv[1:])
