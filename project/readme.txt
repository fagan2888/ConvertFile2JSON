Setup:
(1) Used Python 2.7.10. I have use PyCharm for this assignment. It can be loaded into similar IDE.
(2) Use "requirements.txt" to install required library.
(3) In "config.json" under "conf" folder, the location of data file is mentioned.

Folder structure and information:
(1) The data file is in the folder "data"
(2) "convertFile2Json.py" -> The script that transforms the text file to JSON payload
(3) Script "convertFile2Json.py" has main method to directly run it.

Unit Testing:
(1) unit_test.py runs the unit testing for one valid file (test1.txt) and one invalid file (test2.txt)

Output:
(1) Output is stored in result.json. The "entries" are sorted by last name, first name.
(2) method "convert" inside  convertFile2Json.py also outputs json object with standard json.loads().
(3) JSON output is also printed in the console using print statement
 
