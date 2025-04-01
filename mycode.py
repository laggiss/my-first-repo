import arcpy
from arcpy import env
import myfunctionmodule
env.workspace=r"c:\temp\OTTAWA.gdb\DATA"

fclist= arcpy.ListFeatureClasses()
#Add a variable to hold a sum
sum_field_lengths=0
for fc in fclist:
    # Add to sum of fields current nmber of fields
    sum_field_lengths+=myfunctionmodule.get_number_of_fields(fc)