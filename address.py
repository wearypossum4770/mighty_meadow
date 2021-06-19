import xml.etree.ElementTree as ET

import requests

USPS_ADDRESS_API_COMPANY = "dragoomdoc"
USPS_ADDRESS_API_USERNAME = "693DRAGO4853"
USPS_ADDRESS_API_PASSWORD = "536ES52JZ916"
tag = ET.Element("AddressValidateRequest")
revision = ET.SubElement(tag, "Revision")
address = ET.SubElement(tag, "Address", attrib={"ID": "0"})

address_1 = ET.SubElement(address, "Address1")
address_2 = ET.SubElement(tag, "Address1")
city = ET.SubElement(tag, "Address2")
state = ET.SubElement(tag, "City")
zip_5 = ET.SubElement(tag, "State")
zip_4 = ET.SubElement(tag, "Address1")
last = ET.SubElement(tag, "Address1")
req = ET.dump(tag)
data = f"""https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML=


<AddressValidateRequest USERID={username}><Revision>1</Revision>
<Address ID="0">
<Address1>SUITE K</Address1>
<Address2>29851 Aventura</Address2>
<City/>
<State>CA</State>
<Zip5>92688</Zip5>
<Zip4/>
</Address>
</AddressValidateRequest>"""
print(req)
# r = requests.get(data)
# root = ET.fromstring(r.text)
# tree = ET.ElementTree(root)
# print(tree)
# print(root)
# tree.write("file.xml")
