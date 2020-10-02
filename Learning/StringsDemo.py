string = "RahulShettyAcademy.com"
string2 = "Training"
string3 = "Rahul"

print(string[1])
print(string[0:5])  # subString
print(string + string2)  # string concatenation
print(string3 in string)  # substring check
print(str.__sizeof__(string))  # char count
print(string.__sizeof__())  # char count

var = string.split(".")
print(var[0])
print(var[1])


print(string3.strip())
print(string3.lstrip())
print(string3.rstrip())
