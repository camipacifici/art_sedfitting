import numpy as np
from astropy.io import fits
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

#------------------small------------------
# need to add dust from beagle_dust_attenuation_format.dat

beagle_cat = np.genfromtxt('../code_outputs/beagle_galaxy_properties_format.dat')
if vb == True:
    print(beagle_cat.shape)

#ID
#M_tot_mean     M_tot_median   M_tot_16	M_tot_84	      M_tot_3     M_tot_97
#M_star_mean    M_star_median  M_star_16	M_star_84	     M_star_3	M_star_97
#mass_w_age_mean   mass_w_age_median   mass_w_age_16    mass_w_age_84		   mass_w_age_3	    mass_w_age_97
#mass_w_Z_mean   mass_w_Z_median   mass_w_Z_16	    mass_w_Z_84	   mass_w_Z_3   mass_w_Z_97
#N_ion_mean   N_ion_median   N_ion_16    N_ion_84	       N_ion_3    N_ion_97
#xi_ion_mean   xi_ion_median   xi_ion_16	    xi_ion_84       xi_ion_3     xi_ion_97
#xi_ion_unatt_mean   xi_ion_unatt_median   xi_ion_unatt_16     xi_ion_unatt_84	   xi_ion_unatt_3     xi_ion_unatt_97
#xi_ion_unatt_stellar_mean   xi_ion_unatt_stellar_median   xi_ion_unatt_stellar_16     xi_ion_unatt_stellar_84   xi_ion_unatt_stellar_3     xi_ion_unatt_stellar_97
#UV_slope_mean   UV_slope_median   UV_slope_16    UV_slope_84	       UV_slope_3    UV_slope_97

beagle_cat_sf = np.genfromtxt('../code_outputs/beagle_star_formation_format.dat')

# ID
#sSFR_mean    sSFR_median   sSFR_16  sSFR_84               sSFR_3   sSFR_97
#SFR_10_mean    SFR_10_median   SFR_10_16   SFR_10_84                SFR_10_3   SFR_10_97
#SFR_100_mean   SFR_100_median   SFR_100_16    SFR_100_84              SFR_100_3      SFR_100_97
#max_stellar_age_mean   max_stellar_age_median   max_stellar_age_16  max_stellar_age_84        max_stellar_age_3  max_stellar_age_97

beagle_ID = beagle_cat[0:,0]
beagle_mass_small = np.log10(beagle_cat[0:,8])
beagle_mass_lo_small = np.log10(beagle_cat[0:,9])
beagle_mass_hi_small = np.log10(beagle_cat[0:,10])


beagle_sfr_small = np.log10(beagle_cat_sf[0:,7])
beagle_sfr_lo_small = np.log10(beagle_cat_sf[0:,8])
beagle_sfr_hi_small = np.log10(beagle_cat_sf[0:,9])

if vb == True:
    plt.hist(beagle_mass_small)
    plt.show()

    plt.scatter(beagle_mass_small,beagle_sfr_small)
    plt.show()


# the beagle output isn't sorted by galaxy ID, so I'm doing this to fix it

beagle_mass_small_sorted = [beagle_mass_small for (beagle_ID,beagle_mass_small) in sorted(zip(beagle_ID,beagle_mass_small), key=lambda pair: pair[0])]
beagle_mass_lo_small_sorted = [beagle_mass_lo_small for (beagle_ID,beagle_mass_lo_small) in sorted(zip(beagle_ID,beagle_mass_lo_small), key=lambda pair: pair[0])]
beagle_mass_hi_small_sorted = [beagle_mass_hi_small for (beagle_ID,beagle_mass_hi_small) in sorted(zip(beagle_ID,beagle_mass_hi_small), key=lambda pair: pair[0])]

beagle_sfr_small_sorted = [beagle_sfr_small for (beagle_ID,beagle_sfr_small) in sorted(zip(beagle_ID,beagle_sfr_small), key=lambda pair: pair[0])]
beagle_sfr_lo_small_sorted = [beagle_sfr_lo_small for (beagle_ID,beagle_sfr_lo_small) in sorted(zip(beagle_ID,beagle_sfr_lo_small), key=lambda pair: pair[0])]
beagle_sfr_hi_small_sorted = [beagle_sfr_hi_small for (beagle_ID,beagle_sfr_hi_small) in sorted(zip(beagle_ID,beagle_sfr_hi_small), key=lambda pair: pair[0])]

##########------------z1--------------------

beagle_z1_cat = fits.open('../code_outputs/BEAGLE_summary_catalogue_z1.fits')
if vb == True:
    print(beagle_z1_cat.info())

galprop = beagle_z1_cat[1]
sf = beagle_z1_cat[2]
dust = beagle_z1_cat[3]

if vb == True:
    print(dust.header)

beagle_ids = galprop.data['ID      ']
beagle_ids_int = [int(beagle_ids[i]) for i in range(len(beagle_ids))]

mstar = np.log10(galprop.data['M_star_median'])
mstar_68 = np.log10(galprop.data['M_star_68.00'])

sfr = np.log10(sf.data['SFR_100_median'])
sfr_68 = np.log10(sf.data['SFR_100_68.00'])

A1500 = dust.data['A_V_median']
A1500_68 = dust.data['A_V_68.00']

beagle_z1_cat.close()

beagle_mass_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_mass_lo_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_mass_hi_z1 = np.zeros_like(cat_z1_ids)*np.nan

beagle_sfr_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_sfr_lo_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_sfr_hi_z1 = np.zeros_like(cat_z1_ids)*np.nan

beagle_Av_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_Av_lo_z1 = np.zeros_like(cat_z1_ids)*np.nan
beagle_Av_hi_z1 = np.zeros_like(cat_z1_ids)*np.nan

for i in range(len(cat_z1_ids)):

    if np.sum(beagle_ids_int == cat_z1_ids[i]+1) == 1:

        beagle_mass_z1[i] = mstar[beagle_ids_int == cat_z1_ids[i]+1]

        beagle_mass_lo_z1[i] = mstar_68[beagle_ids_int == cat_z1_ids[i]+1, 0]
        beagle_mass_hi_z1[i] = mstar_68[beagle_ids_int == cat_z1_ids[i]+1, 1]

        beagle_sfr_z1[i] = sfr[beagle_ids_int == cat_z1_ids[i]+1]
        beagle_sfr_lo_z1[i] = sfr_68[beagle_ids_int == cat_z1_ids[i]+1, 0]
        beagle_sfr_hi_z1[i] = sfr_68[beagle_ids_int == cat_z1_ids[i]+1, 1]

        # currently putting these values in as a placeholder, need to use the correct conversion

        beagle_Av_z1[i] = A1500[beagle_ids_int == cat_z1_ids[i]+1]
        beagle_Av_lo_z1[i] = A1500_68[beagle_ids_int == cat_z1_ids[i]+1, 0]
        beagle_Av_hi_z1[i] = A1500_68[beagle_ids_int == cat_z1_ids[i]+1, 1]

if vb == True:
    plt.scatter(beagle_mass_z1, beagle_sfr_z1, c = beagle_Av_z1)
    plt.colorbar()
    plt.show()

######----------------z3-------------------------

beagle_z3_cat = fits.open('../code_outputs/BEAGLE_summary_catalogue_z3.fits')
if vb == True:
    print(beagle_z3_cat.info())

galprop = beagle_z3_cat[1]
sf = beagle_z3_cat[2]
dust = beagle_z3_cat[3]

#print(dust.header)

beagle_ids = galprop.data['ID      ']
beagle_ids_int = [int(beagle_ids[i]) for i in range(len(beagle_ids))]
if vb == True:
    print(beagle_ids.shape)

mstar = np.log10(galprop.data['M_star_median'])
mstar_68 = np.log10(galprop.data['M_star_68.00'])

sfr = np.log10(sf.data['SFR_100_median'])
sfr_68 = np.log10(sf.data['SFR_100_68.00'])

A1500 = dust.data['A_V_median']
A1500_68 = dust.data['A_V_68.00']

beagle_z3_cat.close()

beagle_mass_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_mass_lo_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_mass_hi_z3 = np.zeros_like(cat_z3_ids)*np.nan

beagle_sfr_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_sfr_lo_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_sfr_hi_z3 = np.zeros_like(cat_z3_ids)*np.nan

beagle_Av_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_Av_lo_z3 = np.zeros_like(cat_z3_ids)*np.nan
beagle_Av_hi_z3 = np.zeros_like(cat_z3_ids)*np.nan

for i in range(len(cat_z3_ids)):

    if np.sum(beagle_ids_int == cat_z3_ids[i]+1) == 1:

        beagle_mass_z3[i] = mstar[beagle_ids_int == cat_z3_ids[i]+1]

        beagle_mass_lo_z3[i] = mstar_68[beagle_ids_int == cat_z3_ids[i]+1, 0]
        beagle_mass_hi_z3[i] = mstar_68[beagle_ids_int == cat_z3_ids[i]+1, 1]

        beagle_sfr_z3[i] = sfr[beagle_ids_int == cat_z3_ids[i]+1]
        beagle_sfr_lo_z3[i] = sfr_68[beagle_ids_int == cat_z3_ids[i]+1, 0]
        beagle_sfr_hi_z3[i] = sfr_68[beagle_ids_int == cat_z3_ids[i]+1, 1]

        # currently putting these values in as a placeholder, need to use the correct conversion

        beagle_Av_z3[i] = A1500[beagle_ids_int == cat_z3_ids[i]+1]
        beagle_Av_lo_z3[i] = A1500_68[beagle_ids_int == cat_z3_ids[i]+1, 0]
        beagle_Av_hi_z3[i] = A1500_68[beagle_ids_int == cat_z3_ids[i]+1, 1]

if vb == True:
    plt.scatter(beagle_mass_z3, beagle_sfr_z3, c = beagle_Av_z3)
    plt.colorbar()
    plt.show()

print('imported beagle fits.')
