import datetime, time


print("start")
time.sleep(3)
print("end")

start = datetime.datetime.now()
while True:

    # doing stuff

    now = datetime.datetime.now()
    diff = now- start

    if diff.total_seconds() >= 3:
        break

start = datetime.datetime.now()

while datetime.timedelta( start - datetime.datetime.now() ).total_seconds() < 3:
    # do stuff
    pass
