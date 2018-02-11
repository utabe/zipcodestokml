import shapefile
import csv
import simplekml
import numpy

inputfile = csv.reader(open('zipcodes.csv','r'))

kml = simplekml.Kml()

sf = shapefile.Reader("zcta/tl_2017_us_zcta510.shp")

record = sf.records()
ar = numpy.array(record)

for zipcode in inputfile:
    for zc in zipcode:
        index = numpy.where(ar==zc)[0][0]
        points = sf.shape(index).points
        pol = kml.newpolygon(name=zc, description =zc, outerboundaryis=points)
        pol.style.linestyle.color = simplekml.Color.blue
        pol.style.linestyle.width = 5
        pol.style.polystyle.color = simplekml.Color.changealphaint(50, simplekml.Color.blue)

kml.save("zipcodesboundaries.kml")
