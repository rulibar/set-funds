"""
set_funds.py v0.1 (20-2-25)
Updates the funds parameter for pybots within the cwd.
"""

import os

cwd = os.getcwd()
lst = os.listdir()
bases = dict()

for item in lst:
    # filters and definitions
    if not os.path.isdir(item): continue
    if item[:3] != "bot": continue
    parts = item.split("_")
    if len(parts) != 2: continue

    # get pyfile and configfile
    lst2 = os.listdir(item)
    pyfile = item + "/"
    configfile = item + "/"
    for item2 in lst2:
        if ".py" in item2: pyfile += item2
        if "config.txt" in item2: configfile += item2
    print("~ " + item)
    print("~ " + pyfile)
    print("~ " + configfile)

    # get new funds size
    new_size = None
    with open(pyfile) as pyf:
        pyf_lines = pyf.readlines()
        for line in pyf_lines:
            if "; base =" in line:
                line = line.split(";")
                line = line[1].split("=")
                line = line[1].replace(" ", "")
                line = line.replace("\n", "")
                try:
                    new_size = bases[line]
                except Exception as e:
                    bases[line] = float(input("New size for base {}? ".format(line)))
                    new_size = bases[line]
    if new_size == None:
        print("Error: 'new_size == None'")
        continue

    # update the config.txt file
    text = str()
    with open(configfile, "r") as cof:
        cof_lines = cof.readlines()
        text = "".join(cof_lines)

    print("Old config.txt:\n{}".format(text))

    text_lst = text.split("\n")
    for i in range(len(text_lst)):
        line = text_lst[i]
        if "funds=" in line:
            line_lst = line.split("#")
            line_lst[0] = "funds={} ".format(new_size)
            text_lst[i] = "#".join(line_lst)
    text = "\n".join(text_lst)

    print("New config.txt:\n{}".format(text))

    with open(configfile, "w") as cof:
        cof.write(text)
