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
# data = [
#     (2007,   8,   113.2,    114.2,  112.2),
#     (2007,   9,   112.8,    115.8,  109.8),
#     (2007,  10,   111.0,    116.0,  106.0),
#     (2007,  11,   109.8,    116.8,  102.8),
#     (2007,  12,   107.3,    115.3,  99.3 ),
#     (2008,   1,   105.2,    114.2,  96.2 ),
#     (2008,   2,   104.1,    114.1,  94.1 ),
#     (2008,   3,    99.9,    110.9,  88.9 ),
#     (2008,   4,    94.8,    106.8,  82.8 ),
#     (2008,   5,    91.2,    104.2,  78.2 ),

# ]

drawing = Drawing(200, 150)

pred = [row[2]+30 for row in data ]
high = [row[3]+30 for row in data ] 
low =  [row[4]+30 for row in data ]
times = [200 *((row[0] + row[1]/12.0)-2018) -110 for row in data]

drawing.add(PolyLine(list(zip(times,pred)),strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times,high)),strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times,low)), strokeColor=colors.green))

drawing.add(String(65, 115, 'Sunspot', fontSize=18,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')