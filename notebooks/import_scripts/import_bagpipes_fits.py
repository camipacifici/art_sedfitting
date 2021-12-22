
import numpy as np
from astropy.table import Table
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

#-----small-----

bagpipes_cat_small = np.genfromtxt('../code_outputs/bagpipes_first_cat_pipes_output.txt')
if vb == True:
    print(bagpipes_cat_small.shape)

bagpipes_id = bagpipes_cat_small[0:,0]

bagpipes_Av_lo_small= bagpipes_cat_small[0:,1]
bagpipes_Av_small = bagpipes_cat_small[0:,2]
bagpipes_Av_hi_small = bagpipes_cat_small[0:,3]

bagpipes_mass_lo_small = np.log10(bagpipes_cat_small[0:,34])
bagpipes_mass_small = np.log10(bagpipes_cat_small[0:,35])
bagpipes_mass_hi_small = np.log10(bagpipes_cat_small[0:,36])

bagpipes_sfr_lo_small = np.log10(bagpipes_cat_small[0:,31])
bagpipes_sfr_small = np.log10(bagpipes_cat_small[0:,32])
bagpipes_sfr_hi_small = np.log10(bagpipes_cat_small[0:,33])

# ID dust:Av_16 dust:Av_median dust:Av_84
#dblplaw:tau_16 dblplaw:tau_median dblplaw:tau_84
#dblplaw:beta_16 dblplaw:beta_median dblplaw:beta_84
#dblplaw:metallicity_16 dblplaw:metallicity_median dblplaw:metallicity_84
#dblplaw:massformed_16 dblplaw:massformed_median dblplaw:massformed_84
#dblplaw:alpha_16 dblplaw:alpha_median dblplaw:alpha_84
#redshift_16 redshift_median redshift_84
#UVcolour_16 UVcolour_median UVcolour_84
#VJcolour_16 VJcolour_median VJcolour_84
#tmw_16 tmw_median tmw_84
#sfr_16 sfr_median sfr_84
#mstar_liv_16 mstar_liv_median mstar_liv_84
#z_input global_log_evidence global_log_evidence_err min_chisq_reduced

#--------z1-------

#ID
#dblplaw:alpha_16	dblplaw:alpha_50	dblplaw:alpha_84	3
#dblplaw:beta_16	dblplaw:beta_50	dblplaw:beta_84	6
#dblplaw:massformed_16	dblplaw:massformed_50	dblplaw:massformed_84	9
#dblplaw:metallicity_16	dblplaw:metallicity_50	dblplaw:metallicity_84	12
#dblplaw:tau_16	dblplaw:tau_50	dblplaw:tau_84	15
#dust:Av_16	dust:Av_50	dust:Av_84	18
#stellar_mass_16	stellar_mass_50	stellar_mass_84	21
#formed_mass_16	formed_mass_50	formed_mass_84
#sfr_16	sfr_50	sfr_84
#ssfr_16	ssfr_50	ssfr_84
#nsfr_16	nsfr_50	nsfr_84
#mass_weighted_age_16	mass_weighted_age_50	mass_weighted_age_84
#tform_16	tform_50	tform_84
#tquench_16	tquench_50	tquench_84
#input_redshift	log_evidence	log_evidence_err

bagpipes_cat_z1 = Table.read('../code_outputs/bagpipes_11_3_19_z1_noir.cat', format = 'ascii.commented_header')
if vb == True:
    print(len(bagpipes_cat_z1))
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

#-----z3------

bagpipes_cat_z3 = Table.read('../code_outputs/bagpipes_11_3_19_z3_noir.cat', format = 'ascii.commented_header')
if vb == True:
    print(len(bagpipes_cat_z3))
bagpipes_cat_z3.sort('ID')

bagpipes_id = bagpipes_cat_z3['ID']

bagpipes_Av_lo_z3= bagpipes_cat_z3['dust:Av_16']
bagpipes_Av_z3 = bagpipes_cat_z3['dust:Av_50']
bagpipes_Av_hi_z3 = bagpipes_cat_z3['dust:Av_84']

bagpipes_mass_lo_z3 = bagpipes_cat_z3['stellar_mass_16']
bagpipes_mass_z3 = bagpipes_cat_z3['stellar_mass_50']
bagpipes_mass_hi_z3 = bagpipes_cat_z3['stellar_mass_84']

bagpipes_sfr_lo_z3 = np.log10(bagpipes_cat_z3['sfr_16'])
bagpipes_sfr_z3 = np.log10(bagpipes_cat_z3['sfr_50'])
bagpipes_sfr_hi_z3 = np.log10(bagpipes_cat_z3['sfr_84'])


#---------------plot SFR-M* diagrams as a consistency check

if vb == True:
    plt.scatter(bagpipes_mass_small,bagpipes_sfr_small,c = bagpipes_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(bagpipes_mass_z1,bagpipes_sfr_z1,c = bagpipes_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


    plt.scatter(bagpipes_mass_z3,bagpipes_sfr_z3,c = bagpipes_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported bagpipes fits.')
