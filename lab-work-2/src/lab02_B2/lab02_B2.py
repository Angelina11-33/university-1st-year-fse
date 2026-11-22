indices = ['1', '2', '3']

for n in indices:
    inputFile = open(n + '.WCData.txt')
    outputFile = open(n + '.WindChillReport.txt', 'w')

    inputFile.readline()
    inputFile.readline()

    times = []
    wcTemps = []
    wcEffects = []

    for line in inputFile:
        line = line.strip()
        if line == '':
            continue

        parts = line.split()
        timeStr = parts[0]
        tempF = float(parts[1])
        windV = float(parts[2])

        wcTemp = 35.74 + 0.6125 * tempF + (0.4275 * tempF - 35.75) * (windV ** 0.16)
        wcEffect = wcTemp - tempF

        times.append(timeStr)
        wcTemps.append(wcTemp)
        wcEffects.append(wcEffect)

    count = len(wcTemps)
    avgTemp = sum(wcTemps) / count

    outputFile.write('Time      WC temp    WC Effect\n')
    outputFile.write('--------------------------------\n')

    for i in range(count):
        tStr = format(wcTemps[i], '.1f')
        eStr = format(wcEffects[i], '.1f')
        outputFile.write(times[i] + '     ' + tStr.rjust(5) + '     ' + eStr.rjust(6) + '\n')

    outputFile.write('--------------------------------\n')
    outputFile.write(
        'The average adjusted temperature, based on '
        + str(count)
        + ' observations, was '
        + format(avgTemp, '.1f')
        + '\n'
    )

    inputFile.close()
    outputFile.close()