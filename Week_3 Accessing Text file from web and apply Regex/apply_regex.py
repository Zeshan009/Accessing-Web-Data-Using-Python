import re
path = "C:\Programming Practice\Written material of different tools\Data Science Specialization\Accesing web data using python\Finding sum.txt"
data = open(path, 'r')
values = data.read()
number = re.findall('[0-9]+', values)

for i in range(0, len(number)):
    number[i] = int(number[i])

print(sum(number))


