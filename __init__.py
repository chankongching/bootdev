with open(inipath) as ini:
    for line in ini.readlines():
        exec(line)
