import csv
import matplotlib.pyplot as p

MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]

def main() :
    seoul = open('seoul.csv', 'r', encoding='cp949')
    seoul_data = csv.reader(seoul, delimiter = ',')
    daejeon = open('daejeon.csv', 'r', encoding='cp949')
    daejeon_data = csv.reader(daejeon, delimiter = ',')
    busan = open('busan.csv', 'r', encoding='cp949')
    busan_data = csv.reader(busan, delimiter = ',')
    jeju = open('jeju.csv', 'r', encoding='cp949')
    jeju_data = csv.reader(jeju, delimiter = ',')
    overall = open('total.csv', 'r', encoding='cp949')
    total_data = csv.reader(overall, delimiter = ',')

    stemp = []
    dtemp = []
    btemp = []
    jtemp = []
    ttemp = []

    for row in seoul_data :
        stemp.append(float(row[2]))
    for row in daejeon_data :
        dtemp.append(float(row[2]))
    for row in busan_data :
        btemp.append(float(row[2]))
    for row in jeju_data :
        jtemp.append(float(row[2]))
    for row in total_data :
        ttemp.append(float(row[2]))

    p.title("Average Temp - Yearly")
    p.ylabel('Temp')
    p.plot(MONTH, stemp, color='red', label='Seoul')
    p.plot(MONTH, dtemp, color='orange', label='Daejeon')
    p.plot(MONTH, btemp, color='yellow', label='Busan')
    p.plot(MONTH, jtemp, color='green', label='Jeju')
    p.plot(MONTH, ttemp, color='blue', label='All')

    p.legend()
    
    p.show()
    

if __name__=="__main__" :
    main()
