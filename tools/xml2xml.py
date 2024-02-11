import xml.etree.ElementTree as ET

def read_and_modify_xml(xml_file_path, ori, target):
    # print(xml_file_path)
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    modified = False

    for obj in root.findall("object"):
        name = obj.find("name").text
        if name == ori:        
            obj.find("name").text = target
            modified = True

    if modified:
        print(f"Modified '{ori}' to '{target}' in: {xml_file_path}")

    tree.write(xml_file_path)