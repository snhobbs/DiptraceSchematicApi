# DiptraceSchematicApi
An API for the placement of parts into a diptrace schematic using the ascii import function. This is a python3 project generalizing the tool developed for the Hobbs ElectroOptics database system. This allows for the pulling of parts from an existing Diptrace library and the auto generation of a schematic with the part data pulled from a database.

In the Hobbs ElectroOptics database, this is used so that all useful values are automatically filled in for the parts from a design bill of materials (BOM). When a design is complete, the design BOM can be compared with a script to ensure there were no errors during schematic capture and layout.

There is no scripting interface to Diptrace to date so this functionality is done through the ascii schematic import. Parts with no pattern are loaded automaically and the the CAD user loads the parts from the given library for the proper part to show up. 
