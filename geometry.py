# Sarah Lerman-Sinkoff Lab 5 part 1

import arcpy
from arcpy import env
env.workspace = 'C:\Users\SLermanSinkoff\Desktop\Lab_5_Working_with_geometries'
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length = length + row[0]
    units = arcpy.Describe(fc).spatialReference.linearUnitName
    print str(length) + " " + units # We convert the data to a string, so that it can be concatenated to the unit type

# final result is in meters:
    ##8780.44037544 Meter
    ##16125.7136095 Meter
    ##24774.0008901 Meter
    ##29352.507797 Meter
    ##38730.3884111 Meter
    ##53506.8074512 Meter
    ##63328.5344719 Meter
    ##66124.9536838 Meter
    ##73455.0011035 Meter
    ##89012.7696841 Meter
    ##96099.5836489 Meter
    ##114900.326795 Meter
    ##126424.20679 Meter
    ##142057.838334 Meter
    ##150849.621748 Meter
    ##162938.679613 Meter
    ##172216.837643 Meter
    ##180849.779726 Meter
    ##207463.283463 Meter
    ##214677.926674 Meter
    ##223839.559732 Meter
    ##236850.215142 Meter
    ##241879.546371 Meter
    ##247168.881032 Meter
    ##249676.08066 Meter
    ##256937.409437 Meter
