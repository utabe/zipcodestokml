import shapefile
import simplekml

#Change these variables to match the file locations on your machine
ZIP_TCA_FILE_LOC = "../zcta/tl_2017_us_zcta510.shp"
#ZIP_TCA_FILE_LOC = "mergetest.shp"
KML_OUTPUT_PATH = ""
KML_OUTPUT_NAME = "boundariestest.kml"
#ZIPCODES_FILE_LOC = "zipcodes"
ZIPCODES_FILE_LOC = "3A217 Zip List.csv"
#Create our list of zipcodes
zipcodefile = open(ZIPCODES_FILE_LOC)
ziplist = zipcodefile.read().rstrip().split(',')

kml = simplekml.Kml()

sf = shapefile.Reader(ZIP_TCA_FILE_LOC)
#w = shapefile.Writer(sf.shapeType)
#Creates an index table for our zipcodes
record = sf.records()
lookup = {str(v[0]):i for i, v in enumerate(record)}

#fake = [(-97.77, 30), (-97.79, 30), (-97.78,30.1),(-97.77, 30)]
#fake2 = [(-97.8, 30.1), (-97.79, 30), (-97.78,30.1),(-97.8, 30.1)]
#l1 = [fake,fake2]
#li = []
#di = {}
#for l in l1:
#    for n in range(len(l)-1):
#        li.append((l[n],l[n+1]))
#
#for i in li: di[i] = i in di

#newlist =[k for k in li if not di[k]]
#list(set(list1).intersection(list2))

#print(li)
#print(di)
#print(newlist)
#for point in newlist:
#    line = kml.newlinestring(coords=point)
#kml.save('finaltest.kml')

#dictionary = {}
#setz = set()
#for zc in ziplist:
#    index = lookup[zc]
#    setz.update(sf.shape(index).points)
#print(len(setz))

#print(lookup)
#w._shapes.extend(sf.shape(lookup['78745']))
#w._shapes.extend(sf.shape(lookup['78744']))
#w.save('merged')
#w.poly(parts=[fake])
#w.poly(parts=[fake2])
#w.save('mergetest')

#pol = kml.newpolygon(outerboundaryis=fake)
#poly = kml.newpolygon(outerboundaryis=fake2)
#pol.style.linestyle.color = simplekml.Color.blue
#pol.style.linestyle.width = 2
#pol.style.polystyle.color = simplekml.Color.changealphaint(50, simplekml.Color.blue)
#poly.style.linestyle.color = simplekml.Color.blue
#poly.style.linestyle.width = 2
#poly.style.polystyle.color = simplekml.Color.changealphaint(50, simplekml.Color.blue)

#kml.save("boundarytest.kml")
#
#list(set(dictionary['78745']).intersection(dictionary['78744']))
#Need to do a try/except in case they imput an unlisted zipcode
def convertZipcodesToKML(zipcodes=ziplist,
    shape_file = sf,
    boundary_color = simplekml.Color.blue,
    boundary_width = 5,
    polygon_shading = 50,
    polygon_color = simplekml.Color.blue):
#
#    """
#    Takes a list of zipcodes as strings and outputs a kml file which can be
#    opened in Google Earth, Google Maps, et al. Different polygon boundary colors
#    and shades can be specified using `simplekml.Color.yourcolorchoice`.
#    """
    kml = simplekml.Kml()
    setzip = []
    dic = {}
    for zipcode in zipcodes:
        if zipcode in lookup:
            index = lookup[zipcode]
            points = shape_file.shape(index).points
            if len(shape_file.shape(index).parts) > 1:
                print (zipcode)
            #points = [(float(format(x, '.3f')),float(format(y, '.3f'))) for x, y in points]
            for n in range(len(points)-1):
                setzip.append(tuple(sorted((points[n],points[n+1]))))
    for i in setzip: dic[i] = i in dic

    newlist =[k for k in setzip if not dic[k]]
    n=0
    #points1 = shape_file.shape(lookup['78745']).points
    #points2 = shape_file.shape(lookup['78744']).points
    #list3 = list(set(points1)-set(points2))
    #ppoly = kml.newpolygon(outerboundaryis=list3)
    #kml.save('boundariestest.kml')
    #print(len(newlist), newlist)
    #print(len(dic), dic)
    print(len(setzip), len(set(setzip)))
    for pair in newlist:
        pass
        #print(pair)
        #line = kml.newlinestring(coords=pair)
        #if n %551 == 0:
        #line.style.linestyle.color = boundary_color
        #else:
        #    line.style.linestyle.color = simplekml.Color.red
        #n+=1
    #else:
        #print (n)
        #line.style.linestyle.width = boundary_width
    #line.style.polystyle.color = simplekml.Color.changealphaint(polygon_shading, polygon_color)

    #kml.save(KML_OUTPUT_NAME)

convertZipcodesToKML(boundary_color=simplekml.Color.blue,boundary_width=5, polygon_shading=100)
