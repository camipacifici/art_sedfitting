import numpy as np
from astropy.io import fits
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

# what am I getting from each file? [specifically for mass]
#----------------------------------------------------------
# file: 'code_outputs/cigale_results_noAGN.txt'
# cigale_mass_small_noagn [small sample ~20 galaxies; deprecated]
# cigale_mass_z1_noagn [z=1 sample; deprecated]

# file: 'code_outputs/cigale_results_wAGN.txt'
# cigale_mass_small_wagn [small sample ~20 galaxies; deprecated]
# cigale_mass_z1_wagn [z=1 sample; deprecated]

# file: 'code_outputs/CIGALE_results_candels_goods-south_v0.fits'
# cigale_mass_z3 [z=3 sample; deprecated]

# new fits from Kasia:
# file: 'code_outputs_IR/cigale_noIR_noAGN_results.fits'
# cigale mass [z=1 sample; deprecated]
# cigale_ir_agn_mass [z=1 sample; deprecated]

# file: 'code_outputs/cigale_27feb_results_z3.dat'
# cigale_z3_noagn_mass [z=3 sample]

#---------------------------------------------------------------
# from import_IR_fits.py

# file: 'code_outputs_IR/cigale_new_noIR_withoutAGNs.fits'
# cigale_mass

# file: 'code_outputs_IR/cigale_new_withIR_withoutAGNs.fits'
# cigale_ir_mass

# file: 'code_outputs_IR/cigale_new_withIR_withAGNs.fits'
# cigale_ir_agn_mass

# now let's import the newest versions of everything..

#-------------------------------------------------------------------------
# z=1 sample, no IR, no AGN
#-------------------------------------------------------------------------

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


#-------------------------------------------------------------------------
# z=3 sample,
#-------------------------------------------------------------------------

cigale_z3_cat = np.genfromtxt('../code_outputs/cigale_27feb_results_z3.dat')

cigale_z3_noagn_ids = cigale_z3_cat[0:,0]

cigale_z3_noagn_mass = cigale_z3_cat[0:,1]
cigale_z3_noagn_sfr = cigale_z3_cat[0:,3]
cigale_z3_noagn_Av = cigale_z3_cat[0:,5]

cigale_z3_noagn_mass_err = cigale_z3_cat[0:,2]
cigale_z3_noagn_sfr_err = cigale_z3_cat[0:,4]
cigale_z3_noagn_Av_err = cigale_z3_cat[0:,6]


#---------------------------------------------------------------------------
# extra variables for backward compatibility with current code:
#---------------------------------------------------------------------------

# for the figure 5 notebook
#--------------------------
# the new errors are already in log space
cigale_mass_lo_z1_noagn = cigale_mass - cigale_mass_err
cigale_mass_hi_z1_noagn = cigale_mass + cigale_mass_err
cigale_sfr_lo_z1_noagn = cigale_sfr - cigale_sfr_err
cigale_sfr_hi_z1_noagn = cigale_sfr + cigale_sfr_err
# don't need to do it for Av because the notebook already does this.
