# Create a module with name my_time.py with next code implementation:
#  Import time and datetime modules
#  After import statement set clock count for checking script execution time
#  Print current time in format 'Tue May 24 14:09:17 2016’
#  Print current time year
#  Print current time day from the year begining
#  Use time tuple convertion into string and create string line with next format '24
# Mar 2015 12:14‘
#  Use time convertion from string into time tuple and create object from string '19
# Sep. 2012 10:15'
#  Create datetime tuple with cureent day minus one day
#  Check the difference with datime delta
#  Print script execution time

import time
import datetime

start = time.time()

print(time.ctime())
print(time.struct_time.tm_year)
print(time.struct_time.tm_yday)

print(time.strftime("%d %b. %Y %H:%M", time.gmtime()))
print(time.strptime("19 Sep. 2012 10:15", "%d %b. %Y %H:%M"))
print(datetime.datetime.now())
time_1 = datetime.datetime.date(datetime.datetime.now()) - datetime.timedelta(1, 0)

time_0 = datetime.datetime.date(datetime.datetime.now()) - time_1

print(f"Script execution  time: {(time.time()-start):.5f}" )
print("Script execution perf_count: %f4.2" %(time.perf_counter()))
print("Script execution process_tme: %f4.2" %(time.process_time()))
