# au prealable mettre a jour PIP : python3 -m pip install pip --upgrade
# puis installer curses avec la whl telechargee curses-2.2.1+utf8-cp38-cp38-win_amd64 (https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses)
# je ne sais pas à quoi sert windows-curses peut être une histoire de redimmensionnement de terminal

import curses
import time

# demarre curses
stdscr = curses.initscr()


w1 = stdscr.subwin(20,60,0,0)
w1.box()
w1.refresh()

w2 = stdscr.subwin(20,40,0,60)
w2.box()
w2.refresh()

for i in range(5):
    w1.addstr(1,1,"Entrez quelque chose :")
    entree = w1.getstr(i+2,1).decode(encoding="utf-8")
    w1.box() # sinon la bordure se troue chaque fois qu'on fait ENTER
    w1.refresh()
    w2.addstr(i+2,1,entree)
    w2.refresh()

w2.addstr(8,1,"c'est fini !")
w2.refresh()
time.sleep(3)

""" 
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
win.box()
win.addstr(4,4,"Salut")

"""
