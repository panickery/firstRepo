import datetime

now = datetime.datetime.now()
print('{:<50} :: {}'.format("datetime.datetime.now()", now))
print(type(now))

yesterday = now - datetime.timedelta(days=1)
print('{:<50} :: {}'.format("now - datetime.timedelta(days = 1)", yesterday))
print(type(yesterday))

yesterday_date = datetime.datetime.strftime(yesterday, '%Y%m%d')
print('{:<50} :: {}'.format("datetime.datetime.strftime(yesterday, '%Y%m%d')", yesterday_date))
print(type(yesterday_date))

yesterday_time = datetime.datetime.strftime(yesterday, '%H:%M:%S')
print('{:<50} :: {}'.format("datetime.datetime.strftime(yesterday, '%H:%M:%S')", yesterday_time))
print(type(yesterday_time))
