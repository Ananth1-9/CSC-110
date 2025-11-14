import csv
def write_csv(dictionary, file_name):
    try:
        f = open(file_name, 'w')
        writer = csv.writer(f)

        kv = list(dictionary.items())
        for i in kv:
            writer.writerow([i[0]]+i[1])
    except:
        print('Error')
    
    f.close()
    