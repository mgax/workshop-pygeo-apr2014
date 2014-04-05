LOCALITATI_URL = (
    'http://earth.unibuc.ro/geoserver/datagov/ows'
    '?service=WFS&version=1.0.0&request=GetFeature'
    '&typeName=datagov:animale_localitati&outputFormat=csv'
)

import csv
import requests
from pyproj import Proj

stereo70 = Proj(init='epsg:31700')

with open('localitati.csv', 'wb') as f:
    out = csv.DictWriter(f, ['judet', 'nume', 'xy', 'vaci', 'oi'])
    out.writeheader()

    csv_lines = requests.get(LOCALITATI_URL, stream=True).iter_lines()
    for line in csv.DictReader(csv_lines):
        (x, y) = line['geom'].split('(')[1].split(')')[0].split()
        out.writerow({
            'judet': line['jud'],
            'nume': line['loc'],
            'xy': '%d,%d' % (float(x), float(y)),
            'vaci': line['bovine'],
            'oi': line['ovine'],
        })
