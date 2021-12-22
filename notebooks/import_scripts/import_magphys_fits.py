
import numpy as np
from astropy.io import fits
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

magphys_cat = np.genfromtxt('../code_outputs/magphys_output.dat')
if vb == True:
    print(magphys_cat.shape)

# ID_0
#tau_v16_0   tau_v50_0   tau_v84_0   - 3
#sSFR16_0   sSFR50_0   sSFR84_0    -6
#Mstar16_0   Mstar50_0   Mstar84_0    -9
#Ldust16_0   Ldust50_0   Ldust84_0    -12
#Mdust16_0   Mdust50_0   Mdust84_0    -15
#SFR16_0   SFR50_0   SFR84_0    -18
#age_M16_0   age_M50_0   age_M84_0  -21
#A_V16_0   A_V50_0   A_V84_0    -24
#Tdust16_0   Tdust50_0   Tdust84_0  -27
#tau_v16_agn   tau_v50_agn   tau_v84_agn    -30
#sSFR16_agn   sSFR50_agn   sSFR84_agn    - 33
#Mstar16_agn   Mstar50_agn   Mstar84_agn    -36
#Ldust16_agn   Ldust50_agn   Ldust84_agn    - 39
#Mdust16_agn   Mdust50_agn   Mdust84_agn    - 42
#SFR16_agn   SFR50_agn   SFR84_agn    - 45
#age_M16_agn   age_M50_agn   age_M84_agn   - 48
#A_V16_agn   A_V50_agn   A_V84_agn    - 51
#Tdust16_agn   Tdust50_agn   Tdust84_agn   - 54
#agnf16_agn   agnf50_agn   agnf84_agn    - 57
#Ldustsf16_agn   Ldustsf50_agn   Ldustsf84_agn    -60
#Ldustagn16_agn   Ldustagn50_agn   Ldustagn84_agn

magphys_id_full = magphys_cat[0:,0]

magphys_mass_full = magphys_cat[0:,8]
magphys_mass_full_low = magphys_cat[0:,7]
magphys_mass_full_high = magphys_cat[0:,9]

magphys_sfr_full = magphys_cat[0:,17]
magphys_sfr_full_low = magphys_cat[0:,16]
magphys_sfr_full_high = magphys_cat[0:,18]

magphys_Av_full = magphys_cat[0:,23]
magphys_Av_full_low = magphys_cat[0:,22]
magphys_Av_full_high = magphys_cat[0:,24]

magphys_mass_full_wagn = magphys_cat[0:,35]
magphys_mass_full_low_wagn = magphys_cat[0:,34]
magphys_mass_full_high_wagn = magphys_cat[0:,36]

magphys_sfr_full_wagn = magphys_cat[0:,44]
magphys_sfr_full_low_wagn = magphys_cat[0:,43]
magphys_sfr_full_high_wagn = magphys_cat[0:,45]

magphys_Av_full_wagn = magphys_cat[0:,50]
magphys_Av_full_low_wagn = magphys_cat[0:,49]
magphys_Av_full_high_wagn = magphys_cat[0:,51]



magphys_ids_small = np.zeros((len(cat_small_ids),))

magphys_mass_small = np.zeros((len(cat_small_ids),))
magphys_mass_lo_small = np.zeros((len(cat_small_ids),))
magphys_mass_hi_small = np.zeros((len(cat_small_ids),))

magphys_sfr_small = np.zeros((len(cat_small_ids),))
magphys_sfr_lo_small = np.zeros((len(cat_small_ids),))
magphys_sfr_hi_small = np.zeros((len(cat_small_ids),))

magphys_Av_small = np.zeros((len(cat_small_ids),))
magphys_Av_lo_small = np.zeros((len(cat_small_ids),))
magphys_Av_hi_small = np.zeros((len(cat_small_ids),))

for i in range(len(cat_small_ids)):
    #print(magphys_id_full[magphys_id_full == (cat_small_ids[i]+1)])
    #magphys_ids_small[i] = np.sum([magphys_id_full == cat_small_ids[i]+1])
    magphys_ids_small[i] = magphys_id_full[magphys_id_full == cat_small_ids[i]+1]

    magphys_mass_small[i] = magphys_mass_full[magphys_id_full == cat_small_ids[i]+1]
    magphys_mass_lo_small[i] = magphys_mass_full_low[magphys_id_full == cat_small_ids[i]+1]
    magphys_mass_hi_small[i] = magphys_mass_full_high[magphys_id_full == cat_small_ids[i]+1]

    magphys_sfr_small[i] = magphys_sfr_full[magphys_id_full == cat_small_ids[i]+1]
    magphys_sfr_lo_small[i] = magphys_sfr_full_low[magphys_id_full == cat_small_ids[i]+1]
    magphys_sfr_hi_small[i] = magphys_sfr_full_high[magphys_id_full == cat_small_ids[i]+1]

    magphys_Av_small[i] = magphys_Av_full[magphys_id_full == cat_small_ids[i]+1]
    magphys_Av_lo_small[i] = magphys_Av_full_low[magphys_id_full == cat_small_ids[i]+1]
    magphys_Av_hi_small[i] = magphys_Av_full_high[magphys_id_full == cat_small_ids[i]+1]


magphys_ids_z1 = np.zeros((len(cat_z1_ids),))

magphys_mass_z1 = np.zeros((len(cat_z1_ids),))
magphys_mass_lo_z1 = np.zeros((len(cat_z1_ids),))
magphys_mass_hi_z1 = np.zeros((len(cat_z1_ids),))

magphys_sfr_z1 = np.zeros((len(cat_z1_ids),))
magphys_sfr_lo_z1 = np.zeros((len(cat_z1_ids),))
magphys_sfr_hi_z1 = np.zeros((len(cat_z1_ids),))

magphys_Av_z1 = np.zeros((len(cat_z1_ids),))
magphys_Av_lo_z1 = np.zeros((len(cat_z1_ids),))
magphys_Av_hi_z1 = np.zeros((len(cat_z1_ids),))


for i in range(len(cat_z1_ids)):
    #print(len(magphys_id_full[magphys_id_full == candels_z1_ids[i]+1]))
    if len(magphys_id_full[magphys_id_full == cat_z1_ids[i]+1]) == 1:
        magphys_ids_z1[i] = magphys_id_full[magphys_id_full == cat_z1_ids[i]+1]

        magphys_mass_z1[i] = magphys_mass_full[magphys_id_full == cat_z1_ids[i]+1]
        magphys_mass_lo_z1[i] = magphys_mass_full_low[magphys_id_full == cat_z1_ids[i]+1]
        magphys_mass_hi_z1[i] = magphys_mass_full_high[magphys_id_full == cat_z1_ids[i]+1]

        magphys_sfr_z1[i] = magphys_sfr_full[magphys_id_full == cat_z1_ids[i]+1]
        magphys_sfr_lo_z1[i] = magphys_sfr_full_low[magphys_id_full == cat_z1_ids[i]+1]
        magphys_sfr_hi_z1[i] = magphys_sfr_full_high[magphys_id_full == cat_z1_ids[i]+1]

        magphys_Av_z1[i] = magphys_Av_full[magphys_id_full == cat_z1_ids[i]+1]
        magphys_Av_lo_z1[i] = magphys_Av_full_low[magphys_id_full == cat_z1_ids[i]+1]
        magphys_Av_hi_z1[i] = magphys_Av_full_high[magphys_id_full == cat_z1_ids[i]+1]

    else:
        if vb == True:
            print('id:'+str(cat_z1_ids[i])+' not found. mass set to NaN')
        magphys_mass_z1[i] = np.nan
        magphys_sfr_z1[i] = np.nan

if vb == True:
    print(np.sum(magphys_ids_small))
    print(np.sum(magphys_ids_z1))

    plt.hist(magphys_mass_full)
    plt.show()

magphys_z3 = fits.open('../code_outputs/MAGPHYS_output_z3.fits')
# magphys_z3.info()
# magphys_z3[1].header

magphys_z3_data = magphys_z3[1].data

magphys_ids_z3 = np.zeros((len(cat_z3_ids),))

magphys_mass_z3 = np.zeros((len(cat_z3_ids),))
magphys_mass_lo_z3 = np.zeros((len(cat_z3_ids),))
magphys_mass_hi_z3 = np.zeros((len(cat_z3_ids),))

magphys_sfr_z3 = np.zeros((len(cat_z3_ids),))
magphys_sfr_lo_z3 = np.zeros((len(cat_z3_ids),))
magphys_sfr_hi_z3 = np.zeros((len(cat_z3_ids),))

magphys_Av_z3 = np.zeros((len(cat_z3_ids),))
magphys_Av_lo_z3 = np.zeros((len(cat_z3_ids),))
magphys_Av_hi_z3 = np.zeros((len(cat_z3_ids),))

for i in range(len(magphys_z3_data)):

    magphys_ids_z3[i] = magphys_z3_data[i][0]

    #-----------------------------

    magphys_mass_z3[i] = magphys_z3_data[i][94]
    magphys_mass_lo_z3[i] = magphys_z3_data[i][93]
    magphys_mass_hi_z3[i] = magphys_z3_data[i][95]

    magphys_sfr_z3[i] = magphys_z3_data[i][109]
    magphys_sfr_lo_z3[i] = magphys_z3_data[i][108]
    magphys_sfr_hi_z3[i] = magphys_z3_data[i][110]

    magphys_Av_z3[i] = magphys_z3_data[i][129]
    magphys_Av_lo_z3[i] = magphys_z3_data[i][128]
    magphys_Av_hi_z3[i] = magphys_z3_data[i][130]


#plt.plot(magphys_ids_z3, cat_z3_ids,'.')
#plt.show()
if vb == True:
    plt.scatter(magphys_mass_small,magphys_sfr_small,c=magphys_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(magphys_mass_z1,magphys_sfr_z1, c=magphys_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(magphys_mass_z3,magphys_sfr_z3, c=magphys_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


magphys_z3.close()

print('imported magphys fits.')
