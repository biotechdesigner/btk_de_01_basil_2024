"""
########################################################################
The btkdebasil2024.py module contains a function to setup and run pyfao56
for the treatment in a 2024 basil greenhouse study at
Hohenheim, Germany.  The savefile and loadfile routines for Parameters,
Weather, and Irrigation classes are also tested.

The btkdebasil2024.py module contains the following:
    run - function to setup and run pyfao56 for the
    treatment in a 2024 basil greenhouse study at Hohenheim, Germany

03/11/2024 Scripts developed for running pyfao56 for 2024 basil data
########################################################################
"""

import pyfao56 as fao
import os

def run():
    """Setup and run pyfao56 for a 2024 basil greenhouse study"""

    #Get the module directory
    module_dir = os.path.dirname(os.path.abspath(__file__))

    #Specify the model parameters
    par = fao.Parameters(comment = '2024 Basil')
    par.Kcbini = 0.40 #mint parameters 
    par.Kcbmid = 1.10 #mint parameters 
    par.Kcbend = 1.05 #mint parameters 
    par.Lini = 15 #based on literature for basil plant development
    par.Ldev = 30 #based on literature for basil plant development
    par.Lmid = 20 #based on literature for basil plant development
    par.Lend = 20 #based on literature for basil plant development
    par.hini = 0.1 #height initial of 1 cm because it started with seeds
    par.hmax = 0.8 
    par.thetaFC = 0.14 #Vol. Soil Water Content, Field Capacity (FAO-56, table 19, loamy sand substrat 5)
    par.thetaWP = 0.060 #Vol. Soil Water Content, Wilting point (FAO-56, table 19, loamy sand substrat 5)
    par.theta0 = 0.000 #Initial volume soil water content
    par.Zrini = 0.05 #Initial root depth, 0m because its seeds
    par.Zrmax = 0.0850 # maximum root depth (m), 8.5 cm because of the pot height
    par.pbase = 0.40
    par.Ze = 0.1143
    par.REW = 8.0
    par.savefile(os.path.join(module_dir,'btkdebasil2024.par'))
    par.loadfile(os.path.join(module_dir,'btkdebasil2024.par'))

    #Specify the weather data
    wth = fao.Weather(comment = '2024 basil')
    wth.loadfile(os.path.join(module_dir,'transformed_weather_data.wth'))
    wth.savefile(os.path.join(module_dir,'transformed_weather_data.wth'))
    wth.loadfile(os.path.join(module_dir,'transformed_weather_data.wth'))

    #Specify the irrigation schedule
    """
    Atributes
    -------
        index - Year and day of year as string ('yyyy-ddd')
        columns - ['Depth','fw']
            Depth - Irrigation depth (mm)
            fw - fraction of soil surface wetted (FAO-56 Table 20)
            
    Methods
    -------
    savefile(filepath='pyfao56.irr')
        Save irrigation data to a file
    loadfile(filepath='pyfao56.irr')
        Load irrigation data from a file
    addevent(year,doy,depth,fw)
        Add an irrigation event to self.idata
    customload()
        Users can override for custom loading of irrigation data.
    """
    irr = fao.Irrigation(comment = '2024 basil')
    #irr.addevent(2024, 80, 30, 0.30)
    irr.savefile(os.path.join(module_dir,'btkdebasil2024.irr'))
    irr.loadfile(os.path.join(module_dir,'btkdebasil2024.irr'))

    #Run the model
    mdl = fao.Model('2024-077','2024-098', par, wth, irr=irr, aq_Ks=True,
                    comment = '2024 basil previous test')
    mdl.run()
    print(mdl)
    mdl.savefile(os.path.join(module_dir,'btkdebasil2024.out'))
    mdl.savesums(os.path.join(module_dir,'btkdebasil2024.sum'))

if __name__ == '__main__':
    run()
