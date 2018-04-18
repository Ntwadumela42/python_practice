"""You have to create a method, that corrects a given time string. There was a problem in addition, so many of the time strings are broken. Time-Format is european. So from "00:00:00" to "23:59:59". 

Some examples:

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"
"""

t = ("52:01:01")



st = t.split(':')
print(st)
hour = int(st[0])
minute = int(st[1])
sec = int(st[2])
if int(sec) >= 60:
  minute = minute + 1
  sec = sec - 60
print (minute)
print (sec)
if int(minute) >= 60:
  hour = hour + 1
  minute = minute - 60
print (minute)
print (hour)  
while hour >= 24:
  if hour >= 24:
    hour = hour - 24
seq = str(hour) + ':' + str(minute) + ':' + str(sec)
print(seq)
