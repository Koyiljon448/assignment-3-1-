try:
   hour = int(input("Enter Hours:"))
   rate = int(input("Enter rate"))

except:
    (print("Error, please enter numeric input!"))
else:
   if hour <= 40:
       salary = int(hour) * float(rate)
       print("Salary:", salary)
   else:
      salary = int(hour) * float(rate) * 1.5
      print("Salary:", salary)
