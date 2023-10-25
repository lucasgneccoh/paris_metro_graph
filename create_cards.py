# Only metro, not even RER in paris
# TODO: Add RER in paris, Zone 1
name = "stationsWithRERNoAccent20231019.data"
with open(name, "r", encoding= "iso-8859-1") as f:
    with open('cards_next_station_metro_only.txt', 'w', encoding='utf-8') as out:
        for l in f:
            if l.startswith('##'):
                terminus = l.strip().split('--')[1].strip()
                last = None
                go = True
            elif  any(map(l.startswith, 'ABCDEP@')):
                go = False
                continue
            else:
                if go:
                    station = l.strip().split(':')[1].strip()
                    if last is not None:
                        out.write(f"{last} (-> {terminus});{station}\n")
                    last = station


# RER Only
name = "stationsWithRERNoAccent20231019.data"
with open(name, "r", encoding= "iso-8859-1") as f:
    with open('cards_next_station_RER_only.txt', 'w', encoding='utf-8') as out:
        for l in f:
            if l.startswith('##'):
                terminus = l.strip().split('--')[1].strip()
                last = None
                go = True
            elif not any(map(l.startswith, 'ABCDE')):
                go = False
                continue
            else:
                if go:
                    station = l.strip().split(':')[1].strip()
                    if last is not None:
                        out.write(f"{last} (-> {terminus});{station}\n")
                    last = station



# Metro line
name = "stationsWithRERNoAccent20231019.data"
lines = set()
with open(name, "r", encoding= "iso-8859-1") as f:
    for l in f:
        if any(map(l.startswith, 'P#@')):                
            continue
        else:            
            station = l.strip().split(':')[1].strip()
            num = l.strip().split(':')[0].split('-')[0]
            lines.add(f"{station};{num}\n")
                
with open('cards_line_number.txt', 'w', encoding='utf-8') as out:
    for l in lines:
        out.write(l)


                