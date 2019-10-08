from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

# NOT USEFUL RIGHT NOW

#
# Define a weight range for plotting
#
WeightRange = npy.linspace(25,40,3)*LBF
Aircraft.PlotPayloadvsGrossW(1, WeightRange)

pyl.show()