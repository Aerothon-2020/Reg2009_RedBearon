import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

# Set up the variation of Oswald efficiency vs. gap
BoxWing.GapInterp  = [0.1,0.2,0.3,0.4]
BoxWing.OeffInterp = [1.1832,1.3371,1.4617,1.5676]

# Determine the correct Biwing correction factor for the given wing
#BoxWing.BWCF           = 1
#BoxWing.BWCF           = 0.685 gap=0.1, stagger=0, square endplate
#BoxWing.BWCF           = 0.74  gap=0.2, stagger=0, square endplate
#BoxWing.BWCF           = 0.765 gap=0.3, stagger=0, square endplate
#BoxWing.BWCF           = 0.78  gap=0.4, stagger=0, square endplate
BoxWing.LowerWing.FWCF = 1 
BoxWing.UpperWing.FWCF = 1

# Define the important parameters to vary
BoxWing.Gap        = 0.1
BoxWing.Stagger    = 0.0

BoxWing.EndPlate.Fb      = [0.2,0.5,0.8]
BoxWing.EndPlate.TR      = [1,1,1]
BoxWing.EndPlate.Gam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
BoxWing.EndPlate.Lam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
#BoxWing.EndPlate.CEdge   = 'LE'


# Find the CL based on the Aerothon and AVL models
Alpha1 = npy.linspace(-5,20,26)*ARCDEG

BoxWing.Gap  = 0.1
#BoxWing.BWCF = 0.685 
CL1         = BoxWing.CL(Alpha1)
CD1         = BoxWing.CD(Alpha1)
BoxWing.Draw(2)

BoxWing.Gap  = 0.2
#BoxWing.BWCF = 0.74 
CL2         = BoxWing.CL(Alpha1)
CD2         = BoxWing.CD(Alpha1)
BoxWing.Draw(3)

BoxWing.Gap  = 0.3
#BoxWing.BWCF = 0.765 
CL3         = BoxWing.CL(Alpha1)
CD3         = BoxWing.CD(Alpha1)
BoxWing.Draw(4)

BoxWing.Gap  = 0.4
#BoxWing.BWCF = 0.78 
CL4         = BoxWing.CL(Alpha1)
CD4         = BoxWing.CD(Alpha1)
BoxWing.Draw(5)

BoxWing.Stagger    = 1.0
BoxWing.OeffInterp = [1.1710,1.3293,1.4566,1.5638]
BoxWing.EndPlate.CEdge   = 'LE'
CL5        = BoxWing.CL(Alpha1)
CD5        = BoxWing.CD(Alpha1)
BoxWing.Draw(6)

BoxWing.Stagger    = -1.0
BoxWing.OeffInterp = [1.1761,1.3320,1.4573,1.5637]
CL6               = BoxWing.CL(Alpha1)
CD6               = BoxWing.CD(Alpha1)
BoxWing.Draw(7)

# Front notch
BoxWing.Stagger    = 0.0
BoxWing.OeffInterp = [1.1831,1.3366,1.4605,1.5650]
BoxWing.EndPlate.TR      = [0.6,0.5,2]
BoxWing.EndPlate.CEdge   = 'TE'
CL7                     = BoxWing.CL(Alpha1)
CD7                     = BoxWing.CD(Alpha1)
BoxWing.Draw(8)

# Back notch
BoxWing.OeffInterp = [1.1813,1.3297,1.4500,1.5519]
BoxWing.EndPlate.CEdge   = 'LE'
CL8                     = BoxWing.CL(Alpha1)
CD8                     = BoxWing.CD(Alpha1)
BoxWing.Draw(9)

# Back spike
BoxWing.OeffInterp = [1.1833,1.33394,1.4676,1.5773]
BoxWing.EndPlate.TR    = [1,1,1]
BoxWing.EndPlate.Lam   = [40*ARCDEG,30*ARCDEG,-30*ARCDEG]
BoxWing.EndPlate.CEdge = ''
CL9                   = BoxWing.CL(Alpha1)
CD9                   = BoxWing.CD(Alpha1)
BoxWing.Draw(10)

# Front Spike
BoxWing.OeffInterp = [1.1826,1.3321,1.4460,1.5398]
BoxWing.EndPlate.Lam = [-40*ARCDEG,-30*ARCDEG,30*ARCDEG]
CL10                = BoxWing.CL(Alpha1)
CD10                = BoxWing.CD(Alpha1)
BoxWing.Draw(11)

Alpha1 = Alpha1 / (ARCDEG)

lb1='G=0.1, S=0, square'
lb2='G=0.2, S=0, square'
lb3='G=0.3, S=0, square'
lb4='G=0.4, S=0, square'
lb5='G=0.4, S=1, square'
lb6='G=0.4, S=-1, square'
lb7='G=0.4, S=0, front notch'
lb8='G=0.4, S=0, back notch'
lb9='G=0.4, S=0, back spike'
lb10='G=0.4, S=0, front spike'

pyl.figure(1)
pyl.subplot(121)
pyl.plot(Alpha1,CL1,'y')
pyl.plot(Alpha1,CL2,'b')
pyl.plot(Alpha1,CL3,'g')
pyl.plot(Alpha1,CL4,'r')
pyl.plot(Alpha1,CL5,'r--')
pyl.plot(Alpha1,CL6,'r:')
pyl.plot(Alpha1,CL7,'c')
pyl.plot(Alpha1,CL8,'m')
pyl.plot(Alpha1,CL9,'c:')
pyl.plot(Alpha1,CL10,'m:')

pyl.legend([lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10], loc = 'best')
pyl.xlabel(r'$\alpha[^o]$')
pyl.ylabel('CL')


pyl.subplot(122)
pyl.plot(Alpha1,CD1,'y')
pyl.plot(Alpha1,CD2,'b')
pyl.plot(Alpha1,CD3,'g')
pyl.plot(Alpha1,CD4,'r')
pyl.plot(Alpha1,CD5,'r--')
pyl.plot(Alpha1,CD6,'r:')
pyl.plot(Alpha1,CD7,'c')
pyl.plot(Alpha1,CD8,'m')
pyl.plot(Alpha1,CD9,'c:')
pyl.plot(Alpha1,CD10,'m:')

pyl.legend([lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10], loc = 'best')
pyl.xlabel(r'$\alpha[^o]$')
pyl.ylabel('CD')

pyl.show()

