# Importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Enter required url of your choice
url = input('Enter - ')
# Reads the whole HTML page or document
html = urlopen(url, context=ctx).read()
# Save the HTML document in cleaned and tree structure
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
spans = soup('span')
numbers = list()
for span in spans:
    print('Values:', span.contents[0])
    numbers.append(span.contents[0])

# Converting all values within list into integer
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

# Printing the sum of integer values within the list
print('Sum of values:' ,sum(numbers))