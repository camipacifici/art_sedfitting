
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False


# Fits using Prospector - importing only the UV-NIR results

prospector_cat_small = np.genfromtxt('../code_outputs/prospector_output.dat',delimiter=',')

prospector_ids_small = prospector_cat_small[0:,0]

prospector_mass_small = prospector_cat_small[0:,1]
prospector_mass_hi_small = prospector_cat_small[0:,1] + prospector_cat_small[0:,2]
prospector_mass_lo_small = prospector_cat_small[0:,1] - prospector_cat_small[0:,3]

prospector_sfr_small = prospector_cat_small[0:,4]
prospector_sfr_hi_small = prospector_cat_small[0:,5] + prospector_cat_small[0:,4]
prospector_sfr_lo_small = prospector_cat_small[0:,6] - prospector_cat_small[0:,4]

prospector_Av_small = prospector_cat_small[0:,7]
prospector_Av_hi_small = prospector_cat_small[0:,8] + prospector_cat_small[0:,7]
prospector_Av_lo_small = prospector_cat_small[0:,9] - prospector_cat_small[0:,7]

prospector_cat_z1 = np.genfromtxt('../code_outputs/prospector_output_z1.dat',delimiter=',')

prospector_ids_z1 = prospector_cat_z1[0:,0]

prospector_mass_z1 = prospector_cat_z1[0:,1]
prospector_mass_hi_z1 = prospector_cat_z1[0:,1] + prospector_cat_z1[0:,2]
prospector_mass_lo_z1 = prospector_cat_z1[0:,1] - prospector_cat_z1[0:,3]

prospector_sfr_z1 = prospector_cat_z1[0:,4]
prospector_sfr_hi_z1 = prospector_cat_z1[0:,4] + prospector_cat_z1[0:,5]
prospector_sfr_lo_z1 = prospector_cat_z1[0:,4] - prospector_cat_z1[0:,6]

prospector_Av_z1 = prospector_cat_z1[0:,7]
prospector_Av_hi_z1 = prospector_cat_z1[0:,7] + prospector_cat_z1[0:,8]
prospector_Av_lo_z1 = prospector_cat_z1[0:,7] - prospector_cat_z1[0:,9]


prospector_cat_z3 = np.genfromtxt('../code_outputs/prospector_output_z3.dat',delimiter=',')

# objname,logmass,logmass_errup,logmass_errdown,
#logsfr100,logsfr100_errup,logsfr100_errdown,
#logsfr10,logsfr10_errup,logsfr10_errdown,
#mwa,mwa_errup,mwa_errdown,
#av,av_errup,av_errdown

prospector_ids_z3 = prospector_cat_z3[0:,0]

prospector_mass_z3 = prospector_cat_z3[0:,1]
prospector_mass_hi_z3 = prospector_cat_z3[0:,1] + prospector_cat_z3[0:,2]
prospector_mass_lo_z3 = prospector_cat_z3[0:,1] - prospector_cat_z3[0:,3]

prospector_sfr_z3 = prospector_cat_z3[0:,4]
prospector_sfr_hi_z3 = prospector_cat_z3[0:,4] + prospector_cat_z3[0:,5]
prospector_sfr_lo_z3 = prospector_cat_z3[0:,4] - prospector_cat_z3[0:,6]

prospector_Av_z3 = prospector_cat_z3[0:,13]
prospector_Av_hi_z3 = prospector_cat_z3[0:,13] + prospector_cat_z3[0:,14]
prospector_Av_lo_z3 = prospector_cat_z3[0:,13] - prospector_cat_z3[0:,15]


#---------------plot SFR-M* diagrams as a consistency check

if vb == True:
    plt.scatter(prospector_mass_small,prospector_sfr_small,c = prospector_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(prospector_mass_z1,prospector_sfr_z1,c = prospector_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(prospector_mass_z3,prospector_sfr_z3,c = prospector_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

    print(prospector_mass_small, prospector_mass_lo_small)

print('imported Prospector fits.')
