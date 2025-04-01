import arcpy
from arcpy import env
import myfunctionmodule
env.workspace=r"c:\temp\OTTAWA.gdb\DATA"

fclist= arcpy.ListFeatureClasses()
for fc in fclist:
    print(myfunctionmodule.get_number_of_fields(fc))