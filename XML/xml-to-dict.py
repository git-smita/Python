import xml.etree.ElementTree as element

def xml_iterator(tree, outDict):
  if tree is None:
    return outDict

  # When node has sub elments
  if tree.getchildren():
    outDict[tree.tag] = {}
    for subelement in tree.getchildren():
      result = xml_iterator(subelement, {})
      if subelement.tag in outDict[tree.tag]:
        if not isinstance(outDict[tree.tag][subelement.tag], list):
          outDict[tree.tag][subelement.tag] =[outDict[tree.tag][subelement.tag]]
          outDict[tree.tag][subelement.tag].append(result[subelement.tag])
      else:
        outDict[tree.tag].update(result)
  else:
    outDict[tree.tag] = tree.text

  return outDict

fd=open('C:\\temp\\data.xml','r')
xml_data=fd.read()
xml_data = """
<Records><Students></Students></Records>"""
recordDict=xml_iterator(element.fromstring(xml_data),{})
print recordDict
