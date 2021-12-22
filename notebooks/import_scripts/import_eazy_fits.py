from astropy.io import fits

import numpy as np
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False


fits_image_filename = '../code_outputs/CANDELS_GDSS_workshop_z1.eazypy.zout.fits'
hdul = fits.open(fits_image_filename)
if vb == True:
    print(hdul.info())
#print(hdul[1].header)

#hdul[1].header[0:]

#hdul.close()

temp = np.array(hdul[1].data)
if vb == True:
    print(temp.shape)

eazy_id_z1 = np.zeros((len(temp)))
eazy_zphot_z1 = np.zeros((len(temp)))
eazy_mass_z1 = np.zeros((len(temp)))
eazy_sfr_z1 = np.zeros((len(temp)))
eazy_Av_z1 = np.zeros((len(temp)))
for i in range(len(temp)):
    eazy_id_z1[i] = temp[i][1]
    eazy_zphot_z1[i] = temp[i][4]
    eazy_mass_z1[i] = np.log10(temp[i][27])
    eazy_sfr_z1[i] = np.log10(temp[i][28])
    eazy_Av_z1[i] = (temp[i][26])

if vb == True:
    plt.scatter(eazy_mass_z1,eazy_sfr_z1,c=eazy_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


#print(hdul[1].header[0:])

hdul.close()

#plt.hist(eazy_mass)
#plt.show()



#---------------------------small--------------------

fits_image_filename = '../code_outputs/CANDELS_GDSS_workshop.eazypy.zout.fits'
hdul = fits.open(fits_image_filename)
#hdul.info()
#print(hdul[1].header)

#hdul[1].header[0:]



#hdul.close()

temp = np.array(hdul[1].data)
#print(temp.shape)

eazy_id_small = np.zeros((len(temp)))
eazy_zphot_small = np.zeros((len(temp)))
eazy_mass_small = np.zeros((len(temp)))
eazy_sfr_small = np.zeros((len(temp)))
eazy_Av_small = np.zeros((len(temp)))
for i in range(len(temp)):
    eazy_id_small[i] = temp[i][0]
    eazy_zphot_small[i] = temp[i][4]
    eazy_mass_small[i] = np.log10(temp[i][27])
    eazy_sfr_small[i] = np.log10(temp[i][28])
    eazy_Av_small[i] = (temp[i][26])

if vb == True:
    plt.scatter(eazy_mass_small,eazy_sfr_small,c=eazy_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

hdul[1].header[0:]
hdul.close()

print('imported eazy fits.')
