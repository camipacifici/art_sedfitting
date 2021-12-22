
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

# Header data
#     id    z
#tau  tau_l68  tau_h68
#metal  met_l68  met_h68
#lg_age lg_a_l68 lg_a_h68
#ebv ebv_l68 ebv_h68
#delta del_l68 del_h68
#lg_mass lg_mass_l68 lg_mass_h68
#lg_salmon_sfr lg_sfr lg_sfr_l68 lg_sfr_h68

brett_cat = np.genfromtxt('../code_outputs/fitsed_goods-s_z1_071718.dat')
if vb == True:
    print(brett_cat.shape)


# Galaxy IDs
brett_ids_full = brett_cat[0:,0]

# Stellar Mass
brett_mass_full = brett_cat[0:,17]
brett_mass_lo_full = brett_cat[0:,18]
brett_mass_hi_full = brett_cat[0:,19]

# Star Formation Rate
brett_sfr_full = brett_cat[0:,20]
brett_sfr_lo_full = brett_cat[0:,22] # this one is switched - hi then lo, as opposed to everything else!
brett_sfr_hi_full = brett_cat[0:,21]

# Dust estimate
brett_Av_full = brett_cat[0:,11]*4.05
brett_Av_lo_full = brett_cat[0:,12]*4.05
brett_Av_hi_full = brett_cat[0:,13]*4.05

# some of the dust values are -400, setting these to Nan
brett_Av_full[brett_Av_full < 0] = np.nan

#-------------------get the z1 catalog (no small catalog with the updated version)-----------------

brett_mass_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_sfr_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_Av_z1 = np.zeros((len(cat_z1_ids)))*np.nan

brett_mass_lo_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_sfr_lo_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_Av_lo_z1 = np.zeros((len(cat_z1_ids)))*np.nan

brett_mass_hi_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_sfr_hi_z1 = np.zeros((len(cat_z1_ids)))*np.nan
brett_Av_hi_z1 = np.zeros((len(cat_z1_ids)))*np.nan

for i in range(len(cat_z1_ids)):
    if np.sum(brett_ids_full == cat_z1_ids[i]+1) == 1:
        brett_mass_z1[i] = brett_mass_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_sfr_z1[i] = brett_sfr_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_Av_z1[i] = brett_Av_full[brett_ids_full == cat_z1_ids[i]+1]

        brett_mass_lo_z1[i] = brett_mass_lo_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_sfr_lo_z1[i] = brett_sfr_lo_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_Av_lo_z1[i] = brett_Av_lo_full[brett_ids_full == cat_z1_ids[i]+1]

        brett_mass_hi_z1[i] = brett_mass_hi_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_sfr_hi_z1[i] = brett_sfr_hi_full[brett_ids_full == cat_z1_ids[i]+1]
        brett_Av_hi_z1[i] = brett_Av_hi_full[brett_ids_full == cat_z1_ids[i]+1]

#-----------------------------------------------------------
# Now use another file to get the z3 results

brett_cat = np.genfromtxt('../code_outputs/Salmon_GSD_result.cat')
if vb == True:
    print(brett_cat.shape)



# Galaxy IDs
brett_ids_full = brett_cat[0:,0]

# Stellar Mass
brett_mass_full = brett_cat[0:,17]
brett_mass_lo_full = brett_cat[0:,18]
brett_mass_hi_full = brett_cat[0:,19]

# Star Formation Rate
brett_sfr_full = brett_cat[0:,20]
brett_sfr_lo_full = brett_cat[0:,21]
brett_sfr_hi_full = brett_cat[0:,22]

# Dust estimate
brett_Av_full = brett_cat[0:,11]*4.066
brett_Av_lo_full = brett_cat[0:,12]*4.066
brett_Av_hi_full = brett_cat[0:,13]*4.066

# some of the dust values are -400, setting these to Number_of_bands_used
brett_Av_full[brett_Av_full < 0] = np.nan

brett_mass_z3 = brett_mass_full[cat_z3_ids.astype(int)]
brett_mass_lo_z3 = brett_mass_lo_full[cat_z3_ids.astype(int)]
brett_mass_hi_z3 = brett_mass_hi_full[cat_z3_ids.astype(int)]

brett_sfr_z3 = brett_sfr_full[cat_z3_ids.astype(int)]
brett_sfr_lo_z3 = brett_sfr_lo_full[cat_z3_ids.astype(int)]
brett_sfr_hi_z3 = brett_sfr_hi_full[cat_z3_ids.astype(int)]

brett_Av_z3 = brett_Av_full[cat_z3_ids.astype(int)]
brett_Av_lo_z3 = brett_Av_lo_full[cat_z3_ids.astype(int)]
brett_Av_hi_z3 = brett_Av_hi_full[cat_z3_ids.astype(int)]

#---------------plot SFR-M* diagrams as a consistency check

if vb == True:

    plt.scatter(brett_mass_z1[brett_sfr_z1>-90],brett_sfr_z1[brett_sfr_z1>-90],c = brett_Av_z1[brett_sfr_z1>-90])
    plt.colorbar()
    #plt.ylim(-10,3)
    #plt.xlim(4,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(brett_mass_z3,brett_sfr_z3,c = brett_Av_z3)
    plt.colorbar()
    #plt.ylim(-10,3)
    #plt.xlim(4,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

    np.sum(np.isnan(brett_mass_z3) == np.nan)

print('imported FITSED (salmon+15?) fits.')
