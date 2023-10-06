what_year = int(input("What Year?\n"))
what_month = int(input("What Month?\n"))

def is_leap(year = what_year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False



def days_in_month(year = is_leap(), month = what_month):
  """Takes 2 args, the year and a month.

  Args:
      year (int, optional): Year. Defaults to is_leap().
      month (int, optional): Month. Defaults to what_month.

  Returns:
      int: How many days chosen month of chosen year has.
  """  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(what_year):
    return 29
  else:
    number = month_days[month-1]
    return number
    
print(days_in_month())