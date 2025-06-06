# def dayofweek(day):
#   match day:
#     case 0:
#       return "Monday"
#     case 1:
#       return "Tuesday"
#     case 2:
#       return "Wednesday"
#     case 3:
#       return "Thursday"
#     case 4:
#       return "Friday"
#     case 5:
#       return "Saturday"
#     case 6:
#       return "Sunday"
#     case _:
#       return "Invalid day"
# # Test the function
# print(dayofweek(0))  # Output: Monday
# print(dayofweek(8))  # Output: Thursday
def is_weekend(day):
  match day:
    case 0 | 6:
      return True
    case _:
      return False
# Test the function
print(is_weekend(0))  # Output: True