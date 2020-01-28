#CS 385 – Python Programming Language
#Instructor: Dr. Vidhyacharan Bhaskar
#Homework 2A | Carlos Valero

#1______________________________________
def foo():
  out = ""
  n = int(input("Insert n: "))
  print("n\t\toutput printed so far\n__\t\t_____________________")
  while n != 1:
    out += (str(n)+", ")
    print(str(n) + "\t\t" + out)
    if n % 2 == 0:
      n = int(n/2)
    else:
      n = (n*3) + 1
  out += (str(n)+".")
  print(str(n) + "\t\t" + out)
foo()

#2______________________________________
def figure():
  width = 5   #ease to manipulate function.
  out = ""
  for i in range(1, width+1, 2):   #top half + mid
    out +=  getLine(width, i) + "\n"
  for i in range(width-2, 0, -2):  #bottom half
    out +=  getLine(width, i) + "\n"
  print(out)
  
def getLine(width, n_stars): #Supporting Func
  res = ""
  spc = int((width-n_stars)/2)
  while spc != 0:
    res += " "
    spc -= 1
  while n_stars != 0:
    res += "*"
    n_stars -= 1
  return res
figure()

#3______________________________________
def is_right_angled_triangle(a, b, c):
  return pow(c,2) == pow(a,2) + pow(b,2)  #pythagorean theorem
is_right_angled_triangle(4,3,5)

#4______________________________________
import random
def guess_a_number():
  n_guesses = 0
  n = random.randrange(10, 98)
  print(n)
  guess = 0
  while n != guess:  #Until guess match\
    guess = int(input("Guess the number: (Hint: 2-digit)-->"))
    n_guesses += 1
    if guess == n:
      break
    if n < guess:
      print("Lower..")
    else:
      print("Higher..")
  print("Well done!\nNumber of guesses: " + str(n_guesses))
guess_a_number()

#5______________________________________
lst = [4, 5, 1, 23, 8, 16]
lst1 = ['a', 'y', 'e', 'v']
def arrange_list(lst):
  asc = ()
  desc = []
  if type(lst[0]) == int:
    asc = set(lst) #a set is always ordered
    desc = list(asc)[::-1] #convert it to list for operate it
  else:
    desc = set(lst)
    asc = list(desc)[::-1] 
  print("\nAscending order: ")
  print(asc)
  print("\nDescending order: ")
  print(desc)
arrange_list(lst)
arrange_list(lst1)

#6______________________________________
mtx = [[3, 4, 1], [-12, 6, -4], [5, 2, 2]]
mtx1 = [[8, -2, 0], [7, -9, -1], [11, -4, 3]]
def matrix_operation(a, b):
  result = [[0 for x in range(len(a))] for y in range(len(a[0]))] #def
  opt = input("+ or -: ")
  if opt == '+': #user decides the operation
    for row in range(len(a)):
      for col in range(len(a[0])):
        result[row][col] = a[row][col] + b[row][col]
  else:    #might be a better solution, rather than repeat the code
    for row in range(len(a)):
      for col in range(len(a[0])):
        result[row][col] = a[row][col] - b[row][col]
  show(mtx)
  print('   ' + opt)
  show(mtx1)
  print('   =')
  show(result)
def show(a):   #supporting function
  for row in a:
    print(row)
matrix_operation(mtx, mtx1)
