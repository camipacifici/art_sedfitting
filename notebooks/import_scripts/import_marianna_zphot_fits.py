
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False


# This is a full CANDELS/GOODS-S catalog

marianna_cat = np.genfromtxt('../code_outputs/marianna_GOODSS_BC03_zbest.dat')
if vb == True:
    print(marianna_cat.shape)

#header data
#log10(mass)	SFR	age	E(B-V)	U	B	BJ	V	R	I	J	K

# Galaxy IDs
marianna_ids_full = np.arange(marianna_cat.shape[0])

# Stellar Mass
marianna_mass_full = marianna_cat[0:,0]
marianna_mass_lo_full = marianna_cat[0:,0] - 0.1
marianna_mass_hi_full = marianna_cat[0:,0] + 0.1

# Star Formation Rates
marianna_sfr_full = np.log10(marianna_cat[0:,1])
marianna_sfr_lo_full = np.log10(marianna_cat[0:,1]) - 0.1
marianna_sfr_hi_full = np.log10(marianna_cat[0:,1]) + 0.1

# Dust estimate
marianna_Av_full = marianna_cat[0:,3]*4.05


#-------------------partition into small, z1, and z3 catalogs-----------------

marianna_mass_small = marianna_mass_full[cat_small_ids.astype(int)]
marianna_mass_lo_small = marianna_mass_lo_full[cat_small_ids.astype(int)]
marianna_mass_hi_small = marianna_mass_hi_full[cat_small_ids.astype(int)]

marianna_sfr_small = marianna_sfr_full[cat_small_ids.astype(int)]
marianna_sfr_lo_small = marianna_sfr_lo_full[cat_small_ids.astype(int)]
marianna_sfr_hi_small = marianna_sfr_hi_full[cat_small_ids.astype(int)]

marianna_Av_small = marianna_Av_full[cat_small_ids.astype(int)]

#------------------------------------------------------------------

marianna_mass_z1 = marianna_mass_full[cat_z1_ids.astype(int)]
marianna_mass_lo_z1 = marianna_mass_lo_full[cat_z1_ids.astype(int)]
marianna_mass_hi_z1 = marianna_mass_hi_full[cat_z1_ids.astype(int)]

marianna_sfr_z1 = marianna_sfr_full[cat_z1_ids.astype(int)]
marianna_sfr_lo_z1 = marianna_sfr_lo_full[cat_z1_ids.astype(int)]
marianna_sfr_hi_z1 = marianna_sfr_hi_full[cat_z1_ids.astype(int)]

marianna_Av_z1 = marianna_Av_full[cat_z1_ids.astype(int)]

#-------------------------------------------------------------------

marianna_mass_z3 = marianna_mass_full[cat_z3_ids.astype(int)]
marianna_mass_lo_z3 = marianna_mass_lo_full[cat_z3_ids.astype(int)]
marianna_mass_hi_z3 = marianna_mass_hi_full[cat_z3_ids.astype(int)]

marianna_sfr_z3 = marianna_sfr_full[cat_z3_ids.astype(int)]
marianna_sfr_lo_z3 = marianna_sfr_lo_full[cat_z3_ids.astype(int)]
marianna_sfr_hi_z3 = marianna_sfr_hi_full[cat_z3_ids.astype(int)]

marianna_Av_z3 = marianna_Av_full[cat_z3_ids.astype(int)]


#---------------plot SFR-M* diagrams as a consistency check

if vb == True:
    plt.scatter(marianna_mass_small,marianna_sfr_small,c = marianna_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(marianna_mass_z1,marianna_sfr_z1,c = marianna_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(marianna_mass_z3,marianna_sfr_z3,c = marianna_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported Marianna\'s (zPhot) fits.')
