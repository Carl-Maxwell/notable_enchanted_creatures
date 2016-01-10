from tdl import Console, TDLError, Window, absolute_import, division, event, flush, forceResolution, force_resolution, getFPS, getFullscreen, get_fps, get_fullscreen, init, int_types, map, noise, print_function, screenshot, setFPS, setFont, setFullscreen, setTitle, set_font, set_fps, set_fullscreen, set_title, style, unicode_literals

# I get the error 'TypeError: Item in ``from list'' not a string'
    # when trying to do 'from tdl import *'
# (some sort of unicode bug with python (or tdl) apparently)
# https://bugs.python.org/issue21720 seemingly
# this file is just a (temporary) workaround.
