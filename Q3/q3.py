import csv
import matplotlib.pyplot as p

def main():
    yearArr = ["2022", "2021", "2020"]
    
    for i in range(3):
        f = open(yearArr[i]+"jeju_population.csv", 'r', encoding='ANSI')
        data = csv.reader(f)
        header = next(data)

        total_male = 0
        total_female = 0

        for row in data:
            if '(5000000000)' in row[0]:
                    total_male += int(row[1].replace(',', ''))
                    total_female += int(row[104].replace(',', ''))
        
        
        f.close()
        
        labels = ['Male', 'Female']
        sizes = [total_male, total_female]
        colors = ['blue','red']

        p.title("Total Male and Female Populations in "+yearArr[i])

        p.barh('Female', total_female, color = colors[1], label="Female")
        p.barh('Male', total_male, color = colors[0],label="Male")
        p.xlabel('Population')
        p.legend()
        p.text(total_female, 'Female', f'{total_female:,}', va='center')
        p.text(total_male, 'Male', f'{total_male:,}', va='center')
        p.show()

        p.pie(sizes, labels=labels,colors = colors, autopct='%1.3f%%')
        p.show()

if __name__ == "__main__":
    main()
