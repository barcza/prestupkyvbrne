import csv


tabulka = []
datum = []
cas = []
with open('106_9_2018_prestupky_2017.csv', newline='', encoding="windows-1250") as infile, open('prestupkyx.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter = ";")
    next(reader, None)
    writer = csv.writer(outfile, delimiter = ";")

    for row in reader:
        date, time = row[0].strip().split()
        adresa = row[1].strip().split()
        if adresa[1].lower() == "brno":
            mesto = "0"
        elif adresa[1][0].isdigit():
            mesto = adresa[1][0]
        else:
            mesto = adresa[1]
        #tabulka.append(adresa)

        cas = time.replace(time[5:], "")

        if adresa[0].endswith(","):
            ulice = adresa[0].replace(",", "")
        else:
            ulice = adresa[0]

        if mesto.endswith(","):
            sidlo = mesto.replace(",", "")
        else:
            sidlo = mesto


        writer.writerow([date, cas, ulice, sidlo.lower(), row[2], row[3]])

#print(tabulka)



    #for row in reader:
        # Remove white spaces in each field and assign to vars
    #    date1, time, date2 = [x.strip() for x in row]
    #    writer.writerow([date1 or date2, time])

#for polozka in tabulka:
#    date, time = polozka[0].split()
#    datum.append(date)
#    cas.append(time)
