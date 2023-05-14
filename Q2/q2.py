import matplotlib.pyplot as p
import random as r
import csv

def main():
    initCsv()       #result.csv 초기화
    writeData()     #result.csv에 데이터 쓰기
    readData()      #result.csv를 읽고 그래프 출력
    
def saveCsv(runCount, data):
    f = open('result.csv', 'a')

    f.write("\"" + str(runCount) + "\"")
    
    for d in data:
        f.write(",\""+str(d)+"\"")
        
    if not runCount == 100000:
        f.write("\n")

    f.close()

def initCsv():
    f = open('result.csv', 'w', encoding='cp949')
    f.write('''"시행 횟수","1","2","3","4","5","6"\n''')

def writeData():
    runCount = 100
    for a in range(4):
        arr = [0] * 6
        for i in range(runCount):
            rand = int(6 * r.random()+1)
            arr[rand - 1] += 1

        saveCsv(runCount, arr)
        runCount *= 10
        
def readData():
    f = open('result.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    p.title("Random")

    xVal = [1, 2, 3, 4, 5, 6]
    colorType = ['red', 'green', 'blue', 'purple']

    rowCount = 1
    
    for row in data:
        arr = [0]*6
        for i in range(6):
            arr[i] = int(row[1+i])
        p.subplot(1, 4, rowCount)
        p.bar(xVal, arr, color=colorType[rowCount-1], label=row[0])
        p.legend()
        rowCount += 1
        
    p.show()
        
main()
