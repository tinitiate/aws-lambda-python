# from datetime import datetime

# date_time_str = '18-09-19 01:55:19'

# date_time_obj = datetime.strptime(date_time_str, '%y-%m-%d %H:%M:%S')


# print ("The type of the date is now",  type(date_time_obj))
# print ("The date is", date_time_obj)


import datetime

input = '2021-05-25 01:55:19'
  
# format
format = '%Y-%m-%d %H:%M:%S'
  
# convert from string format to datetime format
invoice_date = datetime.datetime.strptime(input, format)
print(type(invoice_date))