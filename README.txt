COLLECTOR'S README
__________________

authors: TlsLizard

Welcome to Collector, a minimalist manager for your objects and collections!

The idea of this project is to learn Python programming, Qt, sqlite and Git. 
Don't hesitate to submit your code with additional features you might find useful, or discuss the program via github!

Development environment: 
  command line under linux mint, idle, QtCreator,need PyQt5 package installed

For Users：

  Run ./main_gui.py to launch the program and start managing your collection!
  
 - Current functionalities:
    --- You can add objects to a sqlite database via the user interface
    --- Currently, you can store the following information about an object: Dimensions 
    --- The list of objects and their information can be displayed via a button

For Developers：

 - Philosophy
    The windows are designed with Qt Creator then converted to py files using this command:
    pyuic5 -x file.ui -o file.py
    
 - Rules for modification:
    To keep the code concise and facilitate gui upgrades, 
    files ending in _gui should be modified the least possible 
    and changes clearly commented (with a line of # before and after the addition). 
    This way the ui files can be upgraded with Qt creator more easily. 
    Add the code of new callback functions to files other than files ending in _gui when possible.
 
 - Add a new window:
    Please keep the following format:
    create a ui file: new_window_ui.ui  ->>> convert to py  ->>>> new_window_gui.py
 
 - Create an exe under windows:
    double click on cx_freeze.bat. It should create a folder containing the executable (requires cx_freeze)
 
 - Ideas for future developments:
    --- add a quit button to the application
    --- add a picture (for example, the bill or warranty). implement a blob in sqlite
    --- display the stored picture in a window with a 'print' button
    --- store more information about objects (upgrade the edit_line gui)


