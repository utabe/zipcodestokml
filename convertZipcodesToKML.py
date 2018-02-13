import shapefile
import simplekml

ZIP_TCA_FILE_LOC = "../zcta/tl_2017_us_zcta510.shp"
KML_OUTPUT_PATH = ""
KML_OUTPUT_NAME = "boundaries.kml"
ZIPCODES_FILE_LOC = "zipcodes"

#Create our list of zipcodes
zipcodefile = open(ZIPCODES_FILE_LOC)
ziplist = zipcodefile.read().rstrip().split(',')

kml = simplekml.Kml()

sf = shapefile.Reader(ZIP_TCA_FILE_LOC)

#Creates an index table for our zipcodes
record = sf.records()
lookup = {str(v[0]):i for i, v in enumerate(record)}

def convertZipcodesToKML(zipcodes=ziplist,
    shape_file = sf,
    kml_object = kml,
    boundary_color = simplekml.Color.blue,
    boundary_width = 5,
    polygon_shading = 50,
    polygon_color = simplekml.Color.blue):

    """
    Takes a list of zipcodes as strings and outputs a kml file which can be
    opened in Google Earth, Google Maps, et al. Different polygon boundary colors
    and shades can be specified using `simplekml.Color.yourcolorchoice`.
    """

    for zipcode in zipcodes:
        index = lookup[zipcode]
        points = shape_file.shape(index).points
        pol = kml_object.newpolygon(name=zipcode, description=zipcode, outerboundaryis=points)
        pol.style.linestyle.color = boundary_color
        pol.style.linestyle.width = boundary_width
        pol.style.polystyle.color = simplekml.Color.changealphaint(polygon_shading, polygon_color)

    kml_object.save(KML_OUTPUT_NAME)

convertZipcodesToKML()
