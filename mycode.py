import arcpy
from arcpy import env
env.workspace=r"c:\temp\OTTAWA.gdb\DATA"

fclist= arcpy.ListFeatureClasses()
for fc in fclist:
    print(len(arcpy.ListFields(fc)))