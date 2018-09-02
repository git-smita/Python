from lxml import etree
xml_string="""
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology
      society in England, the young survivors lay the
      foundation for a new society.</description>
   </book>
</catalog>
"""


def parseBookXML(xmlFile):

    root = etree.fromstring(xmlFile)

    catalog_dict = {}
    book_dict = {}
    catalog_dict[root.tag] = {}
    for book in root.getchildren():
        book_dict = {}
        catalog_dict[root.tag][book.attrib['id']]={}
        for book_elem in book.getchildren():
            if not book_elem.text:
                book_dict[book_elem.tag] = None
            else:
                book_dict[book_elem.tag] = book_elem.text
        catalog_dict[root.tag][book.attrib['id']].update(book_dict)

    return catalog_dict

if __name__ == "__main__":
    d= parseBookXML(xml_string)
    print d