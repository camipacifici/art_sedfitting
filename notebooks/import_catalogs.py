
"""
This file contains functions to read the data catalogs

"""

import numpy as np

def get_cat():

    # SEDs in magnitudes
    candels_cat_small = np.loadtxt('../catalogs/CANDELS_GDSS_workshop.dat')

    # subtracting 1 from the ID for python indexing
    cat_small_ids = candels_cat_small[0:,0] - 1
    cat_small_z = candels_cat_small[0:,1]

    #print(str(cat_small_z.shape[0])+' galaxies in the small catalog.')

    #------------------------------------------------------------------------------

    candels_cat_z1 = np.loadtxt('../catalogs/CANDELS_GDSS_workshop_z1.dat')

    # subtracting 1 from the ID for python indexing
    cat_z1_ids = candels_cat_z1[0:,0] - 1
    cat_z1_z = candels_cat_z1[0:,1]
    #print(str(cat_z1_z.shape[0])+' galaxies in the z~1 catalog.')

    #------------------------------------------------------------------------------

    candels_cat_z3 = np.loadtxt('../catalogs/CANDELS_GDSS_workshop_z3.dat')

    # subtracting 1 from the ID for python indexing
    cat_z3_ids = candels_cat_z3[0:,0] - 1
    cat_z3_z = candels_cat_z3[0:,1]

    #print(str(cat_z3_z.shape[0])+' galaxies in the z~3 catalog.')

    z1flag_cat = np.genfromtxt('../catalogs/flags_z1.dat')
    z1flag_ids = z1flag_cat[0:,0]

    z1_mask = np.zeros_like(cat_z1_ids)
    for i in range(len(z1flag_ids)):
        z1_mask[cat_z1_ids == z1flag_ids[i]-1 ] = 1

    z3flag_cat = np.genfromtxt('../catalogs/flags_z3.dat')
    z3flag_ids = z3flag_cat[0:,0]

    z3_mask = np.zeros_like(cat_z3_ids)
    for i in range(len(z3flag_ids)):
        z3_mask[cat_z3_ids == z3flag_ids[i]-1 ] = 1

    return cat_small_ids, cat_z1_ids, cat_z3_ids


def get_cat_z():

    # SEDs in magnitudes
    candels_cat_small = np.loadtxt('../catalogs/CANDELS_GDSS_workshop.dat')

    # subtracting 1 from the ID for python indexing
    cat_small_ids = candels_cat_small[0:,0] - 1
    cat_small_z = candels_cat_small[0:,1]

    #print(str(cat_small_z.shape[0])+' galaxies in the small catalog.')

    #------------------------------------------------------------------------------

    candels_cat_z1 = np.loadtxt('../catalogs/CANDELS_GDSS_workshop_z1.dat')

    # subtracting 1 from the ID for python indexing
    cat_z1_ids = candels_cat_z1[0:,0] - 1
    cat_z1_z = candels_cat_z1[0:,1]
    #print(str(cat_z1_z.shape[0])+' galaxies in the z~1 catalog.')

    #------------------------------------------------------------------------------

    candels_cat_z3 = np.loadtxt('../catalogs/CANDELS_GDSS_workshop_z3.dat')

    # subtracting 1 from the ID for python indexing
    cat_z3_ids = candels_cat_z3[0:,0] - 1
    cat_z3_z = candels_cat_z3[0:,1]

    #print(str(cat_z3_z.shape[0])+' galaxies in the z~3 catalog.')

    z1flag_cat = np.genfromtxt('../catalogs/flags_z1.dat')
    z1flag_ids = z1flag_cat[0:,0]

    z1_mask = np.zeros_like(cat_z1_ids)
    for i in range(len(z1flag_ids)):
        z1_mask[cat_z1_ids == z1flag_ids[i]-1 ] = 1

    z3flag_cat = np.genfromtxt('../catalogs/flags_z3.dat')
    z3flag_ids = z3flag_cat[0:,0]

    z3_mask = np.zeros_like(cat_z3_ids)
    for i in range(len(z3flag_ids)):
        z3_mask[cat_z3_ids == z3flag_ids[i]-1 ] = 1

    return cat_small_z, cat_z1_z, cat_z3_z
