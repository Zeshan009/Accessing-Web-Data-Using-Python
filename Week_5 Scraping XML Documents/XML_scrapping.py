# Importing necessory libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

# Getting desired url where xml document is located
url = input('Enter location: ')


address = urllib.request.urlopen(url, context=ctx)

data = address.read()
print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
comment_values = []
for item in comments:
    comment_values.append(item.find('count').text)

for i in range(0, len(comment_values)):
    comment_values[i] = int(comment_values[i])
print('Sum of comment count is: ', sum(comment_values))

