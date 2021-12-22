
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

######----------------small------------------

sed3fit_small_cat = np.genfromtxt('../code_outputs/RIVERSIDE_SMALL_SED3FIT_RESULTS_8_2_corrected.dat')

# ID_0    tau_v16_0   tau_v50_0   tau_v84_0  Mstar16_0   Mstar50_0   Mstar84_0   SFR16_0   SFR50_0   SFR84_0

# new headers
# ID    tau_v16   tau_v50   tau_v84
#age_mw16   age_mw50   age_mw84
#Mstar16   Mstar50   Mstar84
#SFR16_7   SFR50_7   SFR84_7
#SFR16_8   SFR50_8   SFR84_8

# ID    tau_v16   tau_v50   tau_v84
# age_mw16   age_mw50   age_mw84
# Mstar16   Mstar50   Mstar84
# SFR16_7   SFR50_7   SFR84_7
# SFR16_8   SFR50_8   SFR84_8
# Av Av_std

sed3fit_id_small = sed3fit_small_cat[0:,0]

sed3fit_mass_small = sed3fit_small_cat[0:,8]
sed3fit_mass_small_low = sed3fit_small_cat[0:,7]
sed3fit_mass_small_high = sed3fit_small_cat[0:,9]

sed3fit_sfr_small = (sed3fit_small_cat[0:,14])
sed3fit_sfr_small_low = (sed3fit_small_cat[0:,13])
sed3fit_sfr_small_high = (sed3fit_small_cat[0:,15])

sed3fit_av_small = sed3fit_small_cat[0:,16]
sed3fit_av_small_low = sed3fit_small_cat[0:,16]-0.1
sed3fit_av_small_high = sed3fit_small_cat[0:,16]+0.1

#----------------------------z1---------------------

sed3fit_z1_cat = np.genfromtxt('../code_outputs/RIVERSIDE_z1_SED3FIT_RESULTS_8_2_corrected.dat')

# ID_0    tau_v16_0   tau_v50_0   tau_v84_0  Mstar16_0   Mstar50_0   Mstar84_0   SFR16_0   SFR50_0   SFR84_0

sed3fit_id_z1 = sed3fit_z1_cat[0:,0]

sed3fit_mass_z1 = sed3fit_z1_cat[0:,8]
sed3fit_mass_z1_low = sed3fit_z1_cat[0:,7]
sed3fit_mass_z1_high = sed3fit_z1_cat[0:,9]
# 0.1 dex uncertainty floor
sed3fit_mass_z1_low[(sed3fit_mass_z1 - sed3fit_mass_z1_low) < 0.1] = sed3fit_mass_z1[(sed3fit_mass_z1 - sed3fit_mass_z1_low) < 0.1] - 0.1
sed3fit_mass_z1_high[(sed3fit_mass_z1_high - sed3fit_mass_z1) < 0.1] = sed3fit_mass_z1[(sed3fit_mass_z1_high - sed3fit_mass_z1) < 0.1] + 0.1

sed3fit_sfr_z1 = (sed3fit_z1_cat[0:,14])
sed3fit_sfr_z1_low = (sed3fit_z1_cat[0:,13])
sed3fit_sfr_z1_high = (sed3fit_z1_cat[0:,15])
# 0.1 dex uncertainty floor
sed3fit_sfr_z1_low[(sed3fit_sfr_z1 - sed3fit_sfr_z1_low) < 0.1] = sed3fit_sfr_z1[(sed3fit_sfr_z1 - sed3fit_sfr_z1_low) < 0.1] - 0.1
sed3fit_sfr_z1_high[(sed3fit_sfr_z1_high - sed3fit_sfr_z1) < 0.1] = sed3fit_sfr_z1[(sed3fit_sfr_z1_high - sed3fit_sfr_z1) < 0.1] + 0.1

sed3fit_av_z1 = sed3fit_z1_cat[0:,16]
sed3fit_av_z1_low = sed3fit_z1_cat[0:,16]-sed3fit_z1_cat[0:,17]
sed3fit_av_z1_high = sed3fit_z1_cat[0:,16]+sed3fit_z1_cat[0:,17]

#----------------------------z3-------------------------

sed3fit_z3_cat = np.genfromtxt('../code_outputs/RIVERSIDE_z3_SED3FIT_RESULTS_8_2_corrected.dat')

# ID_0    tau_v16_0   tau_v50_0   tau_v84_0  Mstar16_0   Mstar50_0   Mstar84_0   SFR16_0   SFR50_0   SFR84_0

sed3fit_id_z3 = sed3fit_z3_cat[0:,0]

sed3fit_mass_z3 = sed3fit_z3_cat[0:,8]
sed3fit_mass_z3_low = sed3fit_z3_cat[0:,7]
sed3fit_mass_z3_high = sed3fit_z3_cat[0:,9]

sed3fit_sfr_z3 = (sed3fit_z3_cat[0:,14])
sed3fit_sfr_z3_low = (sed3fit_z3_cat[0:,13])
sed3fit_sfr_z3_high =(sed3fit_z3_cat[0:,15])

sed3fit_av_z3 = sed3fit_z3_cat[0:,16]
sed3fit_av_z3_low = sed3fit_z3_cat[0:,16]-0.1
sed3fit_av_z3_high = sed3fit_z3_cat[0:,16]+0.1



if vb == True:
    plt.scatter(sed3fit_mass_small,sed3fit_sfr_small,c=sed3fit_tauv_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(sed3fit_mass_z1,sed3fit_sfr_z1,c=sed3fit_tauv_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(sed3fit_mass_z3,sed3fit_sfr_z3,c=sed3fit_tauv_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported SED3fit fits.')
