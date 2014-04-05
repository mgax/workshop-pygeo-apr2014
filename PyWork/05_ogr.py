import ogr, os

def createBuffer(inputfn, outputBufferfn, bufferDist):
    inputds = ogr.Open(inputfn)
    inputlyr = inputds.GetLayer()

    shpdriver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(outputBufferfn):
        shpdriver.DeleteDataSource(outputBufferfn)
    outputBufferds = shpdriver.CreateDataSource(outputBufferfn)
    bufferlyr = outputBufferds.CreateLayer(outputBufferfn, geom_type=ogr.wkbPolygon)
    featureDefn = bufferlyr.GetLayerDefn()

    for feature in inputlyr:
        ingeom = feature.GetGeometryRef()
        geomBuffer = ingeom.Buffer(bufferDist)
        
        outFeature = ogr.Feature(featureDefn)
        outFeature.SetGeometry(geomBuffer)
        bufferlyr.CreateFeature(outFeature)

def main(inputfn, outputBufferfn, bufferDist):
    createBuffer(inputfn, outputBufferfn, bufferDist)

workspaceVector = "/home/instructor/Desktop/Data/";
inputfn = workspaceVector + 'Vector/02_Judete_centroid.shp'
outputBufferfn = workspaceVector + 'testBuffer.shp'
bufferDist = 10000.0
main(inputfn, outputBufferfn, bufferDist)
print "Done"
