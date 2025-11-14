#Ethan
def read_first_line(filename):
    info = open(filename, 'r')
    line1 = info.readline()
    info.close()
    return line1

