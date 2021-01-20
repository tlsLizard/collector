COLLECTOR'S README
__________________

authors: TlsLizard

User Info :
___________

Welcome to Collector, a minimalist manager for your objetcs and collections
Run ./main_gui.py to launch the program and start managing your collection!

Create an exe under windows:
double click on cx_freeze.bat. It should create a folder containing the executable (requires cx_freeze)

Current functionalities:
- You can add objects to an sqlite database via the user interface
- currently, you can store the following information  about an object:  dimensions 
- The list of objetcs and their information can be  displayed via a button


Developers Info :
_________________

tools: QtCreator
need PyQt5 package installed


philosophy: The windows are designed with Qt Creator then converted to py files using this command:
pyuic5 -x file.ui -o file.py
To keep the code concise and facilitate gui upgrades, files ending in _gui should be modified the least possible and changes clearly commented (with a line of # before and after the addition). This way the ui files can be upgraded with Qt creator more easily. Add the code of new calllback functions to files other than files ending in _gui when possible.

if you add a new window, please keep the following format:
create a ui file: new_window.ui  ->>> convert to py >>>> new_window_ui.py

Ideas for future developments:
- att a quit button to the application
- add a picture (for example, the bill or warranty). implement a blob in sqlite
- display the stored picture in a window with a 'print' button
- store more information about objects (upgrade the edit_line gui)


