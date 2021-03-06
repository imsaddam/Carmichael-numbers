def calculate_euclid_algorithm(number1,number2): #Function for Algorithm
  if number1 == 0:
    return number2
  elif number2 == 0 :
    return number1;    
  reminder = number1%number2; #Check the Reminder
  return calculate_euclid_algorithm(number2,reminder) # Return Function value


def modulu_power(x, y, mod) :
  if (y == 0) :
    return 1
  yy = int(y / 2)
  tem_value = modulu_power(x,yy, mod) % mod 
  tem_value = (tem_value * tem_value) % mod 
  if (y % 2 == 1) :
    tem_value = (tem_value * x) % mod 
  return tem_value 
 
def check_carmichael_number(n) :
  starting_prime_numner = 2
  for i in range(2, n-1 ):
    if (calculate_euclid_algorithm(i, n) == 1) :
      if (modulu_power(i, n - 1, n) != 1):
        return 0
  return 1

def carmichael_numbers_output(n):
  for i in range(561,n):
    if check_carmichael_number(i) == 1:
      print(i)

carmichael_numbers_output(10000)
