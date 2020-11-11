from datetime import date
series=[]

def feladat_1():
    try:
        file = open("lista.txt")
        line=[]
        for data in file:
            line.append(data.rstrip("\n"))
            if(len(line)==5):
                series.append(line)
                line=[]
    except IOError as e:
        print("Error reading file")


def feladat_2():
    print("2. feladat")
    counter = 0
    for data in series:
        if data[0] == "NI":
            counter+=1
    print("A listaban ", len(series)-counter, "db vetitesi datummal rendelkezo epizod van.")


def feladat_3():
    print("3. feladat")
    counter = 0
    for data in series:
        if data[4] == "1":
            counter+=1
    a = (counter/len(series))*100
    print("A listaban levo epizodok ",round(a,2),"%-at latta.")

def feladat_4():
    print("4. feladat")
    sum_minutes = 0
    for data in series:
        if data[4] == "1":
            sum_minutes += int(data[3])

    day = int(sum_minutes / 1440)
    leftover_minutes = sum_minutes % 1440
    hours = int(leftover_minutes /60)
    minutes = sum_minutes - (day * 1440) - (hours*60)
    print("Sorozatnezessel ",day,"napot ",hours,"orat es",minutes,"percet toltott.")


def feladat_5():
    print("5. feladat")
    x = input("Adjon meg egy datumot!")
    print("Datum= ", x)
    input_date = date(int(x.split(".")[0]),int(x.split(".")[1]),int(x.split(".")[2]))
    for data in series:
        if data[0] != "NI":
            x = data[0].split(".")
            year = int(x[0])
            month = int(x[1])
            day = int(x[2])
            series_date = date(year,month,day)
            if series_date <= input_date and data[4]=="0":
                 print(data[2],"\t",data[1])

def Hetnapja(ev, ho, nap):
    napok=["v","h","k","sze","cs","p","szo"]
    honapok=[0,3,2,5,0,3,5,1,4,6,2,4]
    if ho < 3:
        ev-=1
    hetnapja = napok[int((ev + ev/4 - ev/100 + ev/400+ honapok[ho-1] + nap) % 7)]
    return hetnapja
    

def feladat_7():
    print("7. feladat")
    input_day = input("Adja meg a het napjat(pl cs)! Nap = ")
    series_that_day = set()
    previous_title=""
    for data in series:
        if data[0] != "NI":
            date = data[0].split(".")
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            current_day = str(Hetnapja(year,month,day))
            if(current_day==input_day and data[1]!= previous_title):
                previous_title = data[1]
                series_that_day.add(previous_title)

    for i in series_that_day:
        print(i)

def feladat_8():
    print("7. feladat")
    titles = []
    for data in series:
        if data[1] not in titles:
            titles.append(data[1])
            
    output_file = open('summa.txt','w')
    
    for title in titles:
        sum_time = 0
        episode_number = 0
        for data in series:
            if data[1] == title:
                sum_time += int(data[3])
                episode_number +=1       
        output_file.write(title+" "+str(sum_time)+" "+str(episode_number)+"\n")

    output_file.close()
  
feladat_1()
feladat_2()
feladat_3()
feladat_4()
##feladat_5()
##feladat_7()
feladat_8()

