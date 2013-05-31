#MenuTitle: Show previous instance
# -*- coding: utf-8 -*-
"""Jumps to next instance shown in the preview field of the current Edit tab."""

import GlyphsApp

Doc = Glyphs.currentDocument
numberOfInstances = len( Glyphs.font.instances )

try:
	currentInstanceNumber = Doc.windowController().activeEditViewController().selectedInstance()
	
	if currentInstanceNumber > 1:
		Doc.windowController().activeEditViewController().setSelectedInstance_( currentInstanceNumber - 1 )
	else:
		Doc.windowController().activeEditViewController().setSelectedInstance_( numberOfInstances )
		
except Exception, e:
	print "Error:", e

