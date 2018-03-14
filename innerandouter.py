import shapefile
import simplekml
from shapely.geometry import Polygon
from shapely.ops import cascaded_union
from convertZipcodesToKML import convertZipcodesToKML
from outerboundary import getOuterBoundary


ZIP_TCA_FILE_LOC = "../zcta/tl_2017_us_zcta510.shp"
KML_OUTPUT_PATH = ""
KML_OUTPUT_NAME = "boundaries.kml"
ZIPCODES_FILE_LOC = "3A217 Zip List.csv"

zipcodefile = open(ZIPCODES_FILE_LOC)
ziplist = zipcodefile.read().rstrip().split(',')

kml = simplekml.Kml()

sf = shapefile.Reader(ZIP_TCA_FILE_LOC)

#Creates an index table for our zipcodes
record = sf.records()
lookup = {str(v[0]):i for i, v in enumerate(record)}
innerkml = convertZipcodesToKML(kml_object=kml,
    zipcodes=ziplist,
    shape_file = sf,
    boundary_color = simplekml.Color.black,
    boundary_width = 2,
    polygon_shading = 0,
    polygon_color = simplekml.Color.blue)
innerandouterkml = getOuterBoundary(kml_object = innerkml, polygon_shading = 70)
innerandouterkml.save(KML_OUTPUT_NAME)
