import arcpy
def get_number_of_fields(inFC):
    return(len(arcpy.ListFields(inFC)))