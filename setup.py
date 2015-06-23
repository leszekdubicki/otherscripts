from distutils.core import setup
import py2exe

#setup(options = {'py2exe': {'bundle_files': 1, 'excludes':['_ssl', 'pyreadline', 'difflib', 'doctest', 'optparse', 'pickle', 'calendar'], 'compressed':True}}, console=['e2s.py'], zipfile = None)
setup(options = {'py2exe': {'bundle_files':1,'excludes':['_ssl', 'pyreadline', 'difflib', 'doctest', 'optparse', 'pickle', 'calendar','locales'], 'compressed':True}}, console=['to_clipboard.py'], zipfile = None)
#setup(options = {'py2exe': {'compressed':True}}, console=['printer.py'], zipfile = None)
