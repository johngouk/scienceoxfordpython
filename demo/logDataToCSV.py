import time # Go with the micropython-lib/time, via mip download!
import random

print('Demo the use of the file system to store data, in a CSV format')
fn = 'data.csv'
with open(fn, mode='a') as f:
    f.write('Line, Date,Time,Value1,Value2\n')
    for i in range(0,100):
        ns = time.time_ns() # nsec resolution
        stringNs = str(ns) # Horrendous conversion to deal with MPy/ESP's dodgy time functions
        secs = int(stringNs[0:9])
        millis = int(stringNs[9:12])
        micros = int(stringNs[12:15])
        #print(ns, secs, millis, micros)
        #       |Format for CSV line| Variables, strftime format does YYYY-MM-DD,HH:MM:SS, CSV line format does these values
        f.write('%d,%s%d%d,%f,%f\n'%(i, time.strftime('%Y-%m-%d,%H:%M:%S', time.gmtime(secs)), millis, micros, random.randint(0,1000)/100,random.randint(0,1000)/100))

print('Wrote 100 entries to data.csv - reading back')
print()
with open(fn) as f:
    for l in f:
        print(l, end='')
        
print('Now click on three lines icon on RH side of MPy device window and select Refresh to see file')
print('Right click on data.csv to select "Download to..." and look at the downloaded file')
        
        