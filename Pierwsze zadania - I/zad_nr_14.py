import datetime
x = (2014, 7, 2)
y =(2014, 7, 11)

x1 = datetime.date(x[0],x[1],x[2])
y1 = datetime.date(y[0],y[1],y[2])

z = y1 - x1
print(z)