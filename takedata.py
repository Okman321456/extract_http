Len_of_rq=[]
Len_of_argu=[]
Num_of_argu=[]
Num_of_digit_in_argu=[]
Len_of_path=[]
Num_of_let_in_argu=[]
Num_of_let_char_in_path=[]
Num_of_spea_char_in_path=[]
Max_byte_value_in_rq=[]
Class=[]

item_usefull=["Method","URI","Host_Header","Connection","Accept","Accept_Charset","Accept_Language","Cache_control","Cookie","Pragma","User_Agent","Content_Type","POST_Data","GET_Query"]
item_save=["Method","URI","Host_Header","Connection","Accept","Accept_Charset","Accept_Language","Cache_control","Cookie","Pragma","User_Agent","Content_Type","POST_Data","GET_Query"]
item=["Method","URI","Host_Header","Connection","Accept","Accept_Charset","Accept_Language","Cache_control","Cookie","Pragma","User_Agent","Content_Type","POST_Data","GET_Query"]
dict_item_all={}

take_item=["Method","URI","Host_Header","Connection","Accept","Accept_Language","User_Agent","POST_Data","GET_Query"]

def take_length(dic):
    S=0
    for i in dic:
        if(i in take_item):
            S+=len(dic.get(i))
    return S

file=open("csic_ecml_final.arff","r")
d=0

file.readline()
file.readline()

#take feature's name
while True:
    file_line=file.readline()
    # print(file_line[0:30])
    if("@attribute" in file_line):
        temp = file_line.find("{")
        print(temp)
        if("Method" in file_line):
            dict_item_all["Method"]=file_line[temp+1:-2]
        elif ("GET-Query" in file_line):
            dict_item_all["GET_Query"]=file_line[temp+1:-2]
        elif ("URI" in file_line):
            dict_item_all["URI"]=file_line[temp+1:-2]
        elif ("Host-Header" in file_line):
            dict_item_all["Host_Header"]=file_line[temp+1:-2]
        # elif (L[1]=="Host"):
        #     dict_item_all["Host"]=L[2][1:-2]
        elif ("Connection" in file_line):
            dict_item_all["Connection"]=file_line[temp+1:-2]
        elif ("Accept-Charset" in file_line):
            dict_item_all["Accept_Charset"]=file_line[temp+1:-2]
        elif ("Accept-Language" in file_line):
            dict_item_all["Accept_Language"]=file_line[temp+1:-2]
        elif ("Accept" in file_line):
            dict_item_all["Accept"]=file_line[temp+1:-2]
        elif ("Cache-control" in file_line):
            dict_item_all["Cache_control"]=file_line[temp+1:-2]
        elif ("Cookie" in file_line):
            dict_item_all["Cookie"]=file_line[temp+1:-2]
        elif ("Pragma" in file_line):
            dict_item_all["Pragma"]=file_line[temp+1:-2]
        elif ("User-Agent" in file_line):
            dict_item_all["User_Agent"]=file_line[temp+1:-2]
        elif ("Content-Type" in file_line):
            dict_item_all["Content_Type"]=file_line[temp+1:-2]
        elif ("POST-Data" in file_line):
            dict_item_all["POST_Data"]=file_line[temp+1:-2]
        elif ("Class" in file_line):
            dict_item_all["Class"]=file_line[temp+1:-2]
    else:
        break

#print(dict_item_all.get("Method"))
file.readline()
while True:
#for z in range(3):
    dict_item = {}
    file_line=file.readline()
    d += 1
    if not file_line:
        print("end of file")
        # print(d)
        break
    L = file_line.split(",")
    L[-1]=L[-1][:-1]
    item_count=0
    i=0
    j=0
    while j<len(L)-3:
        #print(L[j]," ",item[i])
        if(item_count==11):
            j+=1
        if(L[j]=="?"):
            i+=1
            dict_item[item[i]]=""
            item_count+=1
            #print("1 ",item[i]," ",j, ": ", dict_item.get(item[i]))
            j += 1
        elif (L[j] in dict_item_all[item[i]]):
            if item[i] in dict_item:
                dict_item[item[i]]+=","+L[j]
            elif not(item[i] in dict_item):
                dict_item[item[i]]=L[j]
                item_count += 1

            #print("2 ",item[i], " ", j, ": ", dict_item.get(item[i]))
            j += 1
        elif not(L[j] in dict_item_all[item[i]]):
            i += 1
            if (L[j] in dict_item_all[item[i]]):
                dict_item[item[i]] = L[j]
                item_count += 1
                #print("3 ",item[i], " ", j, ": ", dict_item.get(item[i]))
                j+=1
            else:
                i+=1
                if (L[j] in dict_item_all[item[i]]):
                    dict_item[item[i]] = L[j]
                    item_count += 1
                    #print("4 ",item[i], " ", j, ": ", dict_item.get(item[i]))
                    j += 1
                else:
                    i-=2
                    j += 1
    dict_item["POST_Data"]=L[-3]
    dict_item["GET_Query"]=L[-2]
    dict_item["Class"]=L[-1]
    # print(dict_item)
    if(dict_item.get("Class")=="Valid"):
        Class.append(0)
    else:
        Class.append(1)

    # Length of the request
    Len_of_rq.append(take_length(dict_item))

    # Length of the arguments
    Len_of_argu.append(len(dict_item.get("POST_Data")) + len(dict_item.get("GET_Query")))

    # Number of arguments
    if ((dict_item.get("POST_Data").strip()=="?")and(dict_item.get("GET_Query").strip()=="?")):
        Num_of_argu.append(0)
    elif (dict_item.get("POST_Data").strip()=="?"):
        Num_of_argu.append(len(dict_item.get("GET_Query").split("&")))
        print(len(dict_item.get("GET_Query").split("&")))
    elif (dict_item.get("GET_Query").strip()=="?"):
        Num_of_argu.append(len(dict_item.get("POST_Data").split("&")))
        print(len(dict_item.get("GET_Query").split("&")))
    else:
        Num_of_argu.append(0)

    path = dict_item.get("URI") + "?" + dict_item.get("GET_Query") + dict_item.get("POST_Data")

    # Length of the path
    Len_of_path.append(len(path))


    querypoint=len(dict_item.get("URI"))

    # Number of digits in the arguments
    # Number of letters in the arguments
    # Number of letter chars in the path
    # Number of the 'special' chars in the path
    temp_digit = 0
    temp_letters_in_ar = 0
    temp_letter_char_in_path = 0
    temp_spe = 0
    for i in range(querypoint):
        if (path[i].isalpha()):
            temp_letter_char_in_path+=1
    for i in range(querypoint+1,len(path)):
        if (path[i] == "%"):
            i += 2
            temp_spe += 1
        else:
            try:
                if (path[i].isalpha()):
                    temp_letters_in_ar +=1
                    temp_letter_char_in_path +=1
                int(path[i])
                temp_digit += 1
            except:
                continue

    Num_of_digit_in_argu.append(temp_digit)
    Num_of_let_in_argu.append(temp_letters_in_ar)
    Num_of_let_char_in_path.append(temp_letter_char_in_path)
    Num_of_spea_char_in_path.append(temp_spe)
    item=item_save
    print(d)

import numpy as np
import csv

data=np.array([Len_of_rq,Len_of_argu,Num_of_argu,Num_of_digit_in_argu,Len_of_path,Num_of_let_in_argu,Num_of_let_char_in_path,Num_of_spea_char_in_path,Class])
data=data.transpose()
feature=['Len_of_rq','Len_of_argu','Num_of_argu','Num_of_digit_in_argu','Len_of_path','Num_of_let_in_argu','Num_of_let_char_in_path','Num_of_spea_char_in_path','Class']


with open('.\\data_http.csv', 'w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(feature)
    writer.writerows(data)