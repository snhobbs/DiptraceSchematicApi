#edaClasses.py
from heodb import componentFactoryByPartNumber, printToScreen, sqlInterface, Component
import os, re, string
class EdaUserFields(object):
	def __init__(self):
		self.fieldIndex1 = '-1'
		self.fieldIndex2 = '-1'
		self.locked = '"N"'
		self.angle = '0'
		self.libPath = 0
		self.modelType = '0'
		self.modelString = '""'
		self.lockProperties = '"N"'

class EdaModelBody(object):
	def __init__(self):
		self.datasheet = '""'
		self.horzFlip = '"N"'
		self.vertFlip = '"N"'
		self.pageHiddenId = '0'
		self.manufacturer = ""

class EdaComponent(EdaUserFields, EdaModelBody):
	def __init__(self):
		EdaUserFields.__init__(self)
		EdaModelBody.__init__(self)
		self.showText = '0'#this is the reference designator, matches the number on the textlst in the gui
		self.textAlign = '0'
		self.allowParts = '"N"'
		self.showText2 = '4'#this is the text to show, 8 is the eoi part number, 4 is value
		self.textAlign2 = '0'
		self.showNumbers = '0'
		self.partNumber = '0'
		self.number1 = '0'
		self.number2 = '0'
		self.orientation = '0'
		self.number = '0'
		self.width = '22.86'
		self.height = '9'
		self.partNumber = '0'
		self.partType = '0'
		self.partName = '"Part 1"'
		self.partDescriptor = None
		self.textPosX = '0'
		self.textPosY = '0'
		self.textPosX2 = '0'
		self.textPosY2 = '0'
		self.partString = '""'


	def writeComponentHeading(self):
		return "  (Components\n"
	def writeComponentEnd(self):
		return  "  )"
	def writePart(self):
		strOut = []
		strOut.append('    (Part \"%s\" \"%s\"\n'%(self.packageName, self.ref_des))
		strOut.append("      (Enabled \"Y\")\n")
		strOut.append("      (Selected \"Y\")\n")
		strOut.append("      (Value \"%s\")\n"%(self.value))
		strOut.append("      (BaseName \"%s\")\n"%(self.packageName))
		strOut.append("      (BaseRefDes \"%s\")\n"%(self.ref_des[0]))
		strOut.append("      (X %s)\n"%(self.posX))
		strOut.append("      (Y %s)\n"%(self.posY))
		strOut.append("      (Type 0)\n")
		strOut.append("      (Number1 %s)\n"%(self.number1))
		strOut.append("      (Number2 %s)\n"%(self.number2))
		strOut.append("      (Page %s)\n"%(self.page))
		strOut.append("      (Orientation %s)\n"%(self.orientation))
		strOut.append("      (Group %s)\n"%(self.group))
		strOut.append("      (Number %s)\n"%(self.number))
		strOut.append("      (Width %s)\n"%(self.width))
		strOut.append("      (Height %s)\n"%(self.height))
		strOut.append("      (ShowText %s)\n"%(self.showText))
		strOut.append("      (TextAlign %s)\n"%(self.textAlign))
		strOut.append("      (PartNumber %s)\n"%(self.partNumber))
		strOut.append("      (PartType %s)\n"%(self.partType))
		strOut.append("      (PartName %s)\n"%(self.partName))
		strOut.append("      (PartDescriptor %s)\n"%(self.partDescriptor))
		strOut.append("      (AllowParts %s)\n"%(self.allowParts))
		strOut.append("      (ShowText2 %s)\n"%(self.showText2))
		strOut.append("      (TextAlign2 %s)\n"%(self.textAlign2))
		strOut.append("      (ShowNumbers %s)\n"%(self.showNumbers))
		strOut.append("      (TextPosX %s)\n"%(self.textPosX))
		strOut.append("      (TextPosY %s)\n"%(self.textPosY))
		strOut.append("      (TextPosX2 %s)\n"%(self.textPosX2))
		strOut.append("      (TextPosY2 %s)\n"%(self.textPosY2))
		strOut.append("      (PartString %s)\n"%(self.partString))
		strOut.append("      (HiddenId 1)\n")
		strOut.append("      (UserFields\n")
		strOut.append("        (UserField \"EOI Partnumber\" %s 0)\n"%(self.internalPartNumber))
		strOut.append("      )\n")
		strOut.append("      (FieldIndex1 %s)\n"%(self.fieldIndex1))
		strOut.append("      (FieldIndex2 %s)\n"%(self.fieldIndex2))
		strOut.append("      (Locked %s)\n"%(self.locked))
		strOut.append("      (Angle %s)\n"%(self.angle))
		strOut.append("      (LibPath %s)\n"%(self.libPath))
		strOut.append("      (ModelType %s)\n"%(self.modelType))
		strOut.append("      (ModelString %s)\n"%(self.modelString))
		strOut.append("      (LockProperties %s)\n"%(self.lockProperties))
		strOut.append("      (ModelBody\n")
		strOut.append("      )\n")
		strOut.append("      (Datasheet %s)\n"%(self.datasheet))
		strOut.append("      (HorzFlip %s)\n"%(self.horzFlip))
		strOut.append("      (VertFlip %s)\n"%(self.vertFlip))
		strOut.append("      (PageHiddenId 0)\n")
		strOut.append('      (Manufacturer "%s")\n'%(self.manufacturer))
		strOut.append('      (Component_CategoryName "")\n')
		strOut.append('      (Component_CategoryIndex 0 )\n')
		strOut.append("      (Component_CategoryTypes 0\n")
		strOut.append("      )\n")
		strOut.append("    )\n")
		return ''.join(strOut)

class HeaderSchematic(object):
	def __init__(self):
		self.pageNum = 0
		self.pageCount = 1
	def writeHeader(self):
		strHeader = []
		strHeader.append("""(Source \"DipTrace-Schematic\")
(Units \"in\")
(Scale 200%)
(Xpos 0)
(Ypos 0)
(Schematic
  (Pages""")

		while(self.pageNum <= self.pageCount):#self.pageNum is assigned by the derived class
			strHeader.append(self.makePageStr())
		strHeader.append('''  )
  (PictureCount 0)
  (ShowText 0)
  (TextAlign 0)
  (ShowText2 0)
  (TextAlign2 0)
  (HidePower "N")
  (OriginX 0)
  (OriginY 0)
  (FieldName1 "")
  (FieldName2 "")
  (PartFontVector "Y")
  (PartFontWidth -2)
  (PartFontScale 1)
  (NetClasses
    (NetClass "Default" 0 -1 -1 0 -1 30 6 6 30)
  )
  (DifferentialPairs
  )
''')
		return ''.join(strHeader)

	def readHeader(self):
		return 1

	def makePageStr(self):
		strPage  = ["\n    (Page \"Sheet {}\"".format(self.pageNum)]
		strPage.append('''
      (Zones "N")
      (PageWidth 891)
      (PageHeight 630)
      (HorzZones 4)
      (VertZones 4)
      (ZoneStandard 0)
      (ZoneFontName "Tahoma")
      (ZoneFontSize 10)
      (ZoneBorder "N")
      (HorzZoneBorder 15)
      (VertZoneBorder 15)
      (PageXPos 0)
      (PageyPos 0)
      (PageScale 2)
      (PageType 0)
      (PageHiddenId 0)
      (FLeft 60)
      (FTop 15)
      (FRight 15)
      (FBottom 15)
    )
''')
		self.pageNum += 1
		retStr =  ''.join(strPage)
		return retStr

class pages(object):
	def __init__(self,sheetNum):
		self.sheet = 0
		self.zones = '"N"'
		self.pageWidth = '891'
		self.pageHeight = '630'
		self.horzZones = '4'
		self.vertZones = '4'
		self.zoneStandard = '0'
		self.zoneFontName = '"Tahoma"'
		self.zoneFontSize = '10'
		self.zoneBorder = '"N"'
		self.horzZoneBorder = '15'
		self.vertZoneBorder = '15'
		self.pageXPos = '0'
		self.pageYPos = '0'
		self.pageScale = '2'
		self.pageType = '0'
		self.pageHiddenId = '0'
		self.fLeft = '60'
		self.fTop = '15'
		self.fRight = '15'
		self.fBottom = '15'

class SettingsSchematic(object):
	def __init__(self):
		return None
	def writeSettings(self):
		strSet = '''  (PageConnectors
  )
  (Shapes
  )
  (Nets
  )
  (Buses
  )
  (Groups
  )
  (Tables
  )
  (Settings
    (GridSize 3.81)
    (OriginEnabled "N")
    (clAxis 16711680)
    (BusConnectionFont 4)
    (PinNumberFont 4)
    (GridEnabled "Y")
    (DisplayTitles "N")
    (DisplaySheet "N")
    (BusConNetName "Y")
    (BusConNetNumber "N")
    (ShowPinNumbers "Y")
    (HidePinNumbers "N")
    (BusConAbove "Y")
    (BusConBelow "N")
    (BusLineWidth 2)
    (WireLineWidth 0.3)
    (TableLineWidth 1)
    (TitlesLineWidth 1)
    (NodeSize 3)
    (UnitsMM "N")
    (UnitsMIL "N")
    (UnitsINCH "Y")
    (ERC_PinType "Y")
    (ERC_NotConnected "N")
    (ERC_SinglePin "Y")
    (ERC_Short "N")
    (ERC_VCCTemplate "V*")
    (ERC_GNDTemplate "GND*")
    (ERC_PinSuperimpose "Y")
  )
  (ProjectLibs_Name "Project Libraries")
  (ProjectLibs_Type 2)
  (ProjectLibs_Content 0)
  (ProjectLibs_Folders 0
  )
  (ProjectLibs_Libs 0
  )
  (ProjectLibs_Sorted "N")
  (DesignCache_Count 0)
  (DesignCache_Links 200
  )
'''
		return strSet

class DipTraceSchematic(SettingsSchematic, HeaderSchematic, EdaComponent, sqlInterface):
	def __init__(self, db, bomIn = None):
		SettingsSchematic.__init__(self)
		HeaderSchematic.__init__(self)
		EdaComponent.__init__(self)
		self.db = db
		sqlInterface.__init__(self, db)
		self.bomIn = bomIn
		self.pageCount = max([ent[2] for ent in bomIn])

	def searchLib(self, libraryAsciiLocation):
		'''
		Search the library and make an array of the parts in it, return array
		'''
		parts = []
		with open(libraryAsciiLocation, 'r') as f:
			for line in f:
				match = re.search("\(Part \"*\"", line)
				if match is not None:
					parts.append(line.strip().split('(Part ')[1].split('"')[1].upper())					
		return parts

	def checkBaseCompNames(self, libraryAsciiLocation):
		outStr = ["The Following Part Numbers Do Not Have A Known Part In The Given Library:\n\n"]
		success = True
		libParts = self.searchLib(libraryAsciiLocation)
		for bomComp in self.bomIn:
			compObj = componentFactoryByPartNumber(self.db, bomComp[1] + '-00')
			compObj.loadPart()
			compObj.assignEDAComponent()
			partStr = compObj.EDA.base_comp_name.value.strip().upper()
			if( partStr not in libParts):
				outStr.append('{}) {} -> {}\n'.format(bomComp[0],compObj.part_number_short, partStr))
				success = False
		outStr.append("\nEnd of List. Re-export library to update library information")
		return [''.join(outStr), success]

	def makeLibPath(self, libName):
		return '"C:\HEO\MasterLibrary\{}"'.format(libName)

	def writeSchematic(self, fileName):
		with open(fileName, 'w') as f:
			f.write(self.writeHeader())
			f.write(self.writeComponentHeading())

			for ent in self.bomIn:

				compObj = componentFactoryByPartNumber(self.db, ent[1] + '-00')
				compObj.loadPart()
				partCount = int(compObj.ManuInfo.num_package.value)
				
				for i in range(1, partCount + 1):
					if partCount > 1:
						self.allowParts = '"Y"'
					else:
						self.allowParts = '"N"'
					compObj.assignEDAComponent()
					self.ref_des = ent[0]
					self.page = ent[2]
					self.group = ent[3]
					self.base_res_des = self.ref_des[0]
					self.posX = compObj.posX
					self.posY = compObj.posY
					self.internalPartNumber = compObj.part_number_short
					self.libPath = self.makeLibPath(compObj.EDA.lib_path.value)
					self.value = compObj.EDA.disp_text.value
					self.package_type = compObj.ManuInfo.package_type.value
					self.packageName = compObj.EDA.base_comp_name.value	
					self.partDescriptor = i
					self.partName = '"Part {}"'.format(i)
					self.partString = "{}{}".format(compObj.EDA.base_comp_name.value, i)
					f.write(self.writePart())
			f.write(self.writeComponentEnd())
			f.write(self.writeSettings())
		printToScreen("Schematic Saved To %s"%(fileName))


