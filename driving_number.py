"""Introduction
 	In the United Kingdom, the driving licence is the official document which authorises its holder to operate various types of motor vehicle on highways and some other roads to which the public have access. In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective of ownership of the land over which the road passes, thus including many which allow the public to pass over private land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)
 
Driving
Task
 	The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
 
Rules
 	1–5: The first five characters of the surname (padded with 9s if less than 5 characters)

6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)

9–10: The date within the month of birth

11: The year digit from the year of birth (e.g. for 1987 it would be 7)

12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name

14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9

15–16: Two computer check digits. We will always use "AA"
 
Your task is to code a UK driving license number using an Array of data. The Array will look like

data = ["John","James","Smith","01-Jan-2000","M"]
Where the elements are as follows

 	0 = Forename

1 = Middle Name (if any)

2 = Surname

3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)

4 = M-Male or F-Female
 
You will need to output the full 16 digit driving license number.

Good luck and enjoy!"""

## My Solution:

def driver(data):
  
  
  
  #Surname part
  
  a = data[2]
  if len(a) >= 5:
    a = data[2][0:5]
  else:
    for x in range(0, -len(a)+5):
      a = a + "9"
  a = (a.upper())
  # print (a)
  
  #Second decade digit
  dd = (data[3][-2])
  # print (dd)
  
  #Month fxn
  month = data[3][3:6]
  print(month)
  if month == 'Jan': m = '01'
  elif month == 'Feb': m ='02'
  elif month == 'Mar': m ='03'
  elif month == 'Apr': m ='04'
  elif month == 'May': m ='05'
  elif month == 'Jun': m ='06'
  elif month == 'Jul': m ='07'
  elif month == 'Aug': m ='08'
  elif month == 'Sep': m ='09'
  elif month == 'Oct': m ='10'
  elif month == 'Nov': m ='11'
  elif month == 'Dec': m ='12'
  
  
  # print (m)
  
  
  if data[4] == 'F':  #If female, adds 50
    m = int(m) + 50
    
  # print (m)
  
  #day 
  day = data[3][0:2]
  # print(day)
  
  #year 
  year = data[3][-1]
  # print (year)
  
  #Initials
  # print (data[1])
  if data[1] == '':
    i = data[0][0] + '9'
  else:
    i = data[0][0] + data[1][0]
  
  
  # print (i)
  
  final = a + dd + m + day + year + i + '9AA'
  
  return final
  
print (driver(["Andrew", "Robert", "CUMMINGS", "02-September-1981", "M"]))


##Best Solution:

from datetime import datetime


def driver(data):
    first, middle, last, dob, gender = data
    try:
        d = datetime.strptime(dob, '%d-%b-%Y')
    except ValueError:
        d = datetime.strptime(dob, '%d-%B-%Y')

    return '{:9<5}{[2]}{:0>2}{:0>2}{[3]}{[0]}{[0]}9AA'.format(
        last[:5].upper(),
        str(d.year),
        d.month + (50 if gender == 'F' else 0),
        d.day,
        str(d.year),
        first,
        middle if middle else '9')
