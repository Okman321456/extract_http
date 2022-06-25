import csv
data_normal = []
data_anomalous=[]
with open('.\\data_http.csv','rt',encoding='utf-8')as f:
    data = csv.reader(f)
    for row in data:
        if (len(row) != 0):
            if (row[-1].strip().isalpha()):
                data_normal.append(row)
                data_anomalous.append(row)
            elif (int(row[-1])==0):
                data_normal.append(row)
            elif (int(row[-1])==1):
                data_anomalous.append(row)
                
    temp=data_anomalous[3000:5000]
    data_anomalous+=temp


with open('.\\normal_data.csv', 'w', encoding='utf-8') as fw:
    writer = csv.writer(fw)
    writer.writerows(data_normal)
with open('.\\anomalous.csv', 'w', encoding='utf-8') as fw:
    writer = csv.writer(fw)
    writer.writerows(data_anomalous)
    