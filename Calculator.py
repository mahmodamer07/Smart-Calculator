# Calculator project
# enter first number
# enter operator + - * /
# enter second number
# show result

print ("Thank you for using mahmod calculator, Please elt me help you")
first_number =float (input ("Please enter first number "))
operator = input ("Please enter operator + - * / : ")
second_number =float (input ("Please enter second number "))

if operator == "+":print(("The result is"),(first_number + second_number))
elif operator == "-":print(("The result is"),(first_number - second_number))
elif operator == "*":print(("The result is"),(first_number * second_number))
elif operator == "/":print(("The result is"),(first_number / second_number))
else:print ("Wrong operator")
print ("Thank you for using my calculator, Goodbye")
