import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt
from tqdm import tqdm
import warnings

import scipy.io as sio

from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
cosmo.age(1)

import seaborn as sns
import pandas as pd
from astropy.io import fits

sns.set(font_scale=2)
sns.set_style("whitegrid")

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import statsmodels.api as sm
lowess = sm.nonparametric.lowess

#----------import catalogs----------------------------

warnings.filterwarnings('ignore')

candels_cat_z1 = np.loadtxt('../catalogs/CANDELS_GDSS_workshop_z1.dat')

# subtracting 1 from the ID for python indexing
cat_z1_ids = candels_cat_z1[0:,0] - 1
cat_z1_z = candels_cat_z1[0:,1]

# print(str(cat_z1_z.shape[0])+' galaxies in the z~1 catalog.')

ircat = np.genfromtxt('../catalogs/CANDELS_GDSS_workshop_z1_fluxes_Jy_UVtoIR.dat')
# print(ircat.shape)

# ID      zz                   1
# CTIO_U             eCTIO_U    3
# VIMOS_U            eVIMOS_U    5
# ACS_F435W          eACS_F435W   7
# ACS_F606W          eACS_F606W    9
# ACS_F775W          eACS_F775W     11
# ACS_F814W          eACS_F814W      13
# ACS_F850LP         eACS_F850LP       15
# WFC3_F098M   eWFC3_F098M   17
# WFC3_F105W         eWFC3_F105W 19
# WFC3_F125W         eWFC3_F125W   21
# WFC3_F160W         eWFC3_F160W     23
# ISAAC_KS           eISAAC_KS         25
# HAWKI_KS           eHAWKI_KS          27
# IRAC_CH1           eIRAC_CH1          29
# IRAC_CH2           eIRAC_CH2          31
# IRAC_CH3           eIRAC_CH3          33
# IRAC_CH4           eIRAC_CH4          35
# f24            ef24           37
# f70            ef70           39
# f100           ef100          41
# f160           ef160          43
# f250           ef250          45
# flg1   flg2  47


#--------------------------------------------------------
#-------------------PROSPECTOR---------------------------
#--------------------------------------------------------

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

# objname,
# logmass,logmass_errup,logmass_errdown,
# logsfr100,logsfr100_errup,logsfr100_errdown,
# logsfr10,logsfr10_errup,logsfr10_errdown,
# mwa,mwa_errup,mwa_errdown,
# av,av_errup,av_errdown

prospector_cat_z1_IR = np.genfromtxt('../code_outputs_IR/prospector_output_z1_ir.dat',delimiter=',')

prospector_ids_z1_IR = prospector_cat_z1_IR[0:,0]

prospector_mass_z1_IR = prospector_cat_z1_IR[0:,1]
prospector_mass_hi_z1_IR = prospector_cat_z1_IR[0:,1] + prospector_cat_z1_IR[0:,2]
prospector_mass_lo_z1_IR = prospector_cat_z1_IR[0:,1] - prospector_cat_z1_IR[0:,3]

prospector_sfr_z1_IR = prospector_cat_z1_IR[0:,7]
prospector_sfr_hi_z1_IR = prospector_cat_z1_IR[0:,7] + prospector_cat_z1_IR[0:,8]
prospector_sfr_lo_z1_IR = prospector_cat_z1_IR[0:,7] - prospector_cat_z1_IR[0:,9]

prospector_Av_z1_IR = prospector_cat_z1_IR[0:,13]
prospector_Av_hi_z1_IR = prospector_cat_z1_IR[0:,13] + prospector_cat_z1_IR[0:,14]
prospector_Av_lo_z1_IR = prospector_cat_z1_IR[0:,13] - prospector_cat_z1_IR[0:,15]


prospector_cat_z1_IR_AGN = np.genfromtxt('../code_outputs_IR/prospector_output_z1_ir_agn.dat',delimiter=',')

prospector_ids_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,0]

prospector_mass_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,1]
prospector_mass_hi_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,1] + prospector_cat_z1_IR_AGN[0:,2]
prospector_mass_lo_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,1] - prospector_cat_z1_IR_AGN[0:,3]

prospector_sfr_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,7]
prospector_sfr_hi_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,7] + prospector_cat_z1_IR_AGN[0:,8]
prospector_sfr_lo_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,7] - prospector_cat_z1_IR_AGN[0:,9]

prospector_Av_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,13]
prospector_Av_hi_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,13] + prospector_cat_z1_IR_AGN[0:,14]
prospector_Av_lo_z1_IR_AGN = prospector_cat_z1_IR_AGN[0:,13] - prospector_cat_z1_IR_AGN[0:,15]




#--------------------------------------------------------
#-------------------AGNFITTER----------------------------
#--------------------------------------------------------

agnfitter_full = fits.open('../code_outputs_IR/AGNfitter_CANDELS_z1sample.fits')
# agnfitter_full.info()
# agnfitter_full[1].header

agnfitter_cat = agnfitter_full[1].data

agnfitter_ids = np.zeros((len(cat_z1_ids),))

agnfitter_mass = np.zeros((len(cat_z1_ids),))
agnfitter_mass_lo = np.zeros((len(cat_z1_ids),))
agnfitter_mass_hi = np.zeros((len(cat_z1_ids),))

agnfitter_sfr = np.zeros((len(cat_z1_ids),))
agnfitter_sfr_lo = np.zeros((len(cat_z1_ids),))
agnfitter_sfr_hi = np.zeros((len(cat_z1_ids),))

agnfitter_av = np.zeros((len(cat_z1_ids)))
agnfitter_av_lo = np.zeros((len(cat_z1_ids)))
agnfitter_av_hi = np.zeros((len(cat_z1_ids)))

#for i in range(agnfitter_ids.shape[0]):
for i in range(369):

    temp = agnfitter_full[1].data[i][0]
    id_index = np.argmin(np.abs(temp - cat_z1_ids+1))
    agnfitter_ids[id_index] = temp

    agnfitter_mass[id_index] = agnfitter_full[1].data[i][4]
    agnfitter_sfr[id_index] = np.log10(agnfitter_full[1].data[i][7])
    agnfitter_av[id_index] = agnfitter_full[1].data[i][1] * 4.05
#
# print(cat_z1_ids[0:10]+1)
# print(agnfitter_ids[0:10])

# plt.scatter(agnfitter_mass[agnfitter_ids>0], agnfitter_sfr[agnfitter_ids>0],c=agnfitter_av[agnfitter_ids>0],cmap='magma')
# plt.show()

# agnfitter_full.close()


#--------------------------------------------------------
#---------------------MAGPHYS----------------------------
#--------------------------------------------------------

magphys_cat = np.genfromtxt('../code_outputs/magphys_output.dat')
# print(magphys_cat.shape)

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


magphys_mass_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_mass_lo_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_mass_hi_z1_wagn = np.zeros((len(cat_z1_ids),))

magphys_sfr_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_sfr_lo_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_sfr_hi_z1_wagn = np.zeros((len(cat_z1_ids),))

magphys_Av_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_Av_lo_z1_wagn = np.zeros((len(cat_z1_ids),))
magphys_Av_hi_z1_wagn = np.zeros((len(cat_z1_ids),))

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

        magphys_mass_z1_wagn[i] = magphys_mass_full_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_mass_lo_z1_wagn[i] = magphys_mass_full_low_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_mass_hi_z1_wagn[i] = magphys_mass_full_high_wagn[magphys_id_full == cat_z1_ids[i]+1]

        magphys_sfr_z1_wagn[i] = magphys_sfr_full_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_sfr_lo_z1_wagn[i] = magphys_sfr_full_low_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_sfr_hi_z1_wagn[i] = magphys_sfr_full_high_wagn[magphys_id_full == cat_z1_ids[i]+1]

        magphys_Av_z1_wagn[i] = magphys_Av_full_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_Av_lo_z1_wagn[i] = magphys_Av_full_low_wagn[magphys_id_full == cat_z1_ids[i]+1]
        magphys_Av_hi_z1_wagn[i] = magphys_Av_full_high_wagn[magphys_id_full == cat_z1_ids[i]+1]
    else:
        # print('id:'+str(cat_z1_ids[i])+' not found. mass set to NaN')
        magphys_mass_z1[i] = np.nan
        magphys_sfr_z1[i] = np.nan
        magphys_mass_z1_wagn[i] = np.nan
        magphys_sfr_z1_wagn[i] = np.nan

# print(np.sum(magphys_ids_z1))

# plt.hist(magphys_mass_full)
# plt.show()

magphys_IR_full = fits.open('../code_outputs_IR/magphys_output_z1_ir.fits')
# magphys_IR_full.info()
# magphys_IR_full[1].header

magphys_ir_ids = np.zeros((len(cat_z1_ids),))

magphys_ir_mass = np.zeros((len(cat_z1_ids),))
magphys_ir_sfr = np.zeros((len(cat_z1_ids),))
magphys_ir_av = np.zeros((len(cat_z1_ids),))

magphys_ir_mass_AGN = np.zeros((len(cat_z1_ids),))
magphys_ir_sfr_AGN = np.zeros((len(cat_z1_ids),))
magphys_ir_av_AGN = np.zeros((len(cat_z1_ids),))


for i in range(len(magphys_IR_full[1].data)):

    temp = magphys_IR_full[1].data[i][0]
    id_index = np.argmin(np.abs(cat_z1_ids - float(temp[0:-4])))

    magphys_ir_ids[id_index] = float(temp[0:-4])

    magphys_ir_mass[id_index] = magphys_IR_full[1].data[i][109]
    magphys_ir_sfr[id_index] = magphys_IR_full[1].data[i][124]
    magphys_ir_av[id_index] = magphys_IR_full[1].data[i][144]

    magphys_ir_mass_AGN[id_index] = magphys_IR_full[1].data[i][270]
    magphys_ir_sfr_AGN[id_index] = magphys_IR_full[1].data[i][285]
    magphys_ir_av_AGN[id_index] = magphys_IR_full[1].data[i][305]

magphys_IR_full.close()

#--------------------------------------------------------
#---------------------BAGPIPES---------------------------
#--------------------------------------------------------


print('importing BAGPIPES files from Mar 11, 2019')

bagpipes_cat_z1 = Table.read('../code_outputs/bagpipes_11_3_19_z1_noir.cat', format = 'ascii.commented_header')
bagpipes_cat_z1.sort('ID')

bagpipes_id = bagpipes_cat_z1['ID']

bagpipes_IR_av_lo = bagpipes_cat_z1['dust:Av_16']
bagpipes_IR_av = bagpipes_cat_z1['dust:Av_50']
bagpipes_IR_av_hi = bagpipes_cat_z1['dust:Av_84']

bagpipes_IR_mass_lo = bagpipes_cat_z1['stellar_mass_16']
bagpipes_IR_mass = bagpipes_cat_z1['stellar_mass_50']
bagpipes_IR_mass_hi = bagpipes_cat_z1['stellar_mass_84']

bagpipes_IR_sfr_lo = np.log10(bagpipes_cat_z1['sfr_16'])
bagpipes_IR_sfr = np.log10(bagpipes_cat_z1['sfr_50'])
bagpipes_IR_sfr_hi = np.log10(bagpipes_cat_z1['sfr_84'])


bagpipes_cat_z1 = Table.read('../code_outputs_IR/bagpipes_11_3_19_z1_ir.cat', format = 'ascii.commented_header')
bagpipes_cat_z1.sort('ID')

bagpipes_id = bagpipes_cat_z1['ID']

bagpipes_Av_lo_z1= bagpipes_cat_z1['dust:Av_16']
bagpipes_Av_z1 = bagpipes_cat_z1['dust:Av_50']
bagpipes_Av_hi_z1 = bagpipes_cat_z1['dust:Av_84']

bagpipes_mass_lo_z1 = bagpipes_cat_z1['stellar_mass_16']
bagpipes_mass_z1 = bagpipes_cat_z1['stellar_mass_50']
bagpipes_mass_hi_z1 = bagpipes_cat_z1['stellar_mass_84']

bagpipes_sfr_lo_z1 = np.log10(bagpipes_cat_z1['sfr_16'])
bagpipes_sfr_z1 = np.log10(bagpipes_cat_z1['sfr_50'])
bagpipes_sfr_hi_z1 = np.log10(bagpipes_cat_z1['sfr_84'])


#--------------------------------------------------------
#-----------------------CIGALE---------------------------
#--------------------------------------------------------

c1 = fits.open('../code_outputs/cigale_UV_NIR_2020.fits')
print('imported CIGALE files (z=1 fits from Oct 2020, z=3 fits from 27 Feb 2019)')
# c1.info()
# c1[1].header

cigale_ids = np.zeros((len(cat_z1_ids),))

cigale_mass = np.zeros((len(cat_z1_ids),))
cigale_sfr = np.zeros((len(cat_z1_ids),))
cigale_Av = np.zeros((len(cat_z1_ids),))

cigale_mass_err = np.zeros((len(cat_z1_ids),))
cigale_sfr_err = np.zeros((len(cat_z1_ids),))
cigale_Av_err = np.zeros((len(cat_z1_ids),))

for i in range(len(cat_z1_ids)):
    temp = c1[1].data[i][0]

    cigale_ids[i] = temp
    cigale_mass[i] = c1[1].data[i][1]
    cigale_sfr[i] = c1[1].data[i][3]
    cigale_Av[i] = c1[1].data[i][5]

    cigale_mass_err[i] = c1[1].data[i][2]
    cigale_sfr_err[i] = c1[1].data[i][4]
    cigale_Av_err[i] = c1[1].data[i][6]

c1.close()

# plt.scatter(cigale_mass,cigale_sfr,c=cigale_Av,cmap='viridis');plt.colorbar()
# plt.show()

c2 = fits.open('../code_outputs_IR/cigale_UV_FIR_noAGN_2020.fits')
# c2.info()


cigale_ir_ids = np.zeros((len(cat_z1_ids),))

cigale_ir_mass = np.zeros((len(cat_z1_ids),))
cigale_ir_sfr = np.zeros((len(cat_z1_ids),))
cigale_ir_Av = np.zeros((len(cat_z1_ids),))

cigale_ir_mass_err = np.zeros((len(cat_z1_ids),))
cigale_ir_sfr_err = np.zeros((len(cat_z1_ids),))
cigale_ir_Av_err = np.zeros((len(cat_z1_ids),))

for i in range(len(cat_z1_ids)):
    temp = c2[1].data[i][0]

    cigale_ir_ids[i] = temp
    cigale_ir_mass[i] = c2[1].data[i][1]
    cigale_ir_sfr[i] = c2[1].data[i][3]
    cigale_ir_Av[i] = c2[1].data[i][5]

    cigale_ir_mass_err[i] = c2[1].data[i][2]
    cigale_ir_sfr_err[i] = c2[1].data[i][4]
    cigale_ir_Av_err[i] = c2[1].data[i][6]


# c2[1].header
c2.close()

# plt.scatter(cigale_ir_mass,cigale_ir_sfr,c=cigale_ir_Av,cmap='viridis');plt.colorbar()
# plt.show()

c3 = fits.open('../code_outputs_IR/cigale_UV_FIR_withAGN_2020.fits')
# c3.info()


cigale_ir_agn_ids = np.zeros((len(cat_z1_ids),))

cigale_ir_agn_mass = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_sfr = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_Av = np.zeros((len(cat_z1_ids),))

cigale_ir_agn_mass_err = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_sfr_err = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_Av_err = np.zeros((len(cat_z1_ids),))

for i in range(len(cat_z1_ids)):
    temp = c3[1].data[i][0]

    cigale_ir_agn_ids[i] = temp
    cigale_ir_agn_mass[i] = c3[1].data[i][1]
    cigale_ir_agn_sfr[i] = c3[1].data[i][3]
    cigale_ir_agn_Av[i] = c3[1].data[i][5]

    cigale_ir_agn_mass_err[i] = c3[1].data[i][2]
    cigale_ir_agn_sfr_err[i] = c3[1].data[i][4]
    cigale_ir_agn_Av_err[i] = c3[1].data[i][6]

# c3[1].header
c3.close()

#--------------------------------------------------------
#---------------------SED3FIT----------------------------
#--------------------------------------------------------

#sed3fit_cat = np.genfromtxt('code_outputs_IR/RIVERSIDE_z1_SED3FIT_RESULTS_8_2.dat')
#sed3fit_mass = sed3fit_cat[0:,8]
#sed3fit_sfr = sed3fit_cat[0:,11]
#sed3fit_av = sed3fit_cat[0:,16]


sed3fit_cat = np.genfromtxt('../code_outputs_IR/RIVERSIDE_z1_NO_IR_SED3FIT_RESULTS_10_10.dat')
# print(sed3fit_cat.shape)

# ID
# tau_v16   tau_v50   tau_v84
# age_mw16   age_mw50   age_mw84
# Mstar16   Mstar50   Mstar84
# SFR16_7   SFR50_7   SFR84_7
# SFR16_8   SFR50_8   SFR84_8
# Av Av_std

sed3fit_mass = np.zeros((len(cat_z1_ids),))
sed3fit_sfr = np.zeros((len(cat_z1_ids),))
sed3fit_av = np.zeros((len(cat_z1_ids),))
sed3fit_agnfracs = np.zeros((len(cat_z1_ids),))

sed3fit_internal_id = sed3fit_cat[0:,0]
for i in range(len(sed3fit_internal_id)):
    id_index = np.argmin(np.abs(sed3fit_internal_id[i] - cat_z1_ids))
    sed3fit_mass[id_index] = sed3fit_cat[0:,8][i]
    sed3fit_sfr[id_index] = sed3fit_cat[0:,14][i] # update to SFR100 instead of SFR10
    sed3fit_av[id_index] = sed3fit_cat[0:,16][i]
    sed3fit_agnfracs[id_index] = sed3fit_cat[0:,18][i]


# plt.scatter(sed3fit_mass, sed3fit_sfr,c=sed3fit_av,cmap='magma')
# plt.show()

sed3fit_cat = np.genfromtxt('../code_outputs_IR/RIVERSIDE_z1_ONLY_IR_SED3FIT_RESULTS_10_10.dat')
# print(sed3fit_ir_cat.shape)


# sed3fit_ir_mass = sed3fit_ir_cat[0:,8]
# sed3fit_ir_sfr = sed3fit_ir_cat[0:,11]
# sed3fit_ir_av = sed3fit_ir_cat[0:,16]

sed3fit_ir_mass = np.zeros((len(cat_z1_ids),))
sed3fit_ir_sfr = np.zeros((len(cat_z1_ids),))
sed3fit_ir_av = np.zeros((len(cat_z1_ids),))
sed3fit_ir_agnfracs = np.zeros((len(cat_z1_ids),))

sed3fit_internal_id = sed3fit_cat[0:,0]
for i in range(len(sed3fit_internal_id)):
    id_index = np.argmin(np.abs(sed3fit_internal_id[i] - cat_z1_ids))
    sed3fit_ir_mass[id_index] = sed3fit_cat[0:,8][i]
    sed3fit_ir_sfr[id_index] = sed3fit_cat[0:,14][i] # update to SFR100 instead of SFR10
    sed3fit_ir_av[id_index] = sed3fit_cat[0:,16][i]
    sed3fit_ir_agnfracs[id_index] = sed3fit_cat[0:,18][i]


# plt.scatter(sed3fit_ir_mass, sed3fit_ir_sfr,c=sed3fit_ir_av,cmap='magma')
# plt.show()
