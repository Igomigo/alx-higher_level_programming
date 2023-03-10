#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    #print the names in the module
    names = sorted(dir(hidden_4))

    #iterate through the file
    for name in names:
        if name[:2] != '__':
            #print only names that do not start with '__'
            print("{}".format(name))
