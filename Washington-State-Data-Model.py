#____________________________________________________________________________________________________________________________________________________
# Create a file geodatabase to fit the NENA Data Model: NENADataModel.py
# Created on:     2015-11-20 (Jason Guthrie, TComm911)
# Last Update on: 2016-10-19 (Jason Guthrie, TComm911)
# Description: Creates a File Geodatabase then adds feature classes.  
#              Fields are added to each feature class after they are created.
#              Some fields are optional or conditional so may be commented out with a # if you don't need to use them.
#              The NG911 Data Model is still in DRAFT stage so this script reflects the most current version known and will allow for easy updates.
#____________________________________________________________________________________________________________________________________________________

print ("Importing ArcPy")
import arcpy, datetime
print (datetime.datetime.now().time())

#Make sure that the folder path in this variable exists and is where you want to create the file geodatabase.
FolderPath = "c:\\Temp"
MetadataPath = "\\\\tcomfs01\\Datasys\\GIS\\Scripts\\Metadata\\"
print
print ("Working Folder set to:          " + FolderPath)
print ("Metadata Folder set to:         " + MetadataPath)
GeodatabaseName = FolderPath + "\\NG911DataDRAFT.gdb"
arcpy.gp.CreateFileGDB(FolderPath, "NG911DataDRAFT", "CURRENT")
print ("Created File Geodatabase:       " + GeodatabaseName)
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "RoadCenterlines"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RCL_NGUID", "TEXT", "", "", "100", "Road Centerline NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_L", "TEXT", "", "", "15", "Left Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_R", "TEXT", "", "", "15", "Right Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "FromAddr_L", "LONG", "", "", "", "Left FROM Address", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ToAddr_L", "LONG", "", "", "", "Left TO Address", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "FromAddr_R", "LONG", "", "", "", "Right FROM Address", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ToAddr_R", "LONG", "", "", "", "Right TO Address", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Parity_L", "TEXT", "", "", "1", "Parity Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Parity_R", "TEXT", "", "", "1", "Parity Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "9", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "25", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "StreetName", "TEXT", "", "", "60", "Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "25", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "9", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Type", "TEXT", "", "", "5", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LStPosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESN_L", "TEXT", "", "", "5", "ESN Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESN_R", "TEXT", "", "", "5", "ESN Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_L", "TEXT", "", "", "30", "MSAG Community Name Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_R", "TEXT", "", "", "30", "MSAG Community Name Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country_L", "TEXT", "", "", "2", "Country Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country_R", "TEXT", "", "", "2", "Country Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State_L", "TEXT", "", "", "2", "State Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State_R", "TEXT", "", "", "2", "State Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County_L", "TEXT", "", "", "40", "County Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County_R", "TEXT", "", "", "40", "County Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode_L", "TEXT", "", "", "6", "Additional Code Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode_R", "TEXT", "", "", "6", "Additional Code Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncMuni_L", "TEXT", "", "", "100", "Incorporated Municipality Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncMuni_R", "TEXT", "", "", "100", "Incorporated Municipality Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_L", "TEXT", "", "", "100", "Unincorporated Community Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_R", "TEXT", "", "", "100", "Unincorporated Community Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_L", "TEXT", "", "", "100", "Neighborhood Community Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_R", "TEXT", "", "", "100", "Neighborhood Community Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostCode_L", "TEXT", "", "", "7", "Postal Code Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostCode_R", "TEXT", "", "", "7", "Postal Code Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostComm_L", "TEXT", "", "", "40", "Postal Community Name Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostComm_R", "TEXT", "", "", "40", "Postal Community Name Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RoadClass", "TEXT", "", "", "15", "Road Class", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "OneWay", "TEXT", "", "", "2", "One-Way", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "SpeedLimit", "SHORT", "", "", "", "Speed Limit", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PSAP_Boundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "100", "Emergency Service Boundary NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "Law"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "100", "Emergency Service Boundary NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "Fire"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "100", "Emergency Service Boundary NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EMS"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "100", "Emergency Service Boundary NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "StreetNameAlias"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_NGUID", "TEXT", "", "", "100", "Alias Street Name Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RCL_NGUID", "TEXT", "", "", "100", "Road Centerline NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreMod", "TEXT", "", "", "15", "Alias Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreDir", "TEXT", "", "", "9", "Alias Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AStPreType", "TEXT", "", "", "25", "Alias Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreSep", "TEXT", "", "", "20", "Alias Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_Name", "TEXT", "", "", "60", "Alias Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AStPosType", "TEXT", "", "", "25", "Alias Street Name Post Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PosDir", "TEXT", "", "", "9", "Alias Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PosMod", "TEXT", "", "", "25", "Alias Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStPreDir", "TEXT", "", "", "2", "Alias Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStName", "TEXT", "", "", "75", "Alias Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStType", "TEXT", "", "", "5", "Alias Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStPosDir", "TEXT", "", "", "2", "Alias Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "SiteAddressPoints"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "100", "Site Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "40", "County", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddDataURI", "TEXT", "", "", "254", "Additional Data URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddNum_Pre", "TEXT", "", "", "15", "Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Add_Number", "LONG", "", "", "", "Address Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddNum_Suf", "TEXT", "", "", "15", "Address Number Suffix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "9", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "25", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "StreetName", "TEXT", "", "", "60", "Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "25", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "9", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Type", "TEXT", "", "", "5", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LStPosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESN", "TEXT", "", "", "5", "ESN", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MSAGComm", "TEXT", "", "", "30", "MSAG Community Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Post_Comm", "TEXT", "", "", "40", "Postal Community Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Post_Code", "TEXT", "", "", "7", "Postal Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Post_Code4", "TEXT", "", "", "4", "ZIP Plus 4", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Building", "TEXT", "", "", "75", "Building", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Floor", "TEXT", "", "", "75", "Floor", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Unit", "TEXT", "", "", "75", "Unit", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Room", "TEXT", "", "", "75", "Room", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Seat", "TEXT", "", "", "75", "Seat", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Addtl_Loc", "TEXT", "", "", "225", "Additional Location Information", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LandmkName", "TEXT", "", "", "150", "Complete Landmark Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Mile_Post", "TEXT", "", "", "150", "Milepost", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Place_Type", "TEXT", "", "", "50", "Place Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Placement", "TEXT", "", "", "25", "Placement Method", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Long", "DOUBLE", "", "", "", "Longitude", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Lat", "DOUBLE", "", "", "", "Latitude", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Elev", "SHORT", "", "", "", "Elevation", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "LandmarkNamePart"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNP_NGUID", "TEXT", "", "", "100", "Landmark Name Part NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "100", "Site NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLMNNGUID", "TEXT", "", "", "100", "Alias Complete Landmark Name NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNamePart", "TEXT", "", "", "150", "Landmark Name Part", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNP_Order", "SHORT", "", "", "", "Landmark Name Part Order", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CompleteLandmarkNameAlias"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLMNNGUID", "TEXT", "", "", "100", "Alias Complete Landmark Name NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "100", "Site Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLandmark", "TEXT", "", "", "150", "Alias Complete Landmark Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "State"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel  #This should be provided by the state, not a local jurisdiction.
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "StateNGUID", "TEXT", "", "", "100", "State Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "County"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CntyNGUID", "TEXT", "", "", "100", "County Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "IncorporatedMunicipality"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncM_NGUID", "TEXT", "", "", "100", "Incorporated Municipality NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "UnincorporatedCommunity"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincNGUID", "TEXT", "", "", "100", "Unincorporated NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "NeighborhoodCommunity"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdNGUID", "TEXT", "", "", "100", "Neighborhood NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "RailroadCenterlines"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RS_NGUID", "TEXT", "", "", "100", "Rail Segment NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLOwn", "TEXT", "", "", "100", "Rail Line Owner", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLOp", "TEXT", "", "", "100", "Rail Line Operator", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLName", "TEXT", "", "", "100", "Rail Line Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RMPL", "FLOAT", "", "", "", "Rail Mile Post Low", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RMPH", "FLOAT", "", "", "", "Rail Mile Post High", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "HydrologyLine"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_NGUID", "TEXT", "", "", "100", "Hydrology Segment NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_Type", "TEXT", "", "", "100", "Hydrology Segment Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_Name", "TEXT", "", "", "100", "Hydrology Segment Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "HydrologyPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_NGUID", "TEXT", "", "", "100", "Hydrology Polygon NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Type", "TEXT", "", "", "100", "Hydrology Polygon Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Name", "TEXT", "", "", "100", "Hydrology Polygon Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CellSiteLocation"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Cell_NGUID", "TEXT", "", "", "100", "Cell NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_ID", "TEXT", "", "", "10", "Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Sector_ID", "TEXT", "", "", "4", "Sector ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Switch_ID", "TEXT", "", "", "10", "Switch ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CMarket_ID", "TEXT", "", "", "10", "Market ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSite_Name", "TEXT", "", "", "10", "Cell Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRD_ESRK", "LONG", "", "", "", "ESRD or First ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRK_Last", "LONG", "", "", "", "Last ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSctr_Ornt", "TEXT", "", "", "4", "Sector Orientation", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Technology", "TEXT", "", "", "10", "Technology", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "MileMarker"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "PROJCS['NAD_1983_HARN_StatePlane_Washington_South_FIPS_4602_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',45.83333333333334],PARAMETER['Standard_Parallel_2',47.33333333333334],PARAMETER['Latitude_Of_Origin',45.33333333333334],UNIT['Foot_US',0.3048006096012192]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]];-117498300 -98850300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "Source", "TEXT", "", "", "75", "Source of Data", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileMNGUID", "TEXT", "", "", "100", "Mile Post NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Unit", "TEXT", "", "", "15", "Mile Post Unit of Measurement", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileMValue", "FLOAT", "", "", "", "Mile Post Measurement Value", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Rte", "TEXT", "", "", "100", "MP Route Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Type", "TEXT", "", "", "15", "Mile Post Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Ind", "TEXT", "", "", "1", "Mile Post Indicator", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
#____________________________________________________________________________________________________________________________________________________
print
print ("The script is now COMPLETE.")
print (datetime.datetime.now().time())
wait = raw_input('Press <ENTER> to close.')
