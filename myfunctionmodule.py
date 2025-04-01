import arcpy
def get_number_of_fields(inFC):
    """Returns number of fields in a feature class or table"""
    return(len(arcpy.ListFields(inFC)))