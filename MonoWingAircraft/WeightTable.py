import pylab as pyl
from Aircraft import Aircraft

#
# This will generate a weight table of the entire aircraft
# The objects in the table are labeled based on their .name attribute
#
WeightTable = Aircraft.GetWeightTable()

#
# You can turn off sub categories of a part by setting Collapse = True
#
#WeightTable.Fuselage.Collapse = True
#WeightTable.Fuselage.Nose.Collapse = True

#
# You can give a specific order to the parts in the table
#
WeightTable.Wing.Order     = 0
WeightTable.HTail.Order    = 1
WeightTable.VTail.Order    = 2
WeightTable.Fuselage.Order = 3

#
# This is how you change what it is sorted by. Options are
# 'Weight', 'CG' or 'Order' ('Weight' is default)
#
WeightTable.SortBy = 'Order'

#
# This will draw the plot table
#
WeightTable.PlotWeightTable()

#
# This will write the weight table to a tab delimited file 
# with the file name given in the argument
# (default file name WeightTable.txt)
#
WeightTable.WriteWeightTable("TempFiles\WeightTable.txt")

#
# This will display the tree to access parts in the Weight table
# For example, in the table you might see
#
# Main Wing
#    Aileron
#        Servo
#
# PrintParts will display
#
# Wing
#    Aileron
#        Servo
#
# And you can hence change properties through
# WeightTable.Wing.Aileron.Servo
#
WeightTable.PrintParts()
   
pyl.show()
