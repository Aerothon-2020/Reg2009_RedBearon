#
# This file demonstrates how to plot wing loading and bending stress of the main spar.
# Most numbers are fictitious and are for demonstrative purposes only (i.e they are made up).
#
from scalar.units import IN, PSI
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
import pylab as pyl

#
# The velocity which loads will be computed
#
Vmax = Aircraft.Vmax()

global fignum
fignum = 1

def PlotLiftSurfLoad(Surface, GLoad = 1.0):
    #
    # Plots loads and bending stresses on a lifting surface
    #
    # Inputs:
    #    Surface - A lifting surface with a wing weight calculation
    #    SparFc  - Spar chordwise location in fraction of the chord
    #    SparT   - The thickness of the main spae
    #    MaxBendStress - Optional maximum allowed bending stress of the spar
    #    GLoad   - Generic GLoad multiplier
    
    global fignum
    #
    # Plot the loads on the Surface
    #
    Surface.PlotSpanLoading(V = Vmax, LdMult = GLoad, fig = fignum);       fignum += 1
    Surface.PlotNormalizedSpanLoading(Vmax, LdMult = GLoad, fig = fignum); fignum += 1
    
    WingWeight = Surface.GetWeightCalc()
    #
    # Plot the bending stress
    #
    WingWeight.PlotBendingStress(Vmax, fig = fignum); fignum += 1
    
Aircraft.Wing.UpperWing.WingWeight.MainSpar.MaxBendStress = 30e2*PSI
    
PlotLiftSurfLoad(Aircraft.Wing.UpperWing, GLoad = 1.0)
PlotLiftSurfLoad(Aircraft.Wing.LowerWing, GLoad = 1.0)
PlotLiftSurfLoad(Aircraft.HTail, GLoad = 1.0)
PlotLiftSurfLoad(Aircraft.VTail, GLoad = 1.0)

pyl.show()
