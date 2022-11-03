
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane","Lisa"]

# writing a list data  into a file
try:
    f = open("names.txt", "w+") # W+ overrite every time
    for x in people:
        f.write(x+"\n")
except:
    print("file doenot exist")
finally:
    f.close()

# reading from file 
try:
    f = open("names.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x.strip("\n"))
except:
    print("file doenot exist")
finally:
    f.close()

# puting duplicate data into a asingle file and reading
try:
    f1 = open("names.txt", "r")
    f = f1.readlines()
    count = 0
    newlist = []
    newfile = open("repeatednames.txt","w+")
    for x in f:
        if x not in newlist:
            newlist.append(x)
        else:
            newfile.write(x+"\n")

except:
    print("file does not exist")
finally:
    f1.close()
    newfile.close()

#reading duplicate data file
try:
    print("Duplicate data view\n")
    f = open("repeatednames.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x.strip("\n"))
except:
    print("file doenot exist")
finally:
    f.close()

# make dictionry data in file by using th name as key and valus as repeted name
 
try:
    f1 = open("names.txt", "r")
    f = f1.readlines()
    newlist = []
    new_dic_file = open("dicfile.txt","w+")
    print(type(f))
    for x in f:
        n=x.strip("\n")
        no=f.count(x)
        s=f"name: {n}, count: {no}\n"
        if n not in newlist:
            new_dic_file.write(s)
            newlist.append(n)

except:
    print("file does not exist")
finally:
    new_dic_file.close()

#reading duplicate data file
try:
    print("creating dic file data view\n")
    f = open("dicfile.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x.strip("\n"))
except:
    print("file doenot exist")
finally:
    f.close()
