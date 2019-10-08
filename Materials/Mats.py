from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, LBF, SLUG, FT
from Aerothon.ACBase import g
from Aerothon.ACMaterial import ACMaterial
from Aerothon.DefaultMaterialsLibrary import Steel, AircraftPly, Basswood, Monokote, Balsa

#
# Materials Set-up
#
Steel    = Steel.copy()
ACPly    = AircraftPly.copy()
Basswood = Basswood.copy()
Monokote = Monokote.copy() 
Balsa    = Balsa.copy()


DivinicelFD = 0.00137 * LBF / IN**3
Fibre2Resin = 3 / 2
EpoxDens = 0.017316 * LBF / IN**3
XylonDens = 0.056 * LBF / IN**3
CompDens = 0.0404 * LBF / IN**3
ZylonCompFD = CompDens
PlyThickness = 1/100 * IN / g
ZylonCompAD = CompDens * PlyThickness


###############################################################################
# Fuselage Materials
###############################################################################

# Bulkhead Truss
# 1/8 inch thick with 75% material cut out
cutout = 0.9
ACTrussBH = ACMaterial()
ACTrussBH.Thickness = 0.25*IN
ACTrussBH.ForceDensity = Balsa.ForceDensity*(1-cutout)

# Composite Plate (Composite Plate + monokote)
# 1/4 inch thick Divinicel Foam with 2 ply of Composite
ACNoseComp = ACMaterial()
ACNoseComp.AreaDensity = DivinicelFD * 0.25*IN/g + 2 * ZylonCompAD 

# Section Truss (truss structure + monokote)
# 1/8 inch thick with 80% material cut out
cutout = 0.8
ACTrussSkin = ACMaterial()
ACTrussSkin.AreaDensity = Balsa.ForceDensity*(1-cutout)*0.25*IN/g + Monokote.AreaDensity

# Bulkhead plywood
# 1/8 inch thick with 75% material cut out
cutout = 0.75
ACPlyBH = ACMaterial()
ACPlyBH.Thickness = 0.125*IN
ACPlyBH.ForceDensity = ACPly.ForceDensity*(1-cutout)

# Section plywood (truss structure + monokote)
# 1/8 inch thick with 80% material cut out
cutout = 0.8
ACPlySkin = ACMaterial()
ACPlySkin.AreaDensity = ACPly.ForceDensity*(1-cutout)*0.125*IN/g + Monokote.AreaDensity

# Stringer material from basswood (w=0.25 in , t=0.25 in)
# NOTE: added balsa to the stringer to approximate length of the balsa truss members
w = 0.25*IN ; t = 0.25*IN
BassStringer = ACMaterial()
BassStringer.LinearForceDensity = (Basswood.ForceDensity + 8*Balsa.ForceDensity) * w * t



###############################################################################
# Wing Materials
###############################################################################

#
# Spar material (balsa, 1/4in width at max airfoil thickness + d-spar skin, balsa 1/16in)
#
sparw = 1*IN
UWthick  = 1.5*IN
LWthick  = 1.5*IN
LsparFD  = Balsa.ForceDensity * sparw * LWthick
UsparFD  = Balsa.ForceDensity * sparw * UWthick
# Dspar density as balsa at 1/16in thick and the distance around the front of the airfoil
#  approximated as 2 times the airfoil thickness at the root
LDsparFD = Balsa.ForceDensity * 0.0625*IN * 2.0*LWthick
UDsparFD = Balsa.ForceDensity * 0.0625*IN * 2.0*UWthick 

#
# Rib material (1/8in balsa) + adjustment for stringers
#
stringers = 0.125*IN   #kind of a fudge factor
BWRibMat = Balsa.copy()
BWRibMat.Thickness = 0.125*IN + stringers
