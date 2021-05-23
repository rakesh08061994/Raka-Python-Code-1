# There are several way in python to read time in human readable format in time module.
# Because many time module function return time value as a tuple of 9 integers,
#  so we need to read in human readable format for userfriendly approach
# time.asctime(time.localtime())
# NOTE : Here time.localtime() function return time value as a tuple of 9 integers. 
# Output return of time.localtime() :-
'''time.struct_time(tm_year=2021, tm_mon=4, tm_mday=12,tm_hour=13,
  tm_min=43, tm_sec=18, tm_wday=0, tm_yday=102, tm_isdst=0)'''

# And time.asctime() make it in human readable format 
''' Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
 When the time tuple is not present, current time as returned by localtime() is used.'''

# -----------------------------------------------------------------------------------------------------


import time         # import time module

time_now = time.asctime(time.localtime())       # time_now is a variable object

print("The current date and time is : ",time_now)



# OUTPUT is :
'''The current date and time is :  Mon Apr 12 14:09:18 2021'''


