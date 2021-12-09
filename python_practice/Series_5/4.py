def add_to_list_in_dict(thedict, listname, element):
    if thedict[listname]:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)
    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname))


listname = input("please enter listname : ")
thedict = {"ali":[18,19,20],"reza":[12,14,16],"hasan":[13,15,19]}
try :
    add_to_list_in_dict(thedict, listname, 15)
except :
    print("Error")
finally :
    print("finished")