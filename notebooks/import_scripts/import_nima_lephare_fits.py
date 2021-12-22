
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False


# This is a full CANDELS/GOODS-S catalog

nima_cat = np.genfromtxt('../code_outputs/Nima_GOODSS_v2.1.txt')
if vb == True:
    print(nima_cat.shape)

# ==================================================
# 1 ID
# 2 RAdeg
# 3 DECdeg
# 4 z_Best
# 5 E(B-v)
# 6 Rest-frame U/Johnson
# 7 Rest-frame B/Johnson
# 8 Rest-frame V/Johnson
# 9 Rest-frame R/Johnson
# 10 Rest-frame I/Johnson
# 11 Rest-frame J/2mass
# 12 Rest-frame H/2mass
# 13 Rest-frame K/2mass
# 14 Rest-frame UV_1500
# 15 Age_Best
# 16 Age_inf
# 17 Age_med
# 18 Age_sup
# 19 log(Mass)_Best
# 20 log(Mass)_inf
# 21 log(Mass)_med
# 22 log(Mass)_sup
# 23 log(SFR)_Best
# 24 log(SFR)_inf
# 25 log(SFR)_med
# 26 log(SFR)_sup
# 27 log(sSFR)_Best
# 28 log(sSFR)_inf
# 29 log(sSFR)_med
# 30 log(sSFR)_sup
# 31 chi_Best
# 32 Number_of_bands_used
# 33 Model_Best(BC03)
# 34 Class_star
# 35 AGNFlag

# Galaxy IDs
nima_ids_full = nima_cat[0:,0]

# Stellar Mass
nima_mass_full = nima_cat[0:,20]
nima_mass_lo_full = nima_cat[0:,19]
nima_mass_hi_full = nima_cat[0:,21]

# Star Formation Rate
nima_sfr_full = nima_cat[0:,24]
nima_sfr_lo_full = nima_cat[0:,23]
nima_sfr_hi_full = nima_cat[0:,25]

# Dust estimate
nima_Av_full = nima_cat[0:,4]*4.05


#-------------------partition into small, z1, and z3 catalogs-----------------

nima_mass_small = nima_mass_full[cat_small_ids.astype(int)]
nima_mass_lo_small = nima_mass_lo_full[cat_small_ids.astype(int)]
nima_mass_hi_small = nima_mass_hi_full[cat_small_ids.astype(int)]

nima_sfr_small = nima_sfr_full[cat_small_ids.astype(int)]
nima_sfr_lo_small = nima_sfr_lo_full[cat_small_ids.astype(int)]
nima_sfr_hi_small = nima_sfr_hi_full[cat_small_ids.astype(int)]

nima_Av_small = nima_Av_full[cat_small_ids.astype(int)]

#------------------------------------------------------------------

nima_mass_z1 = nima_mass_full[cat_z1_ids.astype(int)]
nima_mass_lo_z1 = nima_mass_lo_full[cat_z1_ids.astype(int)]
nima_mass_hi_z1 = nima_mass_hi_full[cat_z1_ids.astype(int)]

nima_sfr_z1 = nima_sfr_full[cat_z1_ids.astype(int)]
nima_sfr_lo_z1 = nima_sfr_lo_full[cat_z1_ids.astype(int)]
nima_sfr_hi_z1 = nima_sfr_hi_full[cat_z1_ids.astype(int)]

nima_Av_z1 = nima_Av_full[cat_z1_ids.astype(int)]

#------------------------------------------------------------------

nima_mass_z3 = nima_mass_full[cat_z3_ids.astype(int)]
nima_mass_lo_z3 = nima_mass_lo_full[cat_z3_ids.astype(int)]
nima_mass_hi_z3 = nima_mass_hi_full[cat_z3_ids.astype(int)]

nima_sfr_z3 = nima_sfr_full[cat_z3_ids.astype(int)]
nima_sfr_lo_z3 = nima_sfr_lo_full[cat_z3_ids.astype(int)]
nima_sfr_hi_z3 = nima_sfr_hi_full[cat_z3_ids.astype(int)]

nima_Av_z3 = nima_Av_full[cat_z3_ids.astype(int)]

#---------------plot SFR-M* diagrams as a consistency check

if vb == True:
    plt.scatter(nima_mass_small,nima_sfr_small,c = nima_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(nima_mass_z1,nima_sfr_z1,c = nima_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(nima_mass_z3,nima_sfr_z3,c = nima_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported Nima\'s LePhare fits.')
