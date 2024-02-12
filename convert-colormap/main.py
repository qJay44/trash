with open('colormap.txt', 'r') as f1, \
    open('colormap_formatted.txt', 'w') as f2:
    lines = f1.readlines()
    [f2.write("0x" +
        ("%0.2x" % int(float(l[1:9]) * 255)) +
        ("%0.2x" % int(float(l[11:19]) * 255)) +
        ("%0.2x" % int(float(l[21:29]) * 255)) +
        "ff,\n") for l in lines]
