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
    par.Kcbini = 0.15
    par.Kcbmid = 1.20
    par.Kcbend = 0.573
    par.Lini = 15
    par.Ldev = 30
    par.Lmid = 20
    par.Lend = 20
    par.hini = 0.1
    par.hmax = 0.5
    par.thetaFC = 0.225
    par.thetaWP = 0.100
    par.theta0 = 0.100
    par.Zrini = 0.60
    par.Zrmax = 1.70
    par.pbase = 0.65
    par.Ze = 0.11429
    par.REW = 9.0
    par.savefile(os.path.join(module_dir,'btkdebasil2024.par'))
    par.loadfile(os.path.join(module_dir,'btkdebasil2024.par'))

    #Specify the weather data
    wth = fao.Weather(comment = '2024 basil')
    wth.loadfile(os.path.join(module_dir,'cotton2013.wth'))
    wth.savefile(os.path.join(module_dir,'cotton2013.wth'))
    wth.loadfile(os.path.join(module_dir,'cotton2013.wth'))

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
    irr.addevent(2013, 115, 33.0, 0.5)
    irr.savefile(os.path.join(module_dir,'cottondry2013.irr'))
    irr.loadfile(os.path.join(module_dir,'cottondry2013.irr'))

    #Run the model
    mdl = fao.Model('2013-113','2013-312', par, wth, irr=irr,
                    comment = '2024 basil')
    mdl.run()
    print(mdl)
    mdl.savefile(os.path.join(module_dir,'cottondry2013.out'))
    mdl.savesums(os.path.join(module_dir,'cottondry2013.sum'))

if __name__ == '__main__':
    run()
