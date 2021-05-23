import time

print(type(time.time()))                  #1621734643.6540225

print(type(time.localtime(time.time())))  #time.struct_time(tm_year=2021, tm_mon=5, tm_mday=23, tm_hour=7, tm_min=20, tm_sec=43, tm_wday=6, tm_yday=143, tm_isdst=0)

print(type(time.asctime(time.localtime(time.time()))))    #Sun May 23 07:20:43 2021


