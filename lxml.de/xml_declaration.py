import os
from lxml import etree

parser = etree.XMLParser()

filename = 'test.xml'
doc = etree.parse(filename, parser)

doc.write(filename, encoding="UTF-8", xml_declaration=True, method="xml")
