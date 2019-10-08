Created by Robert Knapke 11/12/08

How to determine the relation between gap and Oswald efficiency?
################################################################################

1. Define the biwing in the "biwing_oswalds_eff" file (imports a general biwing)
     -- the biwing and endplate have been created with general values which can be adjusted
     
2. Run the file.
     -- The output will be efficieny values printed for a gap of 0.1,0.2,0.3,0.4 (or as specified)
    
3. when defining the biwing for other trades, provide the array of Gaps and Oswald Efficiencies
ex.

biwing.GapInterp  = [0.1,0.2,0.3,0.4]
biwing.OeffInterp = [1.1683,1.3212,1.4425,1.5440]