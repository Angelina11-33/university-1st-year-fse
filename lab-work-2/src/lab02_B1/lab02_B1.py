indices = ['0', '1', '2']

for n in indices:
    inputFile = open('inmap' + n + '.dat')
    outputFile = open('outmap' + n + '.dat', 'w')

    firstLine = inputFile.readline().split()
    quantity = int(firstLine[0])
    scale = float(firstLine[1])

    inchesList = []
    distances = []

    for line in inputFile:
        line = line.strip()
        if line == '':
            continue
        inches = float(line)
        inchesList.append(inches)
        distances.append(inches * scale)

    total = sum(distances)

    outputFile.write('Angelina Ploskikh\n')
    outputFile.write('Simple Map Distance Computations\n\n')
    outputFile.write('Map Scale Factor:  ' + format(scale, '.2f') + ' miles per inch\n\n')
    outputFile.write('      Map       Mileage\n')
    outputFile.write('      Measure   Distance\n')
    outputFile.write('============================================================\n')

    for i in range(len(inchesList)):
        inchesStr = format(inchesList[i], '.1f')
        distStr = format(distances[i], '.1f')
        outputFile.write('#  ' + str(i + 1) + '   ' + inchesStr + '        ' + distStr + '\n')

    outputFile.write('============================================================\n')
    outputFile.write('Total Distance:    ' + format(total, '.1f') + ' miles\n')

    inputFile.close()
    outputFile.close()