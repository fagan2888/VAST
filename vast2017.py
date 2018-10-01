import csv
import datetime
import sys

#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    reader.next()
    inputList = []
    for row in reader:
        inputList.append(row)
    nodeList = {}
    for r in inputList:
        if r[1] not in nodeList:
            nodeList.setdefault(r[1], [])
            nodeList[r[1]].extend((r[0], r[2], r[3]))
        else:
            nodeList[r[1]].extend((r[0], r[2], r[3]))
    orig_stdout = sys.stdout
    fw = open("output11.txt", "w")
    sys.stdout = fw
    i = 1
    for key, value in nodeList.items():
        print "XP # " + str(i)
        print "v 1 \"" + key +"\""
        print "v 2 \"" + nodeList[key][1] +"\""
        print "e 1 2 \"type\""
        count = sum(1 for v in value if v)
        itr = count / 3
        num = 3
        vertex = 3
        while itr != 0:
            d = datetime.datetime.strptime(nodeList[key][num-3], "%Y-%m-%d %H:%M:%S")
            if d.hour < 12:
                attime = "Morning"
            elif 12 <= d.hour < 18:
                attime = "afternoon"
            else:
                attime = "evening"
            print "v " + str(vertex) +" \"" + nodeList[key][num-1]+"\""
            #print "v " + str(vertex+1) +" \"" + str(d.date())+"\""
            print "v " + str(vertex+1) +" \"" + str(d.strftime("%B"))+"\""
            #print "v " + str(vertex+2) +" \"" + str(d.time())+"\""
            print "v " + str(vertex+2) +" \"" + attime+"\""
            print "v " + str(vertex+3) +" \"" + str(d.strftime("%A"))+"\""
            if num == 3:
                print "e 2 " + str(vertex) +" \"Start at\""
                print "e " + str(vertex) + " " + str(vertex + 1) + " \"Date\""
                print "e " + str(vertex) + " " + str(vertex + 2) + " \"Time\""
                print "e " + str(vertex) + " " + str(vertex + 3) + " \"Day\""
            elif itr == 1:
                print "e " + str(vertex-2) + " " + str(vertex) +" \"Last at\""
                print "e " + str(vertex) + " " + str(vertex + 1) + " \"Date\""
                print "e " + str(vertex) + " " + str(vertex + 2) + " \"Time\""
                print "e " + str(vertex) + " " + str(vertex + 3) + " \"Day\""
            else:
                print "e " + str(vertex-2) + " " + str(vertex) +" \"Next start at\""
                print "e " + str(vertex) + " " + str(vertex + 1) + " \"Date\""
                print "e " + str(vertex) + " " + str(vertex + 2) + " \"Time\""
                print "e " + str(vertex) + " " + str(vertex + 3) + " \"Day\""
            num = num + 3
            itr = itr -1
            vertex = vertex + 4
        i = i + 1
    sys.stdout = orig_stdout
    fw.close()
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "Lekagul Sensor Data.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
