import tkinter
import time

T = time.time()
window = tkinter.Tk()
window.title('包材BOM表資料系統')
window.geometry('700x300')


def add_number():#----------------------------------------------------新增材料料號
    f = open('包材資料庫.txt','a+')   
    f.seek(0)
    for line in f:
        key = line[0:10]
        values1 = line[13:29]
        values2 = line[32:67]
        values3 = line[70:75]
        dmaterial[key] = [values1, values2, values3]
    
    #print(dmaterial)
    n1, n2, n3, n31 = num1.get(), num2.get(), num3.get(), num31.get()
    n11 = "{:<10s}".format(n1)
    n22 = "{: <16s}".format(n2)
    n33 = "{: <35s}".format(n3)
    n3131 = "{: <5s}".format(n31)
    for k in dmaterial.keys():
        if n33 in dmaterial[k][1]:
            result.set('此規格已有存在料號')
            break
        elif len(n11) > 10:
            result.set('料號格式錯誤')
            break
        elif n11 in k or n1 == '' or n2 == '' or n3 == '' or n31 == '':
            result.set('料號已存在或未輸入')
            break
    else:
        word = n11 + "---" + n22 + "---" + n33 + "---" + n3131 + "\n"
        f.write(word)
        f.flush()
        time.sleep(3)
        result.set('新增完成')
    #print(dmaterial)
    f.close()
    num1.set('')
    num2.set('')
    num3.set('')
    num31.set('')


def find_number():#----------------------------------------------------搜尋材料料號
    f = open('包材資料庫.txt','a+')   
    f.seek(0)
    for line in f:
        key = line[0:10]
        values1 = line[13:29]
        values2 = line[32:67]
        values3 = line[70:75]
        dmaterial[key] = [values1, values2, values3]
    n4 = num4.get()
    n44 = "{:<10s}".format(n4)
    if n44 not in dmaterial.keys():
        result2.set('此料號未建立')
    elif n4 == '':
        result2.set('料號未輸入')
    else:
        num5.set(dmaterial[n44][0])
        num6.set(dmaterial[n44][1])
        num7.set(dmaterial[n44][2])
        time.sleep(3)
        result2.set('搜尋完成')
    f.close()


def change_number():#----------------------------------------------------搜尋材料料號
    f = open('包材資料庫.txt','r+')   
    #f.seek(0)
    for line in f:
        key = line[0:10]
        values1 = line[13:29]
        values2 = line[32:67]
        values3 = line[70:75]
        dmaterial[key] = [values1, values2, values3]    
    n4, n5, n6, n7 = num4.get(), num5.get(), num6.get(), num7.get()
    n44 = "{:<10s}".format(n4)
    n55 = "{: <16s}".format(n5)
    n66 = "{: <35s}".format(n6)
    n77 = "{: <5s}".format(n7)
    
    if n4 == '' or n5 == '' or n6 == '' or n7 == '':
        #print(dmaterial)
        result2.set('未輸入完整')
        f.close()
        
    else:
        dmaterial[n44] = [n55, n66, n77]
        f.seek(0)
        for k in dmaterial.keys():  
            word1 = "{}".format(k) + "---" + "{}".format(dmaterial[k][0]) + "---" + "{}".format(dmaterial[k][1]) + "---" + "{}".format(dmaterial[k][2]) + "\n"
            f.write(word1)
            f.flush()
            time.sleep(1)
        result2.set('修改完成')
        f.close()
        num4.set('')
        num5.set('')
        num6.set('')
        num7.set('')

def find_number_forBOM():#----------------------------------------------------在機種包材BOM表下搜尋材料料號
    f = open('包材資料庫.txt','r')   
    f.seek(0)
    for line in f:
        key = line[0:10]
        values1 = line[13:29]
        values2 = line[32:67]
        values3 = line[70:75]
        dmaterial[key] = [values1, values2, values3]
    n9 = num9.get()
    n99 = "{:<10s}".format(n9)
    if n99 not in dmaterial.keys():
        time.sleep(3)
        result11.set('此料號未建立')
    if n9 == '':
        result11.set('未輸入完整')
    if n99 in dmaterial.keys():
        result_name.set(dmaterial[n99][0])
        result_rule.set(dmaterial[n99][1])
        time.sleep(3)
        result11.set('搜尋完成') 
    f.close()

def add_number_forBOM():#----------------------------------------------------新增機種包材BOM
    f = open('包材資料庫.txt','r')   
    f.seek(0)
    for line in f:
        key = line[0:10]
        values1 = line[13:29]
        values2 = line[32:67]
        values3 = line[70:75]
        dmaterial[key] = [values1, values2, values3]

    w = open('產品包材BOM資料庫.txt','a+')   
    w.seek(0)
    for line in w:
        keyB = line[0:11]
        valuesB1 = line[14:94]
        valuesB2 = line[97:177]
        valuesB3 = line[180:260]
        valuesB4 = line[263:343]
        valuesB5 = line[346:426]
        valuesB6 = line[429:509]
        valuesB7 = line[512:592]
        valuesB8 = line[595:675]
        dBom[keyB] = [valuesB1, valuesB2, valuesB3, valuesB4, valuesB5, valuesB5, valuesB6, valuesB7, valuesB8]
      

    n8, n9, n10 = num8.get(),num9.get(), num10.get()
    n88 = "{:<11s}".format(n8)
    n99 = "{:<10s}".format(n9)
    n1010 = "{:<10s}".format(n10)
    
    if n88 in dBom.keys():
        w.close()
        w_addmaterial = open('產品包材BOM資料庫.txt','r+')
        if n99 == dBom[n88][0][0:10] or n99 == dBom[n88][1][0:10] or n99 == dBom[n88][2][0:10] or n99 == dBom[n88][3][0:10] or n99 == dBom[n88][4][0:10] or n99 == dBom[n88][5][0:10] or n99 == dBom[n88][6][0:10] or n99 == dBom[n88][7][0:10]:
            result11.set('此機種已存在此料號')
        elif len(n88) > 11 or n9 == '' or n10 == '':
            result11.set('未輸入正確')
        else:
            N = 0
            for v in dBom[n88]:
                N += 1
                if v == "#         ---#               ---#                                  ---#         ":
                    dBom[n88][N - 1] = n99 + "---" + dmaterial[n99][0] + "---" + dmaterial[n99][1] + "---" + n1010
                    break
            else:
                result11.set('已無法加入')
                        
            for k in dBom.keys():
                word1 = k + "===" + dBom[k][0] + "===" + dBom[k][1] + "===" + dBom[k][2] + "===" + dBom[k][3] + "===" + dBom[k][4] + "===" + dBom[k][5] + "===" + dBom[k][6] + "===" + dBom[k][7] + "\n"
                w_addmaterial.write(word1)
                w_addmaterial.flush()
                time.sleep(3)
                result11.set('新增完成')
            w_addmaterial.close()
    elif n8 == '' or n9 == '' or n10 == '':
        result11.set('未輸入完整')
        w.close()
    else:
        word = n88 + "===" + n99 + "---" + "{: <16s}".format(dmaterial[n9][0]) + "---" + "{: <35s}".format(dmaterial[n9][1]) + "---" + n1010
        for _ in range(7):
            word = word + "===" + "{:<10s}".format('#') + "---" + "{: <16s}".format('#') + "---" + "{: <35s}".format('#') + "---" + "{:<10s}".format('#')
        word = word + "\n"
        w.write(word)
        w.flush()
        time.sleep(1)
        result11.set('新增完成')
        w.close()
    num8.set('')
    num9.set('')
    num10.set('')

def find_production_forBOM():#----------------------------------------------------搜尋機種包材BOM
    w = open('產品包材BOM資料庫.txt','r')
    for line in w:
        keyB = line[0:11]
        valuesB1 = line[14:94]
        valuesB2 = line[97:177]
        valuesB3 = line[180:260]
        valuesB4 = line[263:343]
        valuesB5 = line[346:426]
        valuesB6 = line[429:509]
        valuesB7 = line[512:592]
        valuesB8 = line[595:675]
        dBom[keyB] = [valuesB1, valuesB2, valuesB3, valuesB4, valuesB5, valuesB5, valuesB6, valuesB7, valuesB8]

    n8 = num8.get()
    n88 = "{:<11s}".format(n8)
    keyword = n88 + '\n'
    if n8 == '':
        result_P.set('料號未輸入')
        w.close()
    elif n88 not in dBom.keys() or len(n88) > 11:
        result_P.set('無此機種型名')
        w.close()
    else:
        txt = ''
        for i in dBom[n88]:
            txt = txt + i + '\n'
        window = tkinter.Tk()
        window.title('機種包材BOM表')
        text = tkinter.Text(window, width=90, height=15, wrap='word')
        text.pack()
        text.insert('end', keyword)
        text.insert('end', txt)
        w.close()
        num8.set('')
    

            
dmaterial = dict()
dBom = dict()

#===========================================新增材料
num1 = tkinter.StringVar()
num2 = tkinter.StringVar()
num3 = tkinter.StringVar()
num31 = tkinter.StringVar()
result = tkinter.StringVar()

Sample_ID_item = tkinter.Entry(window, width=15, textvariable=num1)
Sample_name_item = tkinter.Entry(window, width=16, textvariable=num2)
Sample_rule_item = tkinter.Entry(window, width=35, textvariable=num3)
Sample_number_item = tkinter.Entry(window, width=5, textvariable=num31)

Sample_ID_item.grid(row=1, column=0) 
Sample_name_item.grid(row=1, column=1)
Sample_rule_item.grid(row=1, column=2)
Sample_number_item.grid(row=1, column=3)


btn1 = tkinter.Button(window, width=15, text='新增新材料號', command=add_number)
btn1.grid(row=2, column=0)

label = tkinter.Label(window, width=15, textvariable=result)
label.grid(row=2, column=1)

Sample_ID_label = tkinter.Label(window, width=15, text='新材料號')
Sample_ID_label.grid(row=0, column=0)

Sample_name_label = tkinter.Label(window, width=16, text='品名')
Sample_name_label.grid(row=0, column=1)

Sample_rule_label = tkinter.Label(window, width=35, text='規格')
Sample_rule_label.grid(row=0, column=2)

Sample_number_label = tkinter.Label(window, width=5, text='數量')
Sample_number_label.grid(row=0, column=3)

                            

#=============================================修改材料規格

num4 = tkinter.StringVar()
num5 = tkinter.StringVar()
num6 = tkinter.StringVar()
num7 = tkinter.StringVar()


Findsample_ID_item = tkinter.Entry(window, width=15, textvariable=num4)
Findsample_ID_item.grid(row=4, column=0)
Findsample_name_item = tkinter.Entry(window, width=16, textvariable=num5)
Findsample_name_item.grid(row=4, column=1) 
Findsample_rule_item = tkinter.Entry(window, width=35, textvariable=num6)
Findsample_rule_item.grid(row=4, column=2)
Findsample_number_item = tkinter.Entry(window, width=5, textvariable=num7)
Findsample_number_item.grid(row=4, column=3)

result2 = tkinter.StringVar()

labe2 = tkinter.Label(window, width=15, textvariable=result2)
labe2.grid(row=6, column=2)


Findsample_ID_label = tkinter.Label(window, width=15, text='查詢修改材料號')
Findsample_ID_label.grid(row=3, column=0)
Findsample_name_label = tkinter.Label(window, width=16, text='品名')
Findsample_name_label.grid(row=3, column=1)
Findsample_rule_label = tkinter.Label(window, width=35, text='規格')
Findsample_rule_label.grid(row=3, column=2)
Findsample_number_label = tkinter.Label(window, width=5, text='數量')
Findsample_number_label.grid(row=3, column=3)

btn2 = tkinter.Button(window, width=15, text='搜尋料號', command=find_number)
btn2.grid(row=6, column=0)

btn3 = tkinter.Button(window, width=15, text='進行修改', command=change_number)
btn3.grid(row=6, column=1)

#=========================================================機種BOM表新增及修改

num8 = tkinter.StringVar()
num9 = tkinter.StringVar()
num10 = tkinter.StringVar()

BOM_ProductionID_item = tkinter.Entry(window, width=15, textvariable=num8)
BOM_ProductionID_item.grid(row=9, column=0)

BOM_MaterialID_item = tkinter.Entry(window, width=15, textvariable=num9)
BOM_MaterialID_item.grid(row=11, column=0)

BOM_MaterialUsenumber_item = tkinter.Entry(window, width=10, textvariable=num10)
BOM_MaterialUsenumber_item.grid(row=11, column=3)


result_rule = tkinter.StringVar()
result_name = tkinter.StringVar()
result11 = tkinter.StringVar()


label_rule = tkinter.Label(window, width=35, textvariable=result_rule)
label_rule.grid(row=11, column=2)

label_name = tkinter.Label(window, width=16, textvariable=result_name)
label_name.grid(row=11, column=1)

label10 = tkinter.Label(window, width=30, text='機種包材BOM新增及查詢系統')
label10.grid(row=7, column=1)

label10_1 = tkinter.Label(window, width=15, text='==================')
label10_1.grid(row=7, column=0)

label10_2 = tkinter.Label(window, width=35, text='========================================')
label10_2.grid(row=7, column=2)

BOM_ProductionID_label = tkinter.Label(window, width=15, text='機種型名')
BOM_ProductionID_label.grid(row=8, column=0)
BOM_MaterialID_label = tkinter.Label(window, width=15, text='查詢材料號')
BOM_MaterialID_label.grid(row=10, column=0)
BOM_Matrialname_label = tkinter.Label(window, width=16, text='品名')
BOM_Matrialname_label.grid(row=10, column=1)
BOM_Matrialrule_label = tkinter.Label(window, width=35, text='規格')
BOM_Matrialrule_label.grid(row=10, column=2)
BOM_MaterialUsenumber_label = tkinter.Label(window, width=8, text='數量/單片')
BOM_MaterialUsenumber_label.grid(row=10, column=3)

label1 = tkinter.Label(window, width=10, textvariable=result11)
label1.grid(row=12, column=2)


btn4 = tkinter.Button(window, width=15, text='搜尋料號', command=find_number_forBOM)
btn4.grid(row=12, column=0)

btn5 = tkinter.Button(window, width=15, text='新增此機種包材料號', command=add_number_forBOM)
btn5.grid(row=12, column=1)

#=========================================================機種BOM表查詢

btn6 = tkinter.Button(window, width=15, text='查詢機種包材BOM', command=find_production_forBOM)
btn6.grid(row=9, column=1)

result_P = tkinter.StringVar()
label12 = tkinter.Label(window, width=35, textvariable=result_P)
label12.grid(row=9, column=2)

window.mainloop()




