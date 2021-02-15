# COLLECTOR'S README
##### *authors: TlsLizard, Yishan*
***
## **:loudspeaker: User Info :**
  
Welcome to Collector :blush:  a minimalist manager for your objetcs and collections.  
* **Run**  `./main_script.py`  to launch the program and start managing your collection! :punch:

* **Create an exe under windows**:
double click on `cx_freeze.bat`. It should create a folder containing the executable (requires cx_freeze)

#### Current functionalities:
  - You can add objects to an ***sqlite database*** via the user interface : ```Add an object```
  - Currently, you can store the following information  about an object:  ***dimensions*** , ***value*** , ***image***
  - The list of objects and their information can be displayed via a button : ```Read the object database```

## **:ledger:Developers Info :**

* **Tools:**  ***QtCreator***
_need PyQt5 package installed_

* **Philosophy:** The windows are designed with ***Qt Creator*** then converted to py files using this command: `pyuic5 -x file.ui -o file.py`

* **Rules of modification:** To keep the code concise and facilitate gui upgrades, files ending in `_ui` should be **modified the least possible and changes clearly commented** (with a line of **#** before and after the addition). 
>This way the ui files can be upgraded with Qt creator more easily. Add the code of new callback functions to files other than files ending in `_ui` when possible.

* **Add a new window:** please keep the following format:  
***create a ui file:*** `new_window.ui`  ***>>> convert to py >>>>*** `new_window_ui.py`

* **Ideas for future developments:**
  * Display the stored picture in a window with a 'print' button
  * Store more information about objects (upgrade the `edit_line_ui.py`)
  * Browse [Collector's continuous improvement plan](https://docs.google.com/spreadsheets/d/1C8u6lvReYK2EKYNKb6sXuTvEO1Q9m0ytoQSeTaUkn2k/edit?usp=sharing) for more ideas on how to contribute



Python school by DianGarden  
  ![DianGarden](/Diangarden.png)
