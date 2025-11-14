import csv
def read_csv(file_name):
    dict1 = {}
    try:
        f = open(file_name, 'r')
        reader = csv.reader(f)
        for row in reader:
            if row:
                key = row[0]
                values = []
                for item in row[1:]:
                    try:
                        values.append(int(item))
                    except:
                        try:
                            values.append(float(item))
                        except:
                            values.append(item)
                dict1[key] = values
    except:
        print('error')

    f.close()
    return dict1