from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

Aircraft.PlotTrimmedPolars(fig=6)
Aircraft.Wing.Draw3DWingPolars(fig=6)
Aircraft.PlotPolarsSlopes(fig=4)
Aircraft.PlotDragBuildup(fig=3)

#pyl.figure(6)
#pyl.subplot(221)
#pyl.legend(['Trimmed Aircraft','Wing'] ,loc = 'best', labelspacing = 0.0)

pyl.figure(6+42)
pyl.legend(['Total A/C Trim','Wing'] , labelspacing = 0.0)

pyl.show()