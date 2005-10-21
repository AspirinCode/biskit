##
## Biskit, a toolkit for the manipulation of macromolecular structures
## Copyright (C) 2004-2005 Raik Gruenberg & Johan Leckner; All rights reserved
##
## Default parameters for Biskit.Dock.settings
##
## last $Author$
## last $Date$
## $Revision$

"""
Defines the options exported by Biskit.Dock.settings and 
provides fall-back values for options that are not found in
.biskit/settings.dat.

This is NOT the place where you adapt biskit to the local environment!
Local settings belong into .biskit/settings.dat which is then parsed by
Biskit/settings.py. 

Nevertheless, this IS the place where you define new parameters for
Biskit.Dock. These parameters become then (semi-magically) available as static
fields of Biskit.Dock.settings. Dock.settings.py is importing the content of
this module.
For each field found here, it expects an option in .biskit/settings.dat
under the given section. If such an option (or .biskit/settings.dat) is not
found, the default parameter is taken (or None) and a Warning is issued.

Each parameter is defined by a tuple containing
  (1) the default value for a parameter of this name in settings.py
  (2) the section into which this parameter is put within .biskit/settings.dat
  (3) an optional comment (which also ends up in .biskit/settings.dat)

Note: Keep execution time of this module to a minimum! It always needs to
be imported at the beginning of a Biskit.Dock session. That means, stay away
from file searching or similar things.
"""

import os as __os
import user as __user
import Biskit.tools as __T

## cache for speed
__root = __T.projectRoot()

#################################################
## Parameters expected in .biskit/settings.dat ##

## section DOCK_BIN
s = 'dock_bin'

hex_bin           = 'hex', s, 'HEX: http://www.csd.abdn.ac.uk/hex/'


#############################
## clean up module content ##

del s, __root, __os, __T, __user
