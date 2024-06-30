# print ("hello \nhello\n hello")

# print ("hello" + " baqar")
# a=input ("what is your name: ")
# length = len(a)
# print (length)

# #strings

# print("Hello"[0])
# print("Hello"[1])
# print("Hello"[2])
# print("123"+"567")   #it will take it as a string

# #integer
# print (123 + 567)
# print(3+3)

# #float
# print(6*0.3)
# print(0.6+0.6)

# #decimal point numbers
# print (231.25)

# chara = len (input("what is your name?"))
# print (type (chara))

# chara = len (input("what is your name?"))
# new_char= str(chara)

# print(type(new_char))
# print ("your name have " + new_char + " characters")
# a = str (123)
# print (type(a))

# name = "Baqar Raza"
# print(name.upper())
# print(name.lower())

#Conditions
print ("Welcome to the tip calculator")

total_bill = input ("what was the total bill? $")
T_bill = float (total_bill)

perc = input ("What percentage tip would you lke to give? 10, 12 or 15?")
tip = int (perc)
#print (perc)

persons= int (input ("How many people to split the bill?"))
#print (persons)

if (tip == 10):
      cost = (((T_bill*10)/100) +T_bill )
    #  print (cost)
elif (tip == 12):
      cost = (((T_bill*12)/100) +T_bill )
    #  print (cost)
else:
    cost = (((T_bill*15)/100) +T_bill )
   # print (cost) 

ind_bill = (cost / persons)
bill= (round (ind_bill,2))

print (f"Each person should pay:${bill}")