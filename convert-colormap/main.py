with open('colormap.txt', 'r') as f1, \
    open('colormap_formatted.txt', 'w') as f2:
    lines = f1.readlines()
    lines = [f2.write('{' + \
        f'{int(float(l[1:9])   * 255)}, ' + \
        f'{int(float(l[11:19]) * 255)}, ' + \
        f'{int(float(l[21:29]) * 255)}'   + \
        '},\n')
        for l in lines
    ]
