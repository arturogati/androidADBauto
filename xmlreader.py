import xml.etree.ElementTree
from xml.dom import minidom
#doc = xml.etree.ElementTree.parse('view.xml').getroot()
#for elem in doc.findall('node/node'):
    #print (elem.get('index'))




xmldoc = minidom.parse('view.xml')
product_list = xmldoc.getElementsByTagName('node')
print("No of Items : ", len(product_list))
for product in product_list:
    print(product.attributes['bounds'].value)