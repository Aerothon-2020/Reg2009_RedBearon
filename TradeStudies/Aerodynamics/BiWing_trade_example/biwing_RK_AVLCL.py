import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG
from AeroCats.BoxWingAircraft.BiWing import BoxWing as biwing

ExecuteAVL = True
biwing.AVLexe = '../../../Software/avl.exe'

# Set up the variation of Oswald efficiency vs. gap
biwing.GapInterp  = [0.1,0.2,0.3,0.4]
biwing.OeffInterp = [1.1832,1.3371,1.4617,1.5676]

# Determine the correct Biwing correction factor for the given wing
biwing.BWCFInterp      = [0.77,0.78,0.785,0.79]
biwing.LowerWing.FWCF = 1.0
biwing.UpperWing.FWCF = 1.0

# Define the important parameters to vary
biwing.Gap        = 0.1
biwing.Stagger    = 0.0

biwing.EndPlate.Fb      = [0.2,0.5,0.8]
biwing.EndPlate.TR      = [1,1,1]
biwing.EndPlate.Gam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
biwing.EndPlate.Lam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
#biwing.EndPlate.CEdge   = 'LE'


# Find the CL based on the Aerothon and AVL models
Alpha1 = npy.linspace(-5,20,26)*ARCDEG

biwing.Gap  = 0.1 
CLAerothon1 = biwing.CL(Alpha1)

biwing.Gap  = 0.2 
CLAerothon2 = biwing.CL(Alpha1)

biwing.Gap  = 0.3 
CLAerothon3 = biwing.CL(Alpha1)

biwing.Gap  = 0.4 
CLAerothon4 = biwing.CL(Alpha1)

Alpha2 = npy.linspace(0,24,9)

biwing.Stagger = 0.0
biwing.Gap  = 0.1 
CLAVL1      = biwing.GetAVLCL(Alpha2,'g0.1', 'BiWing_trade_example/',ExecuteAVL)
#biwing.Draw(2)

biwing.Gap  = 0.2 
CLAVL2      = biwing.GetAVLCL(Alpha2,'g0.2', 'BiWing_trade_example/',ExecuteAVL)
#biwing.Draw(3)

biwing.Gap  = 0.3 
CLAVL3      = biwing.GetAVLCL(Alpha2,'g0.3', 'BiWing_trade_example/',ExecuteAVL)
#biwing.Draw(4)

biwing.Gap  = 0.4 
CLAVL4      = biwing.GetAVLCL(Alpha2,'g0.4', 'BiWing_trade_example/',ExecuteAVL)
#biwing.Draw(5)

#biwing.Stagger    = 1.0
#biwing.EndPlate.CEdge   = 'LE'
#CLAVL5    = biwing.GetAVLCL(Alpha2,'s1.0', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(6)
#
#biwing.Stagger    = -1.0
#CLAVL6    = biwing.GetAVLCL(Alpha2,'s-1.0', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(7)
#
## Front notch
#biwing.Stagger    = 0.0
#biwing.EndPlate.TR      = [0.6,0.5,2]
#biwing.EndPlate.CEdge   = 'TE'
#CLAVL7    = biwing.GetAVLCL(Alpha2,'FN', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(8)
#
## Back notch
#biwing.EndPlate.CEdge   = 'LE'
#CLAVL8    = biwing.GetAVLCL(Alpha2,'BN', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(9)
#
## Back spike
#biwing.EndPlate.TR      = [1,1,1]
#biwing.EndPlate.Lam     = [40*ARCDEG,30*ARCDEG,-30*ARCDEG]
#biwing.EndPlate.CEdge   = ''
#CLAVL9    = biwing.GetAVLCL(Alpha2,'BS', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(10)
#
## Front Spike
#biwing.EndPlate.Lam     = [-40*ARCDEG,-30*ARCDEG,30*ARCDEG]
#CLAVL10   = biwing.GetAVLCL(Alpha2,'FS', 'BiWing_trade_example/',ExecuteAVL)
##biwing.Draw(11)

UW = biwing.UpperWing
LW = biwing.LowerWing

Alpha1full = biwing.AlphaFus(Alpha1)
Alpha1half = Alpha1 + (UW.DownWash(Alpha1) + LW.DownWash(Alpha1))/2
Alpha1full = Alpha1full / (ARCDEG)
Alpha1half = Alpha1half / (ARCDEG)
Alpha1 = Alpha1 / (ARCDEG)
pyl.figure(1)
#pyl.plot(Alpha1,CLAerothon,'k-')
#pyl.plot(Alpha1half,CLAerothon,'k--')
pyl.plot(Alpha1full,CLAerothon1,'y-')
pyl.plot(Alpha1full,CLAerothon2,'b-')
pyl.plot(Alpha1full,CLAerothon3,'g-')
pyl.plot(Alpha1full,CLAerothon4,'r-')
pyl.plot(Alpha2,CLAVL1,'ys')
pyl.plot(Alpha2,CLAVL2,'bs')
pyl.plot(Alpha2,CLAVL3,'gs')
pyl.plot(Alpha2,CLAVL4,'rs')
#pyl.plot(Alpha2,CLAVL5,'r+')
#pyl.plot(Alpha2,CLAVL6,'rx')
#pyl.plot(Alpha2,CLAVL7,'co')
#pyl.plot(Alpha2,CLAVL8,'mo')
#pyl.plot(Alpha2,CLAVL9,'c>')
#pyl.plot(Alpha2,CLAVL10,'m<')

lb1='AVL: G=0.1, S=0, square'
lb2='AVL: G=0.2, S=0, square'
lb3='AVL: G=0.3, S=0, square'
lb4='AVL: G=0.4, S=0, square'
#lb5='AVL: G=0.4, S=1, square'
#lb6='AVL: G=0.4, S=-1, square'
#lb7='AVL: G=0.4, S=0, front notch'
#lb8='AVL: G=0.4, S=0, back notch'
#lb9='AVL: G=0.4, S=0, back spike'
#lb10='AVL: G=0.4, S=0, front spike'

#pyl.legend(['2DCL (2d alpha)','2DCL (2d alpha+avg downwash)','2DCL (2d alpha+sum downwash)',lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10], loc = 'lower right')
pyl.legend(['Aerothon CL G=0.1','Aerothon CL G=0.2','Aerothon CL G=0.3','Aerothon CL G=0.4',lb1,lb2,lb3,lb4], loc = 'lower right')

pyl.show()

