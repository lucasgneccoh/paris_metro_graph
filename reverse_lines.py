def write_reverse_order(header, stations, out):
    out.write(header + "\n")
    for s in reversed(stations):
        out.write(s + "\n")



name = "stationsWithRERNoAccent20231019.data"
with open(name, "r", encoding= "iso-8859-1") as f:
    with open('aux.txt', 'w') as out:
        stations = []
        recording = False
        for l in f: 
            if any(map(l.startswith, '#@')):
                if recording and stations:
                    header = f"{start}r:{source} -- {terminus}"
                    write_reverse_order(header, stations, out)
                    stations = []
                    recording = False

                if len(l.strip().split(' '))>1 and any(map(l.strip().split(' ')[1].startswith, 'ABCDE')):
                    terminus = l.strip().split('--')[1].strip()
                    start = l.strip().split('--')[0].split(':')[0].strip()
                    source = l.strip().split('--')[0].split(':')[1].strip()
                    stations = []
                    recording = True

            else:
                if recording:
                    a, b = l.strip().split(':')
                    stations.append(f"{a}r:{b}")