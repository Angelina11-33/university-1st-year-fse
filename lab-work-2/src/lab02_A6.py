N = int(input())

totalSecInDay = N % 86400

hours = totalSecInDay // 3600
remSec = totalSecInDay % 3600

minutes = remSec // 60
seconds = remSec % 60

print(hours, ":", format(minutes, "02d"), ":", format(seconds, "02d"), sep="")