# zipcodestokml
Takes a list of zipcodes and creates a kml file containing polygons of the zipcode areas which can be opened in Google Earth, Google Maps, et al.


# Requirements
You will need to download and extract the tl_2017_us_zcta510.zip file from https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2017&layergroup=ZIP+Code+Tabulation+Areas

You will also need to `pip install shapefile`, `pip install simplekml`, and `pip install shapely` 


##Remember
You will need to change the FILE_LOC variables to match the file locations on your machine.
