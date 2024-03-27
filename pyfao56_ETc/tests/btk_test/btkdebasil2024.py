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
    par.Kcbini = 0.40
    par.Kcbmid = 1.10
    par.Kcbend = 1.05
    par.Lini = 15
    par.Ldev = 30
    par.Lmid = 20
    par.Lend = 20
    par.hini = 0.1
    par.hmax = 0.8
    par.thetaFC = 0.14
    par.thetaWP = 0.060
    par.theta0 = 0.100
    par.Zrini = 0.25
    par.Zrmax = 0.80
    par.pbase = 0.40
    par.Ze = 0.1143
    par.REW = 8.0
    par.savefile(os.path.join(module_dir,'btkdebasil2024.par'))
    par.loadfile(os.path.join(module_dir,'btkdebasil2024.par'))

    #Specify the weather data
    wth = fao.Weather(comment = '2024 basil')
    wth.loadfile(os.path.join(module_dir,'btkdebasil2024.wth'))
    wth.savefile(os.path.join(module_dir,'btkdebasil2024.wth'))
    wth.loadfile(os.path.join(module_dir,'btkdebasil2024.wth'))

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
    irr.savefile(os.path.join(module_dir,'btkdebasil2024.irr'))
    irr.loadfile(os.path.join(module_dir,'btkdebasil2024.irr'))

    #Run the model
    mdl = fao.Model('2024-077','2024-086', par, wth, irr=irr,
                    comment = '2024 basil previous test')
    mdl.run()
    print(mdl)
    mdl.savefile(os.path.join(module_dir,'btkdebasil2024.out'))
    mdl.savesums(os.path.join(module_dir,'btkdebasil2024.sum'))

if __name__ == '__main__':
    run()
