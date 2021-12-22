import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

# This is a full CANDELS/GOODS-S catalog

DB_cat = np.genfromtxt('../code_outputs/Dense_Basis_GOODS-S_v1.2.dat',delimiter=',')
if vb == True:
    print(DB_cat.shape)

DB_cat_dust_uncert = np.genfromtxt('../code_outputs/Dense_Basis_GOODS-S_v1.2_dust_uncertainties.dat')
if vb == True:
    print(DB_cat_dust_uncert.shape)

# Header quantities:
# ID, z_fit, useflag,
# logM_gal, logM*, logM*_84, logM*_16,
# log_SFR_inst, log_SFR_inst_84, log_SFR_inst_16,
# log_SFR_100, log_SFR_300, log_SFR_500,
# t10_gyr, t50_gyr, t90_gyr,
# age_gyr, Av_calzetti, log_Z/Zsolar

# Galaxy IDs
DB_id_full = DB_cat[0:,0]

# Stellar Mass
DB_mass_full = DB_cat[0:,4]
DB_mass_lo_full = DB_cat[0:,6]
DB_mass_hi_full = DB_cat[0:,5]
# uncertainty floor of 0.1 dex
DB_mass_lo_full[(DB_mass_full - DB_mass_lo_full) < 0.1] = DB_mass_full[(DB_mass_full - DB_mass_lo_full) < 0.1] - 0.1
DB_mass_hi_full[(DB_mass_hi_full - DB_mass_full) < 0.1] = DB_mass_full[(DB_mass_hi_full - DB_mass_full) < 0.1] + 0.1

# Star Formation Rate
DB_sfr_full = DB_cat[0:,7]
DB_sfr_lo_full = DB_cat[0:,9]
DB_sfr_hi_full = DB_cat[0:,8]
# uncertainty floor of 0.1 dex
DB_sfr_lo_full[(DB_sfr_full - DB_sfr_lo_full) < 0.1] = DB_sfr_full[(DB_sfr_full - DB_sfr_lo_full) < 0.1] - 0.1
DB_sfr_hi_full[(DB_sfr_hi_full - DB_sfr_full) < 0.1] = DB_sfr_full[(DB_sfr_hi_full - DB_sfr_full) < 0.1] + 0.1

# Dust estimate
DB_Av_full = DB_cat[0:,-2]
DB_Av_lo_full = DB_cat_dust_uncert[0:,0]
DB_Av_hi_full = DB_cat_dust_uncert[0:,1]
# uncertainty floor of 0.1 mags
DB_Av_lo_full[(DB_Av_full - DB_Av_lo_full) < 0.1] = DB_Av_full[(DB_Av_full - DB_Av_lo_full) < 0.1] - 0.1
DB_Av_hi_full[(DB_Av_hi_full - DB_Av_full) < 0.1] = DB_Av_full[(DB_Av_hi_full - DB_Av_full) < 0.1] + 0.1

#-------------------partition into small, z1, and z3 catalogs-----------------

DB_mass_small = DB_mass_full[cat_small_ids.astype(int)]
DB_mass_lo_small = DB_mass_lo_full[cat_small_ids.astype(int)]
DB_mass_hi_small = DB_mass_hi_full[cat_small_ids.astype(int)]

DB_sfr_small = DB_sfr_full[cat_small_ids.astype(int)]
DB_sfr_lo_small = DB_sfr_lo_full[cat_small_ids.astype(int)]
DB_sfr_hi_small = DB_sfr_hi_full[cat_small_ids.astype(int)]

DB_Av_small = DB_Av_full[cat_small_ids.astype(int)]
DB_Av_lo_small = DB_Av_lo_full[cat_small_ids.astype(int)]
DB_Av_hi_small = DB_Av_hi_full[cat_small_ids.astype(int)]

#----------------------------------------------------------

DB_mass_z1 = DB_mass_full[cat_z1_ids.astype(int)]
DB_mass_lo_z1 = DB_mass_lo_full[cat_z1_ids.astype(int)]
DB_mass_hi_z1 = DB_mass_hi_full[cat_z1_ids.astype(int)]

DB_sfr_z1 = DB_sfr_full[cat_z1_ids.astype(int)]
DB_sfr_lo_z1 = DB_sfr_lo_full[cat_z1_ids.astype(int)]
DB_sfr_hi_z1 = DB_sfr_hi_full[cat_z1_ids.astype(int)]

DB_Av_z1 = DB_Av_full[cat_z1_ids.astype(int)]
DB_Av_lo_z1 = DB_Av_lo_full[cat_z1_ids.astype(int)]
DB_Av_hi_z1 = DB_Av_hi_full[cat_z1_ids.astype(int)]

#---------------------------------------------------------

DB_mass_z3 = DB_mass_full[cat_z3_ids.astype(int)]
DB_mass_lo_z3 = DB_mass_lo_full[cat_z3_ids.astype(int)]
DB_mass_hi_z3 = DB_mass_hi_full[cat_z3_ids.astype(int)]

DB_sfr_z3 = DB_sfr_full[cat_z3_ids.astype(int)]
DB_sfr_lo_z3 = DB_sfr_lo_full[cat_z3_ids.astype(int)]
DB_sfr_hi_z3 = DB_sfr_hi_full[cat_z3_ids.astype(int)]

DB_Av_z3 = DB_Av_full[cat_z3_ids.astype(int)]
DB_Av_lo_z3 = DB_Av_lo_full[cat_z3_ids.astype(int)]
DB_Av_hi_z3 = DB_Av_hi_full[cat_z3_ids.astype(int)]


#---------------plot SFR-M* diagrams as a consistency check

if vb == True:
    plt.scatter(DB_mass_small,DB_sfr_small,c = DB_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(DB_mass_z1,DB_sfr_z1,c = DB_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(DB_mass_z3,DB_sfr_z3,c = DB_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported dense basis fits.')
