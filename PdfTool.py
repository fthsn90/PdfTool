from tkinter import *
try:
    import tkinter
except:
    import Tkinter
from tkinter.font import Font
from tkinter import filedialog
from PIL import ImageTk,Image
import os
import PyPDF2
import tkinter.messagebox

pencere = Tk()
pencere.geometry("450x300+450+50")
pencere.config(bg='#252525')
pencere.title("PDF Bölme ve Birleştirme- Pdf Split and Combine")
pencere.iconphoto(False, ImageTk.PhotoImage(Image.open("pdf.png")))
dosyapic = ImageTk.PhotoImage(Image.open("dosya.png"))
kayitpic = ImageTk.PhotoImage(Image.open("kayit.png"))
titlefont = Font(size=15,family='Bahnschrift')

menubar = Menu(pencere)
pencere.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)

def birlestirbro():
    dosyalar = filedialog.askopenfilenames(initialdir = "/",title = "Dosyaları Seç(Select Pdf Files)",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    pdf_merger = PyPDF2.PdfFileMerger()
    try:
        for file in dosyalar:
            pdf_merger.append(file)
        pdf_merger.write(f"{dosyakayıt}.pdf")
        pdf_merger.close()
        lblbilgi["text"] = "İşlem Tamamlandı.(Operation Succeed)"
    except:
        pass
        if not dosyalar:
            pass           

def kayıtyeri():
    global dizinkayıt,dosyakayıt
    try:
        nereyekayıt = filedialog.asksaveasfilename(initialdir = "//",title = "Nereye kaydedilsin(Save As)",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        dizinkayıt,dosyakayıt = os.path.split(nereyekayıt)
        os.chdir(dizinkayıt)
    except:
        pass

def bolbro():
    nereyekayıt = filedialog.asksaveasfilename(initialdir = "//",title = "Nereye kaydedilsin(Save As)",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    dizinkayıt,dosyakayıt = os.path.split(nereyekayıt)
    os.chdir(dizinkayıt)
    sayfalar = entri1.get().split(",")
    dosy, uzantı = os.path.splitext(nereyekayıt)
    with open(dosya, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for i in sayfalar:
            nt = int(i)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(nt))
            output_file_name = f'{dosy}{i}.pdf'
            with open(output_file_name, 'wb') as output_file:
                pdf_writer.write(output_file)  

def sec():
    global dosya
    dosya = filedialog.askopenfilename(initialdir = "/",title = "Dosya Seç(Select File)",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    dizin, dosyadi = os.path.split(dosya)
    if not dosya:
        pass
    else:
        lbl1["text"] = "Seçilen dosya: {}".format(dosyadi)
        lbl1["bg"] = "yellow"

def topbolme():
    global lbl1,entri1,btn1
    tk = Toplevel()
    tk.title("Pdf Bölme - Pdf Split")
    tk.config(bg='#252525')
    tk.geometry("400x400+880+50")
    tk.iconphoto(False, ImageTk.PhotoImage(Image.open("pdf.png")))
    tk.resizable(width=FALSE, height=FALSE)
    lblust = Label(tk,text="PDF KESME BİÇME(PDF SPLİT)",font=titlefont,bg='#252525',fg="white")
    lblust.pack(padx=10)
    dosyasec = Button(tk,text="Dosya Seç",image=dosyapic,compound="top",bg='#252525',command = sec,fg="white")
    dosyasec.pack(side=TOP)
    lbl1 = Label(tk,text="",bg='#252525')
    lbl1.pack()
    frame = Frame(tk)
    frame.pack()
    lbl2 = Label(tk,text="Kesmek istediğiniz sayfaları giriniz(Araya virgün koyunuz)\n Write page numbers on below(with commas)",bg='#252525',fg="white",font=("Bahnschrift 10"))
    lbl2.pack()
    entri1 = Entry(tk,width=7)
    entri1.place(x=175,y=170)
    btn1 = Button(tk,text="Böl",command =bolbro,bg="#252525",fg="white")
    btn1.place(x=185,y=200) 

def topbirlestir():
    global lblust,nereyekayıtedek,dosyasec,lblbilgi
    tk2 = Toplevel()
    tk2.title("Pdf Birleştirme - Pdf Combine")
    tk2.config(bg='#252525')
    tk2.geometry("400x400+70+50")
    tk2.iconphoto(False, ImageTk.PhotoImage(Image.open("pdf.png")))
    tk2.resizable(width=FALSE, height=FALSE)
    lblust = Label(tk2,text="PDF BİRLEŞTİRME",font=titlefont,bg='#252525',fg="white")
    lblust.pack(padx=15,pady=10)
    nereyekayıtedek = Button(tk2,text="Kayıt Yerini Seç\n Save Place",command = kayıtyeri)
    nereyekayıtedek.pack(padx=15,pady=10)
    dosyasec = Button(tk2,text="Dosyaları Seç\n Select Files",image=dosyapic,compound="top",bg='#252525',command = birlestirbro,fg="white")
    dosyasec.pack(side=TOP)
    lblbilgi = Label(tk2,text="",bg='#252525',fg="white")
    lblbilgi.pack()

def Hakkında():
    tkinter.messagebox.showinfo('PdfTool', "İşbu program Python'la kodlanmıstır. @fthsn90 ")

def HakkındaEn():
    tkinter.messagebox.showinfo('PdfTool', 'This tool build using python/tkinter @fthsn90 ')

bolekranı = Button(pencere,text="PDF KESME BİÇME(SPLİT)",fg="#eaeaea",bg="#9b1c00",font=("drifttyp"),command=topbolme)
bolekranı.pack(fill=X,expand=YES,ipady=40)
birlestirekranı = Button(pencere,text="PDF BİRLESTİR(COMBİNE)",fg="#eaeaea",bg="#9b1c00",font=("drifttyp"),command=topbirlestir)
birlestirekranı.pack(fill=X,expand=YES,ipady=40)
menubar.add_cascade(label="Bilgi", menu=subMenu)
subMenu.add_command(label="Hakkında", command=Hakkında)
subMenu.add_command(label="About", command=HakkındaEn)


pencere.mainloop()