#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
 
"""
Pas d'accent dans le setup.py, ni dans la description, ni dans les commentaires
 
Icone sous Windows: il faut:
=> un xxx.ico pour integration dans le exe, avec "icon=xxx.ico"
=> un xxx.png pour integration avec PyQt4 + demander la copie avec includefiles.  
"""
 
import sys, os
from cx_Freeze import setup, Executable
 
#############################################################################
# preparation des options 
 
# chemins de recherche des modules
path = sys.path
 
# options d'inclusion/exclusion des modules
includes = []
excludes = []
packages = []
 
# copier les fichiers et/ou repertoires et leur contenu:
includefiles = [] # recopier l'icone.png de la fenetre ici
 
if sys.platform == "linux2":
    includefiles += [(r"/usr/lib/qt5/plugins","plugins")]
    includefiles += [(r"/usr/share/qt5/translations","translations")]
elif sys.platform == "win32":
    includefiles += [(r"E:\Python34\Lib\site-packages\PyQt5\plugins","plugins")]
    includefiles += [(r"E:\Python34\Lib\site-packages\PyQt5\translations","translations")]
else:
    pass
 
binpathincludes = []
if sys.platform == "linux2":
    # Linux: pour que les bibliotheques de /usr/lib soient copiees aussi
    binpathincludes += ["/usr/lib"]
 
# construction du dictionnaire des options
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": includefiles,
           "bin_path_includes": binpathincludes,
           "create_shared_zip": False,
           "include_in_shared_zip": False,
           "compressed": False
           }
 
# pour inclure sous Windows les dll system necessaires
if sys.platform == "win32":
    options["include_msvcr"] = True
 
#############################################################################
# preparation des cibles
base = None
if sys.platform == "win32":
    # plateforme Windows
    base = "Win32GUI" # pour les programmes graphiques
    #base = "Console" # pour les programmes en console
 
icone = None
if sys.platform == "win32":
    icone = None # mettre ici l'icone.ico pour integration dans l'exe
 
cible_1 = Executable(
    script = "programme1.pyw",
    base = base,
    compress = False,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = False,
    icon = icone
    )
 
cible_2 = Executable(
    script = "programme2.pyw",
    base = base,
    compress = False,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = False,
    icon = icone
    )
#############################################################################
# creation du setup
setup(
    name = "Programme",
    version = "1.00",
    description = "essai",
    author = "Tyrtamos",
    options = {"build_exe": options},
    executables = [cible_1, cible_2]
    )
