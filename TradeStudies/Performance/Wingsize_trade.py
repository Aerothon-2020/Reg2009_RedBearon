from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

ndiv = 5
rng = npy.arange(ndiv)
Wgap = npy.linspace(0.2,0.4,ndiv)
Wspn = npy.linspace(6.25,7.00,ndiv)*FT
LLO  = npy.linspace(33,35,ndiv)*LBF
Vstl = npy.linspace(30,35,ndiv)*FT/SEC
Vplt = Vstl / (FT/SEC)
attemptcnt = 0

data = npy.zeros((ndiv,ndiv,ndiv,ndiv))*FT

minloc = npy.zeros(4)

#
# This is the proper way to access the wing
#
BoxWing = Aircraft.Wing

pyl.figure(1)
for g in rng:
    print "Gap Iteration #",g+1,", Gap = ",Wgap[g]
    for b in rng:
        print "  Span Iteration #",b+1,", Span = ",Wspn[b]
        for v in rng:
            print "    VStall Iteration #",v+1,", VStall = ",Vstl[v]
            attemptcnt = 0            
            for l in rng:
                print "      Lift Iteration #",l+1,", Lift_LO = ",LLO[l]

                try:
                    Aircraft.Wing.Gap     = Wgap[g]
                    Aircraft.Wing.b       = Wspn[b]
                    Aircraft.Wing.V_Stall = Vstl[v]
                    Aircraft.Wing.Lift_LO = LLO[l]
                    Aircraft.TotalWeight = LLO[l]*.9
                    
                    # Force Refresh...
                    try:
                        Aircraft.Refresh()
                    except:
                        Aircraft.dirty = True
                        Aircraft.Refresh()
                    data[g][b][v][l] = Aircraft.Groundroll()
                except:
                    print "  **  This Configuration not Valid, moving on"
                    attemptcnt += 1
                    continue
                
                if (l == 0):
                    continue
                elif (attemptcnt > 1):
                    print "  **  Exceptions on previous ",attemptcnt," attempts."
                elif (attemptcnt > 3):
                    print "  **  Exceeded LiftLO attempts limit, moving on."
                    break
                elif ((data[g][b][v][l] > data[g][b][v][l-1]) and (data[g][b][v][l] > 250*FT)):
                    print "  **   Ground Roll Increased beyond 250 ft!"
                    break
                elif (data[g][b][v][l] > data[g][b][v][l-1]):
                    print "       Ground Roll Increased from ",data[g][b][v][l-1]," to ",data[g][b][v][l]
                elif (data[g][b][v][l] < data[g][b][v][l-1]):
                    print "       Ground Roll Decreased from ",data[g][b][v][l-1]," to ",data[g][b][v][l]
                    
                
print data
                
                
                
#                grndroll.append(Aircraft.Groundroll() / (FT))
                
#            pyl.plot(Vplt,grndroll)
#            lgnd.append('L_LO = %2.0f (lbf)' % l / (LBF)) 

#pyl.axhline(y = 170, color = 'r')
#pyl.title('Groundroll vs. Stall Velocity')
#pyl.xlabel('Stall Velocity (ft/s)') ; pyl.ylabel('Groundroll (ft)')
#pyl.legend(lgnd, loc = 'best')
#
#pyl.show()