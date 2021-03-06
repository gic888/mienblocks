#!/usr/bin/env python
# encoding: utf-8
#Created by gic on 2007-04-11.

# Copyright (C) 2007 Graham I Cummins
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
#

from mien.nmpml.basic_tools import NmpmlObject

class MpiGate(NmpmlObject):
	'''Class describing channels with fixed or state dependant
	(not event triggered) conductance. Allways
	a child of "Section" (or equivalent).

	Attributes:

	Ion: A single ion name, or the string "Leak". (Future: Implement sets
	     of Ions)

	Density: Comma seperated list of floats

	Units: Usually units for channel density are in mhos/centimeter**2.

	Name : Name of the channel. Should corespond to the name of a modl
	       mechanism if Neuron is used for simulation.

	VarName:

	Reversal:
'''
	_allowedChildren =["Comments","Parameters"]
	_requiredAttributes = ["Name"]
	_specialAttributes = ['Ion', 'Density', 'VarName','Reversal' ]

