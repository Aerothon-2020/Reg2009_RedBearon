from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
from scalar.units import ARCDEG, IN
import pylab as pyl
import numpy as npy

#
# Plot the CM polars
#
Aircraft.PlotCMPolars(1, (-10*ARCDEG, 0*ARCDEG, +10 * ARCDEG), (+0.5 * IN, -0.5 * IN))
Aircraft.PlotCLCMComponents(fig = 2, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
pyl.show()