 - Python Game Toolz -
 - A free set of Python 3 game development tools which, although primitive, (usually) work well.
Copyright (C) 2022  Lincoln V.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Dependancies:
	Python 3, NOT 2
	Pygame 2.0 or later (I don't think 1.9.6 will work, but you *could* try it. Not tested.)
	Python's "socket" library (usually comes pre-installed as part of the Python 3 standard library)
	Python's "time" library (again, usually pre-installed)

Brief overview of library functions:
 - font.py
	A vector based font which looks very 8-bit era. Pretty easy to use, just call "draw_font()"
	Check the file for parameters. I *usually* comment my work decently.
 - menu.py
	A sort-of basic library for building menus MUCH MORE QUICKLY than I could by making
	each one by hand. I might need to comment that one a bit better...it's tricky to understand.
	However, it is functional, and works well enough on practically any screen resolution.
 - netcode.py
	A set of functions to allow the transmission of strings across the network without getting
	your hands dirty with "S.recv()" functions and packet loss issues. Generally works well
	without too much issue.
 - HUD.py
	A library which works similarly to the menu.py library, but for designing HUDs instead of menus.
 - controller.py
	WIP, NONFUNCTIONAL ATM. *Going* to be useful for making a game with configurable controls so that both
	keyboards and controllers are supported.
 - GFX.py
	A library with a Particle() class. The Particle() class is used to create basic 2D graphical effects onscreen.
	The GFX engine is designed to work extremely well with screen scaling, and tile-based games.