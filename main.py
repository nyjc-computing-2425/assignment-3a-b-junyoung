nric = input('Enter an NRIC number: ')

# Type your code below
nric_no = nric[1:-1]
length = len(nric_no)
nric_end = nric[-1]
start_st = "JZIHGFEDCBA"
start_fg = "XWUTRQPNMLK"

if nric.startswith(("S", "T", "F", "G")) and nric_end.isalpha() and length == 7:
  total_sum = 0
  total_sum += int(nric_no[0]) * 2
  total_sum += int(nric_no[1]) * 7
  total_sum += int(nric_no[2]) * 6
  total_sum += int(nric_no[3]) * 5
  total_sum += int(nric_no[4]) * 4
  total_sum += int(nric_no[5]) * 3
  total_sum += int(nric_no[6]) * 2
  
  if nric.startswith(("T", "G")):
    total_sum += 4
    final_val = total_sum % 11
  else:
    final_val = total_sum % 11

  if nric.startswith(("S", "T")):
    if start_st[final_val] == nric_end:
      print("NRIC is valid.")
    else:
      print("NRIC is invalid.")

  if nric.startswith(("F", "G")):
    if start_fg[final_val] == nric_end:
      print("NRIC is valid.")
    else:
      print("NRIC is invalid.")

else:
  print("NRIC is invalid.")
