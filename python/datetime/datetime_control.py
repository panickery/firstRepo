import datetime

now = datetime.datetime.now()
print('{:<50} :: {}'.format("datetime.datetime.now()", now)) 
print(type(now))

# datetime.datetime.now() :: 2020-08-07 17:23:17.638442
# <class 'datetime.datetime'>

yesterday = now - datetime.timedelta(days=1)
print('{:<50} :: {}'.format("now - datetime.timedelta(days = 1)", yesterday))
print(type(yesterday))

# now - datetime.timedelta(days = 1) :: 2020-08-06 17:23:17.638442
# <class 'datetime.datetime'>

yesterday_date = datetime.datetime.strftime(yesterday, '%Y%m%d')
print('{:<50} :: {}'.format("datetime.datetime.strftime(yesterday, '%Y%m%d')", yesterday_date))
print(type(yesterday_date))

# datetime.datetime.strftime(yesterday, '%Y%m%d') :: 20200806
# <class 'str'>

yesterday_time = datetime.datetime.strftime(yesterday, '%H:%M:%S')
print('{:<50} :: {}'.format("datetime.datetime.strftime(yesterday, '%H:%M:%S')", yesterday_time))
print(type(yesterday_time))

# datetime.datetime.strftime(yesterday, '%H:%M:%S') :: 17:23:17
# <class 'str'>
