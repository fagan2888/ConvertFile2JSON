import pandas as pd
import re
import json

class convert:

    def __init__(self):
        return None

    # This method finds the number with required length
    def get_attribute(self, arr1, arr2, ilen):
        if len(arr1[0]) == ilen:

            if len(arr2) and arr2[0]:
                return arr2[0]

            return arr1[0], 0
        elif len(arr1[1]) == ilen:

            if len(arr2) and arr2[1]:
                return arr2[1]

            return arr1[1], 1
        elif len(arr1[2]) == ilen:

            if len(arr2) and arr2[2]:
                return arr2[2]

            return arr1[2], 2
        else:
            return ""

    def convert(self, input_file):
        df = pd.read_csv(input_file, header = None, names = ['name1', 'name2', 'c3','c4','c5'])

        result = {}

        df = df.fillna("")
        lst = []
        lerr = []
        for index, row in df.iterrows():
            isFour = False

            # only four columns present
            if len(row['c5']) == 0:
                isFour = True
                arr2 = [str(row['name2']), str(row['c3']), str(row['c4'])]
            else:
                arr2 = [str(row['c3']), str(row['c4']), str(row['c5'])]
            # pattern match to get only number values from alph-numeric string
            r1 = re.sub('[^0-9]', '', arr2[0])
            r2 = re.sub('[^0-9]', '', arr2[1])
            r3 = re.sub('[^0-9]', '', arr2[2])

            arr1 = [r1, r2 , r3]
            # phone
            rpho = self.get_attribute(arr1, [],  10)
            if len(rpho) == 2:
                rph = str(arr2[int(rpho[1])]).strip()
            # zip
            rzip = self.get_attribute(arr1, [],  5)
            if type(rzip) is tuple:
                rzip = rzip[0]
            # color
            color = str(self.get_attribute(arr1, arr2, 0)).strip()
            mdict = {}

            if len(rph) > 0 and len(rzip) > 0 and len(color) > 0:
                if isFour:
                    narr = str(row['name1']).split(" ")
                    fname, lname = narr[0].strip(), narr[1].strip()
                else:
                    fname, lname = str(row['name1']).strip() , str(row['name2']).strip()

                lst.append({"color": color, "firstname": fname, "lastname": lname, "phonenumber": rph, "zipcode": rzip})
            else:
                lerr.append(index)

        lst = sorted(lst, key=lambda k: (k['lastname'], k['firstname'] ))

        mdict["errors"] = lerr
        mdict["entries"] = lst

        f = open("result.json", "w+")
        out = json.dumps(mdict, indent = 2, sort_keys= True, ensure_ascii=False)
        f.write(out)
        f.close()
        # result["out"] = out
        print(out)
        return json.loads(out)

if __name__ == '__main__':

    # read from config file
    conf_file = "./conf/config.json"

    with open(conf_file, 'r') as configFile:
        input_file = json.loads(configFile.read())["filePath"]

    # instantiate class
    c = convert()
    # call the method ( now result is a JSON object, so use result['errors'] or result['entries'] to get values required
    result = c.convert(input_file)

    ##################### Simple testing
    # testing - Grab only the entries
    temp = result['entries']
    t1 = json.dumps(temp, indent=2, sort_keys=True, ensure_ascii=False)
    # print t1