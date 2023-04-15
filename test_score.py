import tkinter as tk
from tkinter import filedialog
import chardet
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import tkinter as tk
import tkinter as tk
from tkinter import filedialog,Canvas
import random
import pandas as pd
from openpyxl import load_workbook

def notdondur(cevapanahtar,cevapogrenci):
    count=0
   
    for x in range(len(cevapanahtar)):
        
        if cevapanahtar[x]==cevapogrenci[x]:
            count+=1
    return count*5

def notdondur2(cevapanahtar,cevapogrenci):
    count=0
   
    for x in range(len(cevapanahtar)):
        
        if cevapanahtar[x]==cevapogrenci[x]:
            count+=1
    return count*4
def notdondur3(cevapanahtar,cevapogrenci):
    count=0
   
    for x in range(len(cevapanahtar)):
        
        if cevapanahtar[x]==cevapogrenci[x]:
            count+=1
    return count*3.33    


def option1():
    ogretmen_not=[]
    notes=[]    
    with open(file_path, "r") as dosya:

        cevapsatiri=dosya.readline()
        if len(cevapsatiri)!=53:
            messagebox.showerror("lütfen doğru soru sayısını seçiniz")
        else:    
            liste=dosya.readlines()
            ogretmen=(cevapsatiri[32:52])
            global new_file
            new_file = filedialog.asksaveasfilename(defaultextension=".txt")
            for i in ogretmen:
                ogretmen_not.append(i) 
            for x in range(0,len(liste)):
                satir=liste[x][32:52]        
                b=notdondur(ogretmen,satir)
                notes.append(b)       
                with open(new_file,"a",encoding="utf-8") as dosyam:
                    # deger=str(liste[x][0:9]+"  "+str(b)+" "+"\n")
                    # dosyam.write(deger)
                    ilk_sutun=str(liste[x][0:9])  
                    ucuncu_sutun=str(b)
                    dosyam.write("{},{}\n".format(ilk_sutun,ucuncu_sutun))
                    dosyam.close()
            listem1=[]   
            listem2=[] 
            listem3=[]
            listem4=[]   
            listem5=[] 
            listem6=[]   
            listem7=[]   
            listem8=[] 
            listem9=[]   
            listem10=[]   
            listem11=[]
            listem12=[] 
            listem13=[]   
            listem14=[]   
            listem15=[] 
            listem16=[]   
            listem17=[]   
            listem18=[] 
            listem19=[]   
            listem20=[]   
            listem21=[] 
            listem22=[]   
            listem23=[]   
            listem24=[] 
            listem25=[]     
    for y in range(0,len(liste)):
        col1=liste[y][32:33]
        col2=liste[y][33:34]
        col3=liste[y][34:35]
        col4=liste[y][35:36]
        col5=liste[y][36:37]
        col6=liste[y][37:38]
        col7=liste[y][38:39]
        col8=liste[y][39:40]
        col9=liste[y][40:41]
        col10=liste[y][41:42]
        col11=liste[y][42:43]
        col12=liste[y][43:44]
        col13=liste[y][44:45]
        col14=liste[y][45:46]
        col15=liste[y][46:47]
        col16=liste[y][47:48]
        col17=liste[y][48:49]
        col18=liste[y][49:50]
        col19=liste[y][50:51]
        col20=liste[y][51:52]
        
        listem1.append(col1)
        listem2.append(col2)
        listem3.append(col3)
        listem4.append(col4)   
        listem5.append(col5)  
        listem6.append(col6)   
        listem7.append(col7)   
        listem8.append(col8)  
        listem9.append(col9)   
        listem10.append(col10)  
        listem11.append(col11)  
        listem12.append(col12)    
        listem13.append(col13)    
        listem14.append(col14)  
        listem15.append(col15)   
        listem16.append(col16)    
        listem17.append(col17)  
        listem18.append(col18)    
        listem19.append(col19)     
        listem20.append(col20)  
        
    dogrucevap1=ogretmen_not[0]
    dogrucevap2=ogretmen_not[1]
    dogrucevap3=ogretmen_not[2]
    dogrucevap4=ogretmen_not[3]
    dogrucevap5=ogretmen_not[4]
    dogrucevap6=ogretmen_not[5]
    dogrucevap7=ogretmen_not[6]
    dogrucevap8=ogretmen_not[7]
    dogrucevap9=ogretmen_not[8]
    dogrucevap10=ogretmen_not[9]
    dogrucevap11=ogretmen_not[10]
    dogrucevap12=ogretmen_not[11]
    dogrucevap13=ogretmen_not[12]
    dogrucevap14=ogretmen_not[13]
    dogrucevap15=ogretmen_not[14]
    dogrucevap16=ogretmen_not[15]
    dogrucevap17=ogretmen_not[16]
    dogrucevap18=ogretmen_not[17]
    dogrucevap19=ogretmen_not[18]
    dogrucevap20=ogretmen_not[19]
    
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    count11=0
    count12=0
    count13=0
    count14=0
    count15=0
    count16=0
    count17=0
    count18=0
    count19=0
      
    for a in listem1:
        if dogrucevap1==a:
            count+=1

    for a in listem2:
        if dogrucevap2==a:
            count1+=1

    for a in listem3:
        if dogrucevap3==a:
            count2+=1

    for a in listem4:
        if dogrucevap4==a:
            count3+=1

    for a in listem5:
        if dogrucevap5==a:  
            count4+=1
    for a in listem6:
        if dogrucevap6==a:
            count5+=1       
    for a in listem7:
        if dogrucevap7==a:
            count6+=1       
    for a in listem8:
        if dogrucevap8==a:
            count7+=1       
    for a in listem9:
        if dogrucevap9==a:
            count8+=1       
    for a in listem10:
        if dogrucevap10==a:
            count9+=1       
    for a in listem11:
        if dogrucevap11==a:
            count10+=1       
    for a in listem12:
        if dogrucevap12==a:
            count11+=1       
    for a in listem13:
        if dogrucevap13==a:
            count12+=1       
    for a in listem14:
        if dogrucevap14==a:
            count13+=1       
    for a in listem15:
        if dogrucevap15==a:
            count14+=1       
    for a in listem16:
        if dogrucevap16==a:
            count15+=1       
    for a in listem17:
        if dogrucevap17==a:
            count16+=1       
    for a in listem18:
        if dogrucevap18==a:
            count17+=1       
    for a in listem19:
        if dogrucevap19==a:
            count18+=1       
    for a in listem20:
        if dogrucevap20==a:
            count19+=1                                                                           
           
    soru_puan=4
    sayi=len(liste)
    #1. soru için oran
    oran_1=(soru_puan/sayi)*count
    oran_2=(soru_puan/sayi)*count1
    oran_3=(soru_puan/sayi)*count2
    oran_4=(soru_puan/sayi)*count3
    oran_5=(soru_puan/sayi)*count4
    oran_6=(soru_puan/sayi)*count5
    oran_7=(soru_puan/sayi)*count6
    oran_8=(soru_puan/sayi)*count7
    oran_9=(soru_puan/sayi)*count8
    oran_10=(soru_puan/sayi)*count9
    oran_11=(soru_puan/sayi)*count10
    oran_12=(soru_puan/sayi)*count11
    oran_13=(soru_puan/sayi)*count12
    oran_14=(soru_puan/sayi)*count13
    oran_15=(soru_puan/sayi)*count14
    oran_16=(soru_puan/sayi)*count15
    oran_17=(soru_puan/sayi)*count16
    oran_18=(soru_puan/sayi)*count17
    oran_19=(soru_puan/sayi)*count18
    oran_20=(soru_puan/sayi)*count19
   
    value=[oran_1,oran_2,oran_3,oran_4,oran_5,oran_6,oran_7,oran_8,oran_9,oran_10,oran_11,oran_12,oran_13,oran_14,oran_15,oran_16,oran_17,oran_18,oran_19,oran_20]
    name=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    plt.bar(name,value)
   
    # global goster
    fig, ax = plt.subplots()
    ax.bar(name,value)
    global canvas1
    canvas1 = FigureCanvasTkAgg(fig, master=root)     
    canvas1.draw()        
    canvas1.get_tk_widget().pack()
    canvas2.get_tk_widget().destroy()
    canvas3.get_tk_widget().destroy()
    ax.set_xlabel("sorular")
    ax.set_ylabel("sorudan alınan puan ortalaması")
    ax.set_title("soru başına sınıf puan ortalaması")     
def option2():
    ogretmen_not=[]
    notes=[]    
    with open(file_path, "r") as dosya:

        cevapsatiri=dosya.readline()
        if len(cevapsatiri)!=58:
            messagebox.showerror("lütfen doğru soru sayısını seçiniz")
        else:    
            liste=dosya.readlines()
            ogretmen=(cevapsatiri[32:57])
            global new_file
            new_file = filedialog.asksaveasfilename(defaultextension=".txt")
            for i in ogretmen:
                ogretmen_not.append(i) 
            for x in range(0,len(liste)):
                satir=liste[x][32:57]        
                b=notdondur2(ogretmen,satir)
                notes.append(b)   
                
                with open(new_file,"a",encoding="utf-8") as dosyam:
                    # deger=str(liste[x][0:9]+"  "+str(b)+" "+"\n")
                    # dosyam.write(deger)
                    ilk_sutun=str(liste[x][0:9])  
                    ucuncu_sutun=str(b)
                    dosyam.write("{},{}\n".format(ilk_sutun,ucuncu_sutun))
                    dosyam.close()
            listem1=[]   
            listem2=[] 
            listem3=[]
            listem4=[]   
            listem5=[] 
            listem6=[]   
            listem7=[]   
            listem8=[] 
            listem9=[]   
            listem10=[]   
            listem11=[]
            listem12=[] 
            listem13=[]   
            listem14=[]   
            listem15=[] 
            listem16=[]   
            listem17=[]   
            listem18=[] 
            listem19=[]   
            listem20=[]   
            listem21=[] 
            listem22=[]   
            listem23=[]   
            listem24=[] 
            listem25=[]     
    for y in range(0,len(liste)):
        col1=liste[y][32:33]
        col2=liste[y][33:34]
        col3=liste[y][34:35]
        col4=liste[y][35:36]
        col5=liste[y][36:37]
        col6=liste[y][37:38]
        col7=liste[y][38:39]
        col8=liste[y][39:40]
        col9=liste[y][40:41]
        col10=liste[y][41:42]
        col11=liste[y][42:43]
        col12=liste[y][43:44]
        col13=liste[y][44:45]
        col14=liste[y][45:46]
        col15=liste[y][46:47]
        col16=liste[y][47:48]
        col17=liste[y][48:49]
        col18=liste[y][49:50]
        col19=liste[y][50:51]
        col20=liste[y][51:52]
        col21=liste[y][52:53]
        col22=liste[y][53:54]
        col23=liste[y][54:55]
        col24=liste[y][55:56]
        col25=liste[y][56:57]    
        listem1.append(col1)
        listem2.append(col2)
        listem3.append(col3)
        listem4.append(col4)   
        listem5.append(col5)  
        listem6.append(col6)   
        listem7.append(col7)   
        listem8.append(col8)  
        listem9.append(col9)   
        listem10.append(col10)  
        listem11.append(col11)  
        listem12.append(col12)    
        listem13.append(col13)    
        listem14.append(col14)  
        listem15.append(col15)   
        listem16.append(col16)    
        listem17.append(col17)  
        listem18.append(col18)    
        listem19.append(col19)     
        listem20.append(col20)  
        listem21.append(col21)   
        listem22.append(col22)     
        listem23.append(col23)  
        listem24.append(col24) 
        listem25.append(col25)
    dogrucevap1=ogretmen_not[0]
    dogrucevap2=ogretmen_not[1]
    dogrucevap3=ogretmen_not[2]
    dogrucevap4=ogretmen_not[3]
    dogrucevap5=ogretmen_not[4]
    dogrucevap6=ogretmen_not[5]
    dogrucevap7=ogretmen_not[6]
    dogrucevap8=ogretmen_not[7]
    dogrucevap9=ogretmen_not[8]
    dogrucevap10=ogretmen_not[9]
    dogrucevap11=ogretmen_not[10]
    dogrucevap12=ogretmen_not[11]
    dogrucevap13=ogretmen_not[12]
    dogrucevap14=ogretmen_not[13]
    dogrucevap15=ogretmen_not[14]
    dogrucevap16=ogretmen_not[15]
    dogrucevap17=ogretmen_not[16]
    dogrucevap18=ogretmen_not[17]
    dogrucevap19=ogretmen_not[18]
    dogrucevap20=ogretmen_not[19]
    dogrucevap21=ogretmen_not[20]
    dogrucevap22=ogretmen_not[21]
    dogrucevap23=ogretmen_not[22]
    dogrucevap24=ogretmen_not[23]
    dogrucevap25=ogretmen_not[24]
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    count11=0
    count12=0
    count13=0
    count14=0
    count15=0
    count16=0
    count17=0
    count18=0
    count19=0
    count20=0
    count21=0
    count22=0
    count23=0
    count24=0   
    for a in listem1:
        if dogrucevap1==a:
            count+=1

    for a in listem2:
        if dogrucevap2==a:
            count1+=1

    for a in listem3:
        if dogrucevap3==a:
            count2+=1

    for a in listem4:
        if dogrucevap4==a:
            count3+=1

    for a in listem5:
        if dogrucevap5==a:  
            count4+=1
    for a in listem6:
        if dogrucevap6==a:
            count5+=1       
    for a in listem7:
        if dogrucevap7==a:
            count6+=1       
    for a in listem8:
        if dogrucevap8==a:
            count7+=1       
    for a in listem9:
        if dogrucevap9==a:
            count8+=1       
    for a in listem10:
        if dogrucevap10==a:
            count9+=1       
    for a in listem11:
        if dogrucevap11==a:
            count10+=1       
    for a in listem12:
        if dogrucevap12==a:
            count11+=1       
    for a in listem13:
        if dogrucevap13==a:
            count12+=1       
    for a in listem14:
        if dogrucevap14==a:
            count13+=1       
    for a in listem15:
        if dogrucevap15==a:
            count14+=1       
    for a in listem16:
        if dogrucevap16==a:
            count15+=1       
    for a in listem17:
        if dogrucevap17==a:
            count16+=1       
    for a in listem18:
        if dogrucevap18==a:
            count17+=1       
    for a in listem19:
        if dogrucevap19==a:
            count18+=1       
    for a in listem20:
        if dogrucevap20==a:
            count19+=1                                                                           
    for a in listem21:
        if dogrucevap21==a:
            count20+=1   
    for a in listem22:
        if dogrucevap22==a:
            count21+=1           
    for a in listem23:
        if dogrucevap23==a:
            count22+=1   
    for a in listem24:
        if dogrucevap24==a:
            count23+=1           
    for a in listem25:
        if dogrucevap25==a:
            count24+=1           
    soru_puan=4
    sayi=len(liste)
    #1. soru için oran
    oran_1=(soru_puan/sayi)*count
    oran_2=(soru_puan/sayi)*count1
    oran_3=(soru_puan/sayi)*count2
    oran_4=(soru_puan/sayi)*count3
    oran_5=(soru_puan/sayi)*count4
    oran_6=(soru_puan/sayi)*count5
    oran_7=(soru_puan/sayi)*count6
    oran_8=(soru_puan/sayi)*count7
    oran_9=(soru_puan/sayi)*count8
    oran_10=(soru_puan/sayi)*count9
    oran_11=(soru_puan/sayi)*count10
    oran_12=(soru_puan/sayi)*count11
    oran_13=(soru_puan/sayi)*count12
    oran_14=(soru_puan/sayi)*count13
    oran_15=(soru_puan/sayi)*count14
    oran_16=(soru_puan/sayi)*count15
    oran_17=(soru_puan/sayi)*count16
    oran_18=(soru_puan/sayi)*count17
    oran_19=(soru_puan/sayi)*count18
    oran_20=(soru_puan/sayi)*count19
    oran_21=(soru_puan/sayi)*count20
    oran_22=(soru_puan/sayi)*count21
    oran_23=(soru_puan/sayi)*count22
    oran_24=(soru_puan/sayi)*count23
    oran_25=(soru_puan/sayi)*count24
    value=[oran_1,oran_2,oran_3,oran_4,oran_5,oran_6,oran_7,oran_8,oran_9,oran_10,oran_11,oran_12,oran_13,oran_14,oran_15,oran_16,oran_17,oran_18,oran_19,oran_20,oran_21,oran_22,oran_23,oran_24,oran_25]
    name=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",]
    plt.bar(name,value)
   
    # global goster
    fig, ax = plt.subplots()
    ax.bar(name,value)
    global canvas2
    
    canvas2 = FigureCanvasTkAgg(fig, master=root)     
    canvas2.draw()        
    canvas2.get_tk_widget().pack()
    canvas1.get_tk_widget().destroy()
    canvas3.get_tk_widget().destroy()
    ax.set_xlabel("sorular")
    ax.set_ylabel("sorudan alınan puan ortalaması")
    ax.set_title("soru başına sınıf puan ortalaması")            
def option3():
    ogretmen_not=[]
    notes=[]    
    with open(file_path, "r") as dosya:

        cevapsatiri=dosya.readline()
        if len(cevapsatiri)!=63:
            messagebox.showerror("lütfen doğru soru sayısını seçiniz")
        else:    
            liste=dosya.readlines()
            ogretmen=(cevapsatiri[32:62])
            global new_file
            new_file = filedialog.asksaveasfilename(defaultextension=".txt")
            for i in ogretmen:
                ogretmen_not.append(i) 
            for x in range(0,len(liste)):
                satir=liste[x][32:62]        
                b=notdondur2(ogretmen,satir)
                notes.append(b)       
                with open(new_file,"a",encoding="utf-8") as dosyam:
                    # deger=str(liste[x][0:9]+"  "+str(b)+" "+"\n")
                    # dosyam.write(deger)
                    ilk_sutun=str(liste[x][0:9])  
                    ucuncu_sutun=str(b)
                    dosyam.write("{},{}\n".format(ilk_sutun,ucuncu_sutun))
                    dosyam.close()
            listem1=[]   
            listem2=[] 
            listem3=[]
            listem4=[]   
            listem5=[] 
            listem6=[]   
            listem7=[]   
            listem8=[] 
            listem9=[]   
            listem10=[]   
            listem11=[]
            listem12=[] 
            listem13=[]   
            listem14=[]   
            listem15=[] 
            listem16=[]   
            listem17=[]   
            listem18=[] 
            listem19=[]   
            listem20=[]   
            listem21=[] 
            listem22=[]   
            listem23=[]   
            listem24=[] 
            listem25=[]
            listem26=[]
            listem27=[]
            listem28=[]
            listem29=[]
            listem30=[]     
    for y in range(0,len(liste)):
        col1=liste[y][32:33]
        col2=liste[y][33:34]
        col3=liste[y][34:35]
        col4=liste[y][35:36]
        col5=liste[y][36:37]
        col6=liste[y][37:38]
        col7=liste[y][38:39]
        col8=liste[y][39:40]
        col9=liste[y][40:41]
        col10=liste[y][41:42]
        col11=liste[y][42:43]
        col12=liste[y][43:44]
        col13=liste[y][44:45]
        col14=liste[y][45:46]
        col15=liste[y][46:47]
        col16=liste[y][47:48]
        col17=liste[y][48:49]
        col18=liste[y][49:50]
        col19=liste[y][50:51]
        col20=liste[y][51:52]
        col21=liste[y][52:53]
        col22=liste[y][53:54]
        col23=liste[y][54:55]
        col24=liste[y][55:56]
        col25=liste[y][56:57]
        col26=liste[y][57:58]  
        col27=liste[y][58:59]  
        col28=liste[y][59:60]  
        col29=liste[y][60:61]
        col30=liste[y][61:62]        
        listem1.append(col1)
        listem2.append(col2)
        listem3.append(col3)
        listem4.append(col4)   
        listem5.append(col5)  
        listem6.append(col6)   
        listem7.append(col7)   
        listem8.append(col8)  
        listem9.append(col9)   
        listem10.append(col10)  
        listem11.append(col11)  
        listem12.append(col12)    
        listem13.append(col13)    
        listem14.append(col14)  
        listem15.append(col15)   
        listem16.append(col16)    
        listem17.append(col17)  
        listem18.append(col18)    
        listem19.append(col19)     
        listem20.append(col20)  
        listem21.append(col21)   
        listem22.append(col22)     
        listem23.append(col23)  
        listem24.append(col24) 
        listem25.append(col25)
        listem26.append(col26)
        listem27.append(col27)
        listem28.append(col28)
        listem29.append(col29)
        listem30.append(col30)
    dogrucevap1=ogretmen_not[0]
    dogrucevap2=ogretmen_not[1]
    dogrucevap3=ogretmen_not[2]
    dogrucevap4=ogretmen_not[3]
    dogrucevap5=ogretmen_not[4]
    dogrucevap6=ogretmen_not[5]
    dogrucevap7=ogretmen_not[6]
    dogrucevap8=ogretmen_not[7]
    dogrucevap9=ogretmen_not[8]
    dogrucevap10=ogretmen_not[9]
    dogrucevap11=ogretmen_not[10]
    dogrucevap12=ogretmen_not[11]
    dogrucevap13=ogretmen_not[12]
    dogrucevap14=ogretmen_not[13]
    dogrucevap15=ogretmen_not[14]
    dogrucevap16=ogretmen_not[15]
    dogrucevap17=ogretmen_not[16]
    dogrucevap18=ogretmen_not[17]
    dogrucevap19=ogretmen_not[18]
    dogrucevap20=ogretmen_not[19]
    dogrucevap21=ogretmen_not[20]
    dogrucevap22=ogretmen_not[21]
    dogrucevap23=ogretmen_not[22]
    dogrucevap24=ogretmen_not[23]
    dogrucevap25=ogretmen_not[24]
    dogrucevap26=ogretmen_not[25]
    dogrucevap27=ogretmen_not[26]
    dogrucevap28=ogretmen_not[27]
    dogrucevap29=ogretmen_not[28]
    dogrucevap30=ogretmen_not[29]

    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    count11=0
    count12=0
    count13=0
    count14=0
    count15=0
    count16=0
    count17=0
    count18=0
    count19=0
    count20=0
    count21=0
    count22=0
    count23=0
    count24=0
    count25=0  
    count26=0  
    count27=0  
    count28=0  
    count29=0  
    for a in listem1:
        if dogrucevap1==a:
            count+=1

    for a in listem2:
        if dogrucevap2==a:
            count1+=1

    for a in listem3:
        if dogrucevap3==a:
            count2+=1

    for a in listem4:
        if dogrucevap4==a:
            count3+=1

    for a in listem5:
        if dogrucevap5==a:  
            count4+=1
    for a in listem6:
        if dogrucevap6==a:
            count5+=1       
    for a in listem7:
        if dogrucevap7==a:
            count6+=1       
    for a in listem8:
        if dogrucevap8==a:
            count7+=1       
    for a in listem9:
        if dogrucevap9==a:
            count8+=1       
    for a in listem10:
        if dogrucevap10==a:
            count9+=1       
    for a in listem11:
        if dogrucevap11==a:
            count10+=1       
    for a in listem12:
        if dogrucevap12==a:
            count11+=1       
    for a in listem13:
        if dogrucevap13==a:
            count12+=1       
    for a in listem14:
        if dogrucevap14==a:
            count13+=1       
    for a in listem15:
        if dogrucevap15==a:
            count14+=1       
    for a in listem16:
        if dogrucevap16==a:
            count15+=1       
    for a in listem17:
        if dogrucevap17==a:
            count16+=1       
    for a in listem18:
        if dogrucevap18==a:
            count17+=1       
    for a in listem19:
        if dogrucevap19==a:
            count18+=1       
    for a in listem20:
        if dogrucevap20==a:
            count19+=1                                                                           
    for a in listem21:
        if dogrucevap21==a:
            count20+=1   
    for a in listem22:
        if dogrucevap22==a:
            count21+=1           
    for a in listem23:
        if dogrucevap23==a:
            count22+=1   
    for a in listem24:
        if dogrucevap24==a:
            count23+=1           
    for a in listem25:
        if dogrucevap25==a:
            count24+=1  
    for a in listem26:
        if dogrucevap26==a:
            count25+=1  
    for a in listem27:
        if dogrucevap27==a:
            count26+=1 
    for a in listem28:
        if dogrucevap28==a:
            count27+=1 
    for a in listem29:
        if dogrucevap29==a:
            count28+=1 
    for a in listem30:
        if dogrucevap30==a:
            count29+=1 

    soru_puan=3.33
    sayi=len(liste)
    #1. soru için oran
    oran_1=(soru_puan/sayi)*count
    oran_2=(soru_puan/sayi)*count1
    oran_3=(soru_puan/sayi)*count2
    oran_4=(soru_puan/sayi)*count3
    oran_5=(soru_puan/sayi)*count4
    oran_6=(soru_puan/sayi)*count5
    oran_7=(soru_puan/sayi)*count6
    oran_8=(soru_puan/sayi)*count7
    oran_9=(soru_puan/sayi)*count8
    oran_10=(soru_puan/sayi)*count9
    oran_11=(soru_puan/sayi)*count10
    oran_12=(soru_puan/sayi)*count11
    oran_13=(soru_puan/sayi)*count12
    oran_14=(soru_puan/sayi)*count13
    oran_15=(soru_puan/sayi)*count14
    oran_16=(soru_puan/sayi)*count15
    oran_17=(soru_puan/sayi)*count16
    oran_18=(soru_puan/sayi)*count17
    oran_19=(soru_puan/sayi)*count18
    oran_20=(soru_puan/sayi)*count19
    oran_21=(soru_puan/sayi)*count20
    oran_22=(soru_puan/sayi)*count21
    oran_23=(soru_puan/sayi)*count22
    oran_24=(soru_puan/sayi)*count23
    oran_25=(soru_puan/sayi)*count24
    oran_26=(soru_puan/sayi)*count25
    oran_27=(soru_puan/sayi)*count26
    oran_28=(soru_puan/sayi)*count27
    oran_29=(soru_puan/sayi)*count28
    oran_30=(soru_puan/sayi)*count29
    value=[oran_1,oran_2,oran_3,oran_4,oran_5,oran_6,oran_7,oran_8,oran_9,oran_10,oran_11,oran_12,oran_13,oran_14,oran_15,oran_16,oran_17,oran_18,oran_19,oran_20,oran_21,oran_22,oran_23,oran_24,oran_25,oran_26,oran_27,oran_28,oran_29,oran_30]
    name=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
    rounded_list = [round(x) for x in value]


    plt.bar(name,rounded_list)
   
    # global goster
    fig, ax = plt.subplots()
    ax.bar(name,value)
    global canvas3
    canvas3 = FigureCanvasTkAgg(fig, master=root)     
    canvas3.draw()        
    canvas3.get_tk_widget().pack()
    canvas1.get_tk_widget().destroy()
    canvas2.get_tk_widget().destroy()
    ax.set_xlabel("sorular")
    ax.set_ylabel("sorudan alınan puan ortalaması")
    ax.set_title("soru başına sınıf puan ortalaması")                       

def show_info():
    messagebox.showinfo("Bilgi", "Önce txt seç butonundan doğru formattaki txt dosyamızı seçelim ve açılan 2.pencerede dosyaya bir isim veriniz daha sonra excell dosyası seç butonuna tıklayarak notların içine yazdırılmasını istediğiniz excel dosyasını seçiniz.")                
def select_file():
    global file_path
    root = tk.Tk()
    root.withdraw()

    file_path =filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    encoding = chardet.detect(open(file_path, 'rb').read())['encoding']
    if encoding != 'ISO-8859-1':
        messagebox.showerror("Hata", "Lütfen doğru  bir dosya seçtiğinize emin olunuz")
        select_file()
    else:
        messagebox.showinfo("seçim yapınız","lütfen soru sayınızı seçiniz")

def select_excel_file():
    filename = filedialog.askopenfilename(filetypes = (("Excel files", "*.xlsx"), ("all files", "*.*")))
    with open(new_file, "r") as file:
        data = file.readlines()
    ogrenciler = []
    for line in data:
        ogrenci = line.strip().split(",")
        ogrenciler.append(ogrenci)

    # excel dosyasını okuma
    excel_data = pd.read_excel(filename)

    # txt dosyasındaki verileri excel dosyasına yazma
    for ogrenci in ogrenciler:
        numara = ogrenci[0]
        puan = ogrenci[1]
        for index, row in excel_data.iterrows():
            
            
            if int(numara) == int(row["no"]) :            
                excel_data.at[index, "puan"] = int(puan)

    # değişiklikleri kaydetme
    excel_data.to_excel(filename, index=False)
    wb = load_workbook(filename)
    ws = wb.active

    # sütun genişliğini ayarlamak
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 12

    # dosyayı kaydetme
    wb.save(filename)
    messagebox.showinfo("Bilgi","işleminiz Başarıyla Tamamlnamıştır")
root = tk.Tk()
root.geometry("700x700")
file_button = tk.Button(root, text="Select txt file", command=select_file)
file_button.pack()

info_button = tk.Button(text="Yardım", command=show_info)
info_button.place(x=5, y=5)

var = tk.StringVar(value='2')

option1_rb = tk.Radiobutton(root, text='20soru', variable=var, value='1', command=option1)
option1_rb.pack()

option2_rb = tk.Radiobutton(root, text='25soru', variable=var, value='2', command=option2)
option2_rb.pack()

option3_rb = tk.Radiobutton(root, text='30soru', variable=var, value='3', command=option3)
option3_rb.pack()
excel_button = tk.Button(text="Excel Dosyası Seç", command=select_excel_file)
excel_button.pack()
root.title("not hesapla")
root.mainloop()