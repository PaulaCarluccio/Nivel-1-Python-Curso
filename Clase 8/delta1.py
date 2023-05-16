# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
print(str(datetime.now() + timedelta(days=365)))
print(str(datetime.now() + timedelta(hours=1)))
print(str(datetime.now() + timedelta(minutes=1)))