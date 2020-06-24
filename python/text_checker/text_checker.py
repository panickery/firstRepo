import tkinter as tk
import tkinter.scrolledtext as st

listSt = None

def doDistinct() :
    full_txt = listSt.get("1.0", "end")
    txt_arr = full_txt.split('\n')
    txt_arr.pop()
    txt_arr = list(set(txt_arr))
    listSt.delete(1.0 ,"end")
    listSt.insert(1.0, '\n'.join(txt_arr))

def doVerticalSum() :
    full_txt = listSt.get("1.0", "end")
    txt_arr = full_txt.split('\n')
    txt_arr = list(map(str.strip, txt_arr))
    txt_arr.pop()
    num_arr = []

    for i in txt_arr :
        try :
            num_arr.append(float(i))        
        except Exception as e:
            print(e)
            continue
    sum = 0
    for i in num_arr :
        sum += i

    listSt.delete(1.0 ,"end")
    listSt.insert(1.0, str(sum))

def doSort() :
    full_txt = listSt.get("1.0", "end")
    txt_arr = full_txt.split('\n')
    txt_arr.pop()
    txt_arr.sort()
    listSt.delete(1.0 ,"end")
    listSt.insert(1.0, '\n'.join(txt_arr))

if __name__ == '__main__' : 
    window = tk.Tk()
    window.title('Text cheker')

    frame1 = tk.Frame(window)
    frame1.grid(row = 0, column = 0)

    tk.Label(frame1, text='Result : ', width = 10).grid(row = 0, column = 0)
    frame2 = tk.Frame(window)
    frame2.grid(row = 0, column = 1)

    nameEn = tk.Entry(frame2, width = 30)
    nameEn.grid(row = 0, column = 0)

    frame3 = tk.Frame(window)
    frame3.grid(row = 0, column = 2)

    distinctBtn = tk.Button(frame3, text = 'Distinct', width = 15, command = doDistinct)
    distinctBtn.grid(row = 0, column = 0)
    veriticalSumBtn = tk.Button(frame3, text = 'Vertical Sum', width = 15, command = doVerticalSum)
    veriticalSumBtn.grid(row = 1, column = 0)
    sortBtn = tk.Button(frame3, text = 'Sort', width = 15, command = doSort)
    sortBtn.grid(row = 2, column = 0)

    frame4 = tk.Frame(window)
    frame4.grid(row = 1, column = 0, columnspan = 3)

    listSt = st.ScrolledText(frame4, width = 80, height = 10)
    listSt.grid(row = 0, column = 0)

    window.mainloop()


