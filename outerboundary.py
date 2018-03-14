import shapefile
import simplekml
from shapely.geometry import Polygon
from shapely.ops import cascaded_union

#Change these variables to match the file locations on your machine
ZIP_TCA_FILE_LOC = "../zcta/tl_2017_us_zcta510.shp"
#ZIP_TCA_FILE_LOC = "mergetest.shp"
KML_OUTPUT_PATH = ""
KML_OUTPUT_NAME = "outerboundary.kml"
#ZIPCODES_FILE_LOC = "zipcodes"
ZIPCODES_FILE_LOC = "3A217 Zip List.csv"
#Create our list of zipcodes
zipcodefile = open(ZIPCODES_FILE_LOC)
ziplist = zipcodefile.read().rstrip().split(',')

kml = simplekml.Kml()

sf = shapefile.Reader(ZIP_TCA_FILE_LOC)

#Creates an index table for our zipcodes
record = sf.records()
lookup = {str(v[0]):i for i, v in enumerate(record)}

def getOuterBoundary(kml_object = kml,
    zipcodes=ziplist,
    shape_file = sf,
    boundary_color = simplekml.Color.blue,
    boundary_width = 5,
    polygon_shading = 50,
    polygon_color = simplekml.Color.blue):

    """
    Takes a list of zipcodes as strings and outputs a kml file of the outer boundary
    which can be opened in Google Earth, Google Maps, et al. Different polygon
    boundary colors and shades can be specified using `simplekml.Color.yourcolorchoice`.
    """
    polygons = {}
    for zipcode in zipcodes:
        if zipcode in lookup:
            index = lookup[zipcode]
            points = shape_file.shape(index).points
            parts = shape_file.shape(index).parts
            if len(parts) == 1:
                polygons[zipcode] = Polygon(points)
            elif len(parts) > 1:
                for n in range(len(parts)-1):
                    polygons[zipcode+str(n)] = Polygon(points[parts[n]:parts[n+1]])
                else:
                    polygons[zipcode+str(n+1)] = Polygon(points[parts[n+1]:])

    union = cascaded_union([v for k, v in polygons.items()])
    for polygon in union:
        pol = kml_object.newpolygon(outerboundaryis=list(zip(*polygon.exterior.coords.xy)))
        pol.style.linestyle.color = boundary_color
        pol.style.linestyle.width = boundary_width
        pol.style.polystyle.color = simplekml.Color.changealphaint(polygon_shading, polygon_color)
    return kml_object
    #kml.save(KML_OUTPUT_NAME)

#getOuterBoundary(boundary_color=simplekml.Color.blue,boundary_width=5, polygon_shading=70)
