import arcpy
from arcpy import env
env.workspace=r"c:\temp\OTTAWA.gdb\DATA"
arcpy.ListFeatureClasses()