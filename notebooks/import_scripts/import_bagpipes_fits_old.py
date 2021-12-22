
import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False

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


bagpipes_cat_z1 = np.genfromtxt('../code_outputs/bagpipes_z1_cat_pipes_output.txt')
if vb == True:
    print(bagpipes_cat_z1.shape)

bagpipes_id = bagpipes_cat_z1[0:,0]

bagpipes_Av_lo_z1= bagpipes_cat_z1[0:,1]
bagpipes_Av_z1 = bagpipes_cat_z1[0:,2]
bagpipes_Av_hi_z1 = bagpipes_cat_z1[0:,3]

bagpipes_mass_lo_z1 = np.log10(bagpipes_cat_z1[0:,34])
bagpipes_mass_z1 = np.log10(bagpipes_cat_z1[0:,35])
bagpipes_mass_hi_z1 = np.log10(bagpipes_cat_z1[0:,36])

bagpipes_sfr_lo_z1 = np.log10(bagpipes_cat_z1[0:,31])
bagpipes_sfr_z1 = np.log10(bagpipes_cat_z1[0:,32])
bagpipes_sfr_hi_z1 = np.log10(bagpipes_cat_z1[0:,33])

# ID
#dust:Av_16 dust:Av_median dust:Av_84
#dblplaw:tau_16 dblplaw:tau_median dblplaw:tau_84
#dblplaw:metallicity_16 dblplaw:metallicity_median dblplaw:metallicity_84
#dblplaw:beta_16 dblplaw:beta_median dblplaw:beta_84
#dblplaw:massformed_16 dblplaw:massformed_median dblplaw:massformed_84
#dblplaw:alpha_16 dblplaw:alpha_median dblplaw:alpha_84
#UVcolour_16 UVcolour_median UVcolour_84 VJcolour_16 VJcolour_median VJcolour_84
#tmw_16 tmw_median tmw_84
#sfr_16 sfr_median sfr_84
#mstar_liv_16 mstar_liv_median mstar_liv_84
#z_input log_evidence log_evidence_err min_chisq_reduced


bagpipes_cat_z3 = np.genfromtxt('../code_outputs/bagpipes_ucr_z3_results.cat')
if vb == True:
    print(bagpipes_cat_z3.shape)

bagpipes_id = bagpipes_cat_z3[0:,0]

bagpipes_Av_lo_z3= bagpipes_cat_z3[0:,1]
bagpipes_Av_z3 = bagpipes_cat_z3[0:,2]
bagpipes_Av_hi_z3 = bagpipes_cat_z3[0:,3]

bagpipes_mass_lo_z3 = np.log10(bagpipes_cat_z3[0:,31])
bagpipes_mass_z3 = np.log10(bagpipes_cat_z3[0:,32])
bagpipes_mass_hi_z3 = np.log10(bagpipes_cat_z3[0:,33])

bagpipes_sfr_lo_z3 = np.log10(bagpipes_cat_z3[0:,28])
bagpipes_sfr_z3 = np.log10(bagpipes_cat_z3[0:,29])
bagpipes_sfr_hi_z3 = np.log10(bagpipes_cat_z3[0:,30])

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
