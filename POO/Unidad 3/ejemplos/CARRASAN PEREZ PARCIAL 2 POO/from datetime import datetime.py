import datetime

fechaV = '25/12/2024'
fechaV = int(fechaV.split('/')[1])
fechaH = datetime.date.today()
if fechaV - fechaH.month <= 2:
    importe = 3600 - (3600*0.1)
else:
    importe = 3600 + (3600*0.01)
print(importe)