from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF


data = [
        # Year Month  Predict    High  Low
        (2018,  10,     4.2,      5.2,  3.2),
        (2018,  11,     4.2,      6.2,  2.2),
        (2018,  12,     4.1,      7.1,  1.1),
        (2019,   1,     4.1,      9.1,  0.0),
        (2019,   2,     4.4,      9.4,  0.0),
        (2019,   3,     4.5,     10.5,  0.0),
        (2019,   4,     4.7,     11.7,  0.0),
        (2019,   5,     4.9,     11.9,  0.0),
        (2019,   6,     5.0,     13.0,  0.0),
        (2019,   7,     5.1,     14.1,  0.0),
        (2019,   8,     5.2,     14.2,  0.0),
        (2019,   9,     5.2,     15.2,  0.0),
        (2019,  10,     4.9,     14.9,  0.0),
        (2019,  11,     4.4,     14.4,  0.0),
        (2019,  12,     4.1,     14.1,  0.0),
        (2020,   1,     3.8,     13.8,  0.0),
        (2020,   2,     3.6,     13.6,  0.0),
        (2020,   3,     3.3,     13.3,  0.0),
        (2020,   4,     3.0,     13.0,  0.0),
        (2020,   5,     2.8,     12.8,  0.0),
        (2020,   6,     2.6,     12.6,  0.0),
]


drawing = Drawing(200, 150)

pred = [row[2] for row in data ]
high = [row[3] for row in data ] 
low =  [row[4] for row in data ]
times = [200 *((row[0] + row[1]/12.0)-2007)-100 for row in data]

drawing.add(String(65, 115, 'Sunspot', fontSize=18,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')