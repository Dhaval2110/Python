__author__ = 'DHAVAL'
import xml.etree.ElementTree as ET                                                                                      # Imort module ET

tree=ET.parse('Dhaval.xml')
root=tree.getroot()

print root.tag
print root.attrib

for child in root:
     print(child.tag,child.attrib)

print([elem.tag for elem in root.iter()])
"""
for child in root:
    dictionary=dict(zip(child.tag,child.attrib))

print dictionary
"""
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):                                                        #The function .findall() always begins at the element specified. This type of function is extremely powerful for a "find and replace". You can even search on attributes!
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):                                           #use '...' inside of XPath to return the parent element of the current element
    print(movie.attrib)

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")                                                    # To modify an XML
print(b2tf)

b2tf.attrib["title"] = "Back to the Future"                                                                             # Replce with modification
print(b2tf.attrib)

tree.write("movies.xml")                                                                                                # Re=print modified

tree = ET.parse('movies.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)
tree.write("dhaval.xml")

tree = ET.parse('dhaval.xml')
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))

