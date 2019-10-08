from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

BoxWing.Draw2DAirfoilPolars(fig=1)
BoxWing.Draw3DWingPolars(fig=2)

pyl.show()
