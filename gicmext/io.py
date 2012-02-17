#!/usr/bin/env python
# encoding: utf-8
#Created by  on 2008-04-11.

# Copyright (C) 2008 Graham I Cummins
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

from mien.datafiles.dataset import *
import wave, os
from mien.math.array import ravel, Int16
from wx import Sound

def _array2wav(a, sampr, filename):
	wav=wave.open(filename, "w")
	wav.setparams((a.shape[1],2, sampr, a.shape[0], 'NONE', 'not compressed'))
	scalefac=max(50, max(abs(ravel(a))))
	a=(a/scalefac)*32767
	a=a.astype(Int16)
	wav.writeframes(a.tostring())
	wav.close()

def _playArray(a, sampr):
	_array2wav(a, sampr, '__temp.wav')
	s=Sound("__temp.wav")
	s.Play()
	os.unlink('__temp.wav')
 
def playAudio(ds, select=(None, [0], None)):
	dat=getSelection(ds, select)
	sampr=getSelectionHeader(ds, select)['SamplesPerSecond']
	_playArray(dat, sampr)