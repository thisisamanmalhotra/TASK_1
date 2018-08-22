import xml.etree.ElementTree as ET
tree=ET.parse('Task.xml')
root=tree.getroot()
title=raw_input("Enter title: ")
frame=raw_input("Enter frame: ")
main=""
for elem in root.findall('./PageRoot/Page'):
    if elem.get('name')==title:
        for elem2 in elem.findall('./steps/step'):
            if elem2.get("frame")==frame:
                for elem3 in elem2.attrib["pose"]:
                    if elem3!=" ":
                        main=main+elem3
                    else:
                        print main
                        main=""
                        #print "\n"