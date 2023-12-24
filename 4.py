import xml.dom.minidom

dom = xml.dom.minidom.parse("sample.xml")
company = dom.documentElement
staff = company.getElementsByTagName("staff")
for i in staff:
    print(f"-- Staff {i.getAttribute('id')} --")

    name = i.getElementsByTagName('name')[0].childNodes[0].nodeValue
    salary = i.getElementsByTagName('salary')[0].childNodes[0].nodeValue

    print(f"Name : {name}")
    print(f"Salary : {salary}")