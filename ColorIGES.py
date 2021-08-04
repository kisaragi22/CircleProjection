# export IGES with colors
# -*- coding: utf-8 -*-
import ImportGui,PySide

#path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserHomePath")
path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/General").GetString("FileOpenSavePath")

SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, u"Export IGES with color", path, "*.igs")

#ImportGui.export(FreeCAD.ActiveDocument.findObjects("App::Part"),SaveName)
#ImportGui.export(FreeCAD.ActiveDocument.Objects,SaveName)
#ImportGui.export(FreeCAD.ActiveDocument.findObjects("Part::Feature"),SaveName)
ImportGui.export(Gui.Selection.getSelection(),SaveName)