
monthConversions = {
    "Jan" : "January",
    "Feb" : "Februry",
    "Apr" : "April",
}

print(monthConversions["Apr"])

for letter in "Giraffa pazza":
    print(letter)

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print ("Hai diviso per zero, male male")
except ValueError:
    print ("invalid Input")