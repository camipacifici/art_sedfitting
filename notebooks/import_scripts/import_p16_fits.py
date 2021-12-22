# This is a full CANDELS/GOODS-S catalog

#  id
# logM_50   logSFR100_50       logMt_50        tauV_50      lmwAGE_50         zzz_50
# AV_50        AFUV_50        ANUV_50
# logM_16   logSFR100_16      logMt__16        tauV_16      lmwAGE_16         zzz_16
# AV_16        AFUV_16        ANUV_16
# logM_84   logSFR100_84      logMt__84        tauV_84      lmwAGE_84         zzz_84
# AV_84        AFUV_84        ANUV_84

import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat() #get the needed IDs

vb = False

cami_catalog = np.genfromtxt('../code_outputs/cami_mederr_GDSS_znew_avgal_np_sfr100mwage.dat')

if vb == True:
    print(cami_catalog.shape)

# Galaxy IDs
cami_id_full = cami_catalog[0:,0]

# Stellar Mass
cami_mass_full = cami_catalog[0:,1]
cami_mass_lo_full = cami_catalog[0:,10]
cami_mass_hi_full = cami_catalog[0:,19]

# Star Formation Rate
cami_sfr_full = cami_catalog[0:,2]
cami_sfr_lo_full = cami_catalog[0:,11]
cami_sfr_hi_full = cami_catalog[0:,20]

# Dust estimate
cami_AV_full = cami_catalog[0:,7]
cami_AV_lo_full = cami_catalog[0:,16]
cami_AV_hi_full = cami_catalog[0:,25]

#-------------------partition into small, z1, ad z3 catalogs-----------------

cami_mass_small = cami_mass_full[cat_small_ids.astype(int)]
cami_mass_lo_small = cami_mass_lo_full[cat_small_ids.astype(int)]
cami_mass_hi_small = cami_mass_hi_full[cat_small_ids.astype(int)]

cami_sfr_small = cami_sfr_full[cat_small_ids.astype(int)]
cami_sfr_lo_small = cami_sfr_lo_full[cat_small_ids.astype(int)]
cami_sfr_hi_small = cami_sfr_hi_full[cat_small_ids.astype(int)]

cami_Av_small = cami_AV_full[cat_small_ids.astype(int)]
cami_Av_lo_small = cami_AV_lo_full[cat_small_ids.astype(int)]
cami_Av_hi_small = cami_AV_hi_full[cat_small_ids.astype(int)]

#-------------------------------------------------------------

cami_mass_z1 = cami_mass_full[cat_z1_ids.astype(int)]
cami_mass_lo_z1 = cami_mass_lo_full[cat_z1_ids.astype(int)]
cami_mass_hi_z1 = cami_mass_hi_full[cat_z1_ids.astype(int)]

cami_sfr_z1 = cami_sfr_full[cat_z1_ids.astype(int)]
cami_sfr_lo_z1 = cami_sfr_lo_full[cat_z1_ids.astype(int)]
cami_sfr_hi_z1 = cami_sfr_hi_full[cat_z1_ids.astype(int)]

cami_Av_z1 = cami_AV_full[cat_z1_ids.astype(int)]
cami_Av_lo_z1 = cami_AV_lo_full[cat_z1_ids.astype(int)]
cami_Av_hi_z1 = cami_AV_hi_full[cat_z1_ids.astype(int)]

#-------------------------------------------------------------

cami_mass_z3 = cami_mass_full[cat_z3_ids.astype(int)]
cami_mass_lo_z3 = cami_mass_lo_full[cat_z3_ids.astype(int)]
cami_mass_hi_z3 = cami_mass_hi_full[cat_z3_ids.astype(int)]

cami_sfr_z3 = cami_sfr_full[cat_z3_ids.astype(int)]
cami_sfr_lo_z3 = cami_sfr_lo_full[cat_z3_ids.astype(int)]
cami_sfr_hi_z3 = cami_sfr_hi_full[cat_z3_ids.astype(int)]

cami_Av_z3 = cami_AV_full[cat_z3_ids.astype(int)]
cami_Av_lo_z3 = cami_AV_lo_full[cat_z3_ids.astype(int)]
cami_Av_hi_z3 = cami_AV_hi_full[cat_z3_ids.astype(int)]


if vb == True:
    #---------------plot SFR-M* diagrams as a consistency check

    plt.scatter(cami_mass_small,cami_sfr_small,c = cami_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(cami_mass_z1,cami_sfr_z1,c = cami_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(cami_mass_z3,cami_sfr_z3,c = cami_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported pacifici+16 fits.')
