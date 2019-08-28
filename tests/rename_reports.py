import os
import xml.etree.cElementTree as ET

def main():

    
    for xml_file in os.listdir("test-reports/"):
        et = ET.ElementTree(file="test-reports/{}".format(xml_file))
        root = et.getroot()
        for testcase in root.findall('testcase'):
            class_name = testcase.get('classname')
            testcase.set('classname', "tests/{}".format(class_name))
        et.write("test-reports/{}".format(xml_file)) 


if __name__ == "__main__":
    main()