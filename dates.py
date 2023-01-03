# Existing datetime module to import dates

import datetime

x = datetime.datetime.now()
print(x)

# Creating date objects
# datetime() class has 3 parameters year, month, day

x = datetime.datetime(2020,5,19)

#Date Output

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%a"))
