from datetime import datetime
from tidegravity import solve_point_corr

lat = float(input("Latitude : "))
lon = float(input("Longitude : "))
alt = float(input("Altitude : "))

year = int(input("Tahun: "))
month = int(input("Bulan: "))
day = int(input("Hari: "))

start = input("Jam mulai: ")
finish = input("Jam selesai:")

interval = int(input("Interval pengukuran (menit):"))

start_time = datetime.strptime(f"{year}-{month}-{day} {start}", "%Y-%m-%d %H:%M")
finish_time = datetime.strptime(f"{year}-{month}-{day} {finish}", "%Y-%m-%d %H:%M")

duration = int((finish_time - start_time).total_seconds() / 60)

x = int(duration/ interval) + 1

result = solve_point_corr(lat,lon,alt,start_time,n=x, increment=f"{interval}min")

print(result)

gtotal = g0
print(gtotal)