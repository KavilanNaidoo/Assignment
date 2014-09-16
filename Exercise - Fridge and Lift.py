#Kavilan Naidoo
#16-09-2014
#Exercise - Fridge and Lift

lift_height=float(input(" Please enter the lift height: "))
lift_width=float(input(" Please enter the lift width: "))
lift_length=float(input(" Please enter the lift length: "))
lift_space= lift_height * lift_width * lift_length

fridge_height=float(input(" Please enter the fridge height: "))
fridge_width=float(input(" Please enter the fridge width: "))
fridge_length=float(input(" Please enter the fridge length: "))
fridge_space= fridge_height * fridge_width * fridge_length

space= lift_space - fridge_space
print("The available space when the fridge is in the lift is: {0}cm cubed".format(space))

