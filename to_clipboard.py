# -*- coding: cp1250 -*-
import win32clipboard, sys

if len(sys.argv)==2:
	FULL_PATH = sys.argv[1]
	TEXT = '<file://'+FULL_PATH+'>'
elif len(sys.argv)>2:
	TEXT = ""
	for FULL_PATH in sys.argv[1:]:
		TEXT += '<file://'+FULL_PATH+'>\n'
		
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(TEXT, win32clipboard.CF_UNICODETEXT)
win32clipboard.CloseClipboard()

