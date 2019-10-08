from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

TW = Aircraft.TotalWeight
EW = Aircraft.EmptyWeight
h  = Aircraft.Wing.Alt_LO

Aircraft.PlotWeightPrediction(1, TotalWeight = 33*LBF, EmptyWeight = 9*LBF, h = h)

pyl.show()
