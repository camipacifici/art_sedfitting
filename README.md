# The Art of Measuring Physical Parameters in Galaxies: A Critical Assessment of Spectral Energy Distribution Fitting Techniques
This repository contains the catalogs and codes used to create the figures of the paper "The Art of Measuring Physical Parameters in Galaxies: A Critical Assessment of Spectral Energy Distribution Fitting Techniques" (Pacifici et al. 2022). This paper is the result of the SED fitting comparison done during the CANDELS workshop in Riverside in April 2018. During the workshop, builders or users of fourteen different SED fitting tools ran their codes on the same photometric catalogs.

Content of this repository:
- catalogs: it includes four photometric catalogs (CANDELS_GDSS_workshop.dat, CANDELS_GDSS_workshop_z1.dat, CANDELS_GDSS_workshop_z1_fluxes_Jy_UVtoIR.dat, CANDELS_GDSS_workshop_z3.dat) and flags to the z=1 and z=3 catalogs.
- code_outputs: it includes fits or ascii files generated by the various codes when fitting the UV-optical-NIR photometry.
- code_outputs_IR: it includes fits or ascii files generated by the various codes when fitting the UV-optical-IR photometry.
- filters: it includes the filter curves of the UV-optical-NIR bands
- notebooks: it includes thirteen Jupyter Notebooks used to generate the figures in the paper; it includes also the script called by these notebooks to read the code outputs.
- templates: it includes one ascii file with one model template used in figure one.

Feel free to grab the catalogs and ran them through your favorite SED fitting tools. I will be curious to see how your results compare with what is presented in the paper! You can contact me at cpacifici@stsci.edu or submitting an issue to this repository.
