
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

#	ID
#BPASS_log10M*_16	BPASS_log10M*_50	BPASS_log10M*_84
#BPASS_SFR10_16	BPASS_SFR10_50	BPASS_SFR10_84
#BPASS_SFR100_16	BPASS_SFR100_50	BPASS_SFR100_84
#BPASS_A_V_16	BPASS_A_V_50	BPASS_A_V_84
#PEGASE_log10M*_16	PEGASE_log10M*_50	PEGASE_log10M*_84
#PEGASE_SFR10_16	PEGASE_SFR10_50	PEGASE_SFR10_84
#PEGASE_SFR100_16	PEGASE_SFR100_50	PEGASE_SFR100_84
#PEGASE_A_V_16	PEGASE_A_V_50	PEGASE_A_V_84

# Currently using SFR10, come back to this if it needs to be changed to SFR100

#---------------------z1-----------------------------

interrogator_mass_z1_lo_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_mass_z1_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_mass_z1_hi_bpass = np.zeros_like(cat_z1_ids)*np.nan

interrogator_mass_z1_lo_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_mass_z1_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_mass_z1_hi_pegase = np.zeros_like(cat_z1_ids)*np.nan

interrogator_sfr_z1_lo_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_sfr_z1_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_sfr_z1_hi_bpass = np.zeros_like(cat_z1_ids)*np.nan

interrogator_sfr_z1_lo_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_sfr_z1_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_sfr_z1_hi_pegase = np.zeros_like(cat_z1_ids)*np.nan

interrogator_Av_z1_lo_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_Av_z1_bpass = np.zeros_like(cat_z1_ids)*np.nan
interrogator_Av_z1_hi_bpass = np.zeros_like(cat_z1_ids)*np.nan

interrogator_Av_z1_lo_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_Av_z1_pegase = np.zeros_like(cat_z1_ids)*np.nan
interrogator_Av_z1_hi_pegase = np.zeros_like(cat_z1_ids)*np.nan

interrogator_z1_cat = np.genfromtxt('../code_outputs/INTERROGATOR_z1_output.dat')
if vb == True:
    print(interrogator_z1_cat.shape)

interrogator_id_z1 = interrogator_z1_cat[0:,0]
if vb == True:
    print(np.sort(interrogator_id_z1)[1:10])

for i, idtemp in enumerate(cat_z1_ids):

    #print(np.sum(interrogator_id_z1 == (idtemp+1)))

    if np.sum(interrogator_id_z1 == (idtemp+1)) == 1:
        interrogator_mass_z1_lo_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),1]
        interrogator_mass_z1_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),2]
        interrogator_mass_z1_hi_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),3]

        interrogator_mass_z1_lo_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),13]
        interrogator_mass_z1_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),14]
        interrogator_mass_z1_hi_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),15]

        interrogator_sfr_z1_lo_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),4]
        interrogator_sfr_z1_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),5]
        interrogator_sfr_z1_hi_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),6]

        interrogator_sfr_z1_lo_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),16]
        interrogator_sfr_z1_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),17]
        interrogator_sfr_z1_hi_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),18]

        interrogator_Av_z1_lo_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),10]
        interrogator_Av_z1_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),11]
        interrogator_Av_z1_hi_bpass[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),12]

        interrogator_Av_z1_lo_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),22]
        interrogator_Av_z1_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),23]
        interrogator_Av_z1_hi_pegase[i] = interrogator_z1_cat[interrogator_id_z1 == (idtemp+1),24]

#--------------------z3-----------------------------------------

interrogator_mass_z3_lo_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_mass_z3_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_mass_z3_hi_bpass = np.zeros_like(cat_z3_ids)*np.nan

interrogator_mass_z3_lo_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_mass_z3_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_mass_z3_hi_pegase = np.zeros_like(cat_z3_ids)*np.nan

interrogator_sfr_z3_lo_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_sfr_z3_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_sfr_z3_hi_bpass = np.zeros_like(cat_z3_ids)*np.nan

interrogator_sfr_z3_lo_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_sfr_z3_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_sfr_z3_hi_pegase = np.zeros_like(cat_z3_ids)*np.nan

interrogator_Av_z3_lo_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_Av_z3_bpass = np.zeros_like(cat_z3_ids)*np.nan
interrogator_Av_z3_hi_bpass = np.zeros_like(cat_z3_ids)*np.nan

interrogator_Av_z3_lo_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_Av_z3_pegase = np.zeros_like(cat_z3_ids)*np.nan
interrogator_Av_z3_hi_pegase = np.zeros_like(cat_z3_ids)*np.nan

interrogator_z3_cat = np.genfromtxt('../code_outputs/INTERROGATOR_z3_output.dat')
if vb == True:
    print(interrogator_z3_cat.shape)

interrogator_id_z3 = interrogator_z3_cat[0:,0]

if vb == True:
    print(np.sort(interrogator_id_z3)[1:10])

for i, idtemp in enumerate(cat_z3_ids):

    #print(np.sum(interrogator_id_z3 == (idtemp+1)))

    if np.sum(interrogator_id_z3 == (idtemp+1)) == 1:
        interrogator_mass_z3_lo_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),1]
        interrogator_mass_z3_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),2]
        interrogator_mass_z3_hi_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),3]

        interrogator_mass_z3_lo_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),13]
        interrogator_mass_z3_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),14]
        interrogator_mass_z3_hi_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),15]

        interrogator_sfr_z3_lo_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),4]
        interrogator_sfr_z3_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),5]
        interrogator_sfr_z3_hi_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),6]

        interrogator_sfr_z3_lo_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),16]
        interrogator_sfr_z3_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),17]
        interrogator_sfr_z3_hi_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),18]

        interrogator_Av_z3_lo_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),10]
        interrogator_Av_z3_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),11]
        interrogator_Av_z3_hi_bpass[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),12]

        interrogator_Av_z3_lo_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),22]
        interrogator_Av_z3_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),23]
        interrogator_Av_z3_hi_pegase[i] = interrogator_z3_cat[interrogator_id_z3 == (idtemp+1),24]

if vb == True:
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)

    mask = (interrogator_mass_z1_pegase > -99)

    plt.scatter(interrogator_mass_z1_bpass,interrogator_sfr_z1_bpass,c=interrogator_Av_z1_bpass)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')

    plt.subplot(1,2,2)
    plt.scatter(interrogator_mass_z1_pegase[mask],interrogator_sfr_z1_pegase[mask],c=interrogator_Av_z1_pegase[mask])
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.scatter(interrogator_mass_z3_bpass,interrogator_sfr_z3_bpass,c=interrogator_Av_z3_bpass)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')

    plt.subplot(1,2,2)
    plt.scatter(interrogator_mass_z3_pegase,interrogator_sfr_z3_pegase,c=interrogator_Av_z3_pegase)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported interrogator fits.')
