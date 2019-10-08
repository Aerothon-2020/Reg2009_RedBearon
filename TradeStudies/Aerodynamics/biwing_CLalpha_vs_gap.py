import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG, FT, SEC, IN
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing as biwing
from Aerocats2008BiWing import BoxWing as biwingAeroCats2008

RunDir = 'biwing_AVLCL/'

#biwing.V_Stall = 30.0*FT/SEC
chord = biwing.MAC().asUnit(IN)

Execute = False
clrstr = 'bgrycmk'

# Find the CL_alpha vs. gap for AVL
gap   = npy.linspace(0.1, 0.4, 4)
a     = npy.linspace(0,1,2)

print
print 'CLalpha for AVL and Aerothon'

pyl.figure(1)
ind = 0
lgnd = []
for g in gap:
    biwing.Gap = g
    CL      = biwing.GetAVLCL(a,'g'+str(g), RunDir, Execute)
    CLalpha = (CL[-1]-CL[0])

    print 'gap: ',g,'  CLalpha: ',CLalpha

    pyl.axhline(y = CLalpha, color = clrstr[ind])
    ind = ind + 1
    lgnd.append(r'$CL_{\alpha}$ g='+str(g))


# Get CL_alpha for the unaltered wing and the AeroCats 2008 wing
biwing.BWCFInterp = [1,1,1,1]
Alpha1 = npy.linspace(-5,12,69)*ARCDEG
Alpha = (biwing.AlphaWing(Alpha1)) / (ARCDEG) #Fuselage angle of attack

CL = biwing.CL(Alpha1)
#CLAerocats2008 = biwingAeroCats2008.CL(Alpha1)

amin = 0; amax = 12 #Linear region alpha values
num = 0

alpha_half = []
CLa = []             ; CLaSum = 0
CLaAerocats2008 = [] ; CLa2008Sum = 0
for i in range(len(CL)-1):
    alpnum = (Alpha[i+1]-Alpha[i])
    ahalf  = (Alpha[i+1]+Alpha[i])/2
    alpha_half.append(ahalf)
    
    CLa.append((CL[i+1] - CL[i])/(alpnum))
#    CLaAerocats2008.append((CLAerocats2008[i+1]-CLAerocats2008[i])/(alpnum))
    
    #
    # Get the average CLa in the "linear region" of the CL curve  to plot vs. gap
    #
    if ahalf > amin and ahalf < amax:
        num        += 1
        CLaSum     += (CL[i+1] - CL[i])/(alpnum)
#        CLa2008Sum += (CLAerocats2008[i+1]-CLAerocats2008[i])/(alpnum)

CLaAvg     = CLaSum/num
#CLa2008Avg = CLa2008Sum/num

print 'Aerothon 2009 CLalpha from 0deg to 12deg: ', CLaAvg

#pyl.plot(alpha_half,CLa,clrstr[ind])
#pyl.plot(alpha_half,CLaAerocats2008,clrstr[ind+1])
pyl.axhline(y = CLaAvg, color = clrstr[ind], linestyle = '--')
#pyl.axhline(y = CLa2008Avg, color = clrstr[ind+1], linestyle = '--')
pyl.xlabel(r'$\alpha$')
pyl.ylabel(r'$CL_\alpha$')
pyl.title('Lift Curve Slope vs. Angle of Attack')

#lgnd.append(r'Aerothon $CL_{\alpha}$ Uncorrected')
#lgnd.append(r'Aerothon $CL_{\alpha}$ 2008 g=0.2')
lgnd.append(r'Aerothon $CL_{\alpha}$ Avg. Uncorrected')
#lgnd.append(r'Aerothon $CL_{\alpha}$ Avg. 2008 g=0.2')
pyl.legend(lgnd, loc = 'best')

#
# plot cl vs alpha curve
#
alp  = npy.linspace(-3,6,2)*ARCDEG
alpw = (biwing.AlphaWing(alp)) / (ARCDEG)

print 'alpw', alpw
pyl.figure(3)
pyl.plot(Alpha,CL,'b',alpw,biwing.CL(alp),'g')
#pyl.plot(Alpha,CLAerocats2008,'g')
pyl.xlabel(r'$\alpha$'); pyl.ylabel('CL')
pyl.title('Coefficient of Lift vs. Angle of Attack')
pyl.legend(['Aerothon CL','Linear CL'],loc='best')


#
# Get the CLalpha from the Altman et. al. paper model and AVL
#
pyl.figure(2)

# Set BWCF to 1 to get unaltered values
biwing.BWCFInterp = [1,1,1,1]
stgvals = npy.linspace(-1,1,3)
gapvals = npy.linspace(.1,0.4,4)

ind = 0
labels=[]
for s in stgvals:
    CLaAlt = []
    AVLCLa = []
    for g in gapvals:
        biwing.Stagger = s
        biwing.Gap     = g
        
        # AVL CLalpha
        CL      = biwing.GetAVLCL(a,'g'+str(g)+'s'+str(s), RunDir, Execute)
        CLalpha = (CL[-1]-CL[0])
        AVLCLa.append(CLalpha)
        
        # Altman CLalpha
        CLaAlt.append(biwing.CL2(1*ARCDEG)-biwing.CL2(0*ARCDEG))
    
#    pyl.plot(gapvals,CLaAlt,clrstr[ind] + '--')
    pyl.plot(gapvals,AVLCLa,clrstr[ind])
    
    ind = ind + 1
#    labels.append(r'Altman $CL_{\alpha}$ S = '+str(s))
    labels.append(r'AVL $CL_{\alpha}$      S = '+str(s))

#
# Find the BWCF to match the AVL output
#
biwing.BWCFInterp = [0.745,0.845,0.88,0.915]  #chord=12.5IN
#biwing.BWCFInterp = [0.69,0.785,0.835,0.87]  #chord=15.0IN
biwing.Stagger = 0
gapvals = npy.linspace(0.1,0.4,4)
CLa2009 = []
for g in gapvals:
    biwing.Gap = g
    CL = biwing.CL(Alpha1)
    
    CLa = []; CLaSum = 0; num = 0
    for i in range(len(CL)-1):
        alpnum = (Alpha[i+1]-Alpha[i])
        ahalf  = (Alpha[i+1]+Alpha[i])/2
        
        CLa.append((CL[i+1] - CL[i])/(alpnum))
        
        #
        # Get the average CLa in the "linear region" of the CL curve  to plot vs. gap
        #
        if ahalf > amin and ahalf < amax:
            num        += 1
            CLaSum     += (CL[i+1] - CL[i])/(alpnum)
    
    CLa2009.append(CLaSum/num)

pyl.axhline(y = CLaAvg, color = clrstr[ind+1], lw=2)
#pyl.axhline(y = CLa2008Avg, color = clrstr[ind+2])
#pyl.plot(gapvals,CLa2009,clrstr[ind+3])

labels.append(r'Aerothon Linear $CL_{\alpha}$')
#labels.append(r'Aerothon $CL_{\alpha}$ Avg. 2008 g=0.2')
#labels.append(r'Aerothon $CL_{\alpha}$ Predicted 2009')

pyl.axis([0.1,0.4,0,0.1])

pyl.xlabel('Gap/Span')
pyl.ylabel(r'$CL_{\alpha}$')
pyl.title('Lift Curve Slope vs. Gap')
pyl.legend(labels,loc='best',labelspacing = 0.1)

print
print 'Wing Chord', chord

pyl.show()

