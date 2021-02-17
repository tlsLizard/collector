# COLLECTOR'S README
##### *authors: TlsLizard, Yishan*
***
## **:loudspeaker: User Info :**
  
Welcome to Collector :blush:  a minimalist manager for your collection.  
* **Run**  `./main_script.py`  to launch the program and start managing your collection! :punch:

* **Create an exe under windows**:
double click on `cx_freeze.bat`. It will create a folder containing the executable (requires cx_freeze)

#### Current functionalities:
  - You can add objects to the ***DataBase (DB)*** via the button : ```Add an object```
  - You can store the following information  about an object:  ***dimensions*** , ***value*** , ***currency*** , ***image***
  - The list of objects and their information can be displayed via the button : ```Read the object database```

## **:ledger:Developers Info :**

* **Tools:**  ***QtCreator***
_need PyQt5 package installed_

* **General philosophy:** The windows are designed with ***Qt Creator*** then converted to .py files using this command: `pyuic5 -x file.ui -o file.py`

* **Rules of modification:** To keep the code clear and facilitate UI upgrades, files ending in `_ui.py` (UI files) should be **modified as little as possible and changes clearly commented** (with a line of **#** before and after the addition). 
>This way the UI files can be upgraded with Qt creator more easily. The code of new callback functions should be added to files other than UI files whenever it is possible.
***create a UI file:*** `new_window.ui`  ***>>> convert to py >>>>*** `new_window_ui.py`

* **Ideas for future developments:**
  * Display the picture associated with the DataBase entry in a window with a 'print' button
  * Store more information about objects (upgrade the `edit_line_ui.py`): let's discuss your ideas!
  * Browse [Collector's continuous improvement plan](https://docs.google.com/spreadsheets/d/1C8u6lvReYK2EKYNKb6sXuTvEO1Q9m0ytoQSeTaUkn2k/edit?usp=sharing) for ideas on how to contribute. Request edit rights to this document to contribute even further : [tlsLizard](mailto:python.school@diangarden.com)!



Python school by DianGarden  
  ![DianGarden](/Diangarden.png)
