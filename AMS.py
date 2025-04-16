from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox, simpledialog
import mysql.connector
import pandas as pd
from fpdf import FPDF
import openpyxl
from openpyxl.styles import Font
import os

class admission:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Admission Management System")

    # ================= variables==================
        self.var_Name=StringVar()
        self.var_id=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_Language=StringVar()
        self.var_Combination=StringVar()
        self.var_Category=StringVar()
        self.var_Caste_Name=StringVar()
        self.var_DOA=StringVar()
        self.var_Fee_paid=StringVar()
        self.var_Fine_Amount=StringVar()
        self.var_Remarks=StringVar()

        # first img
        img=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\online-admission.jpg")
        img=img.resize((1530,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=140)

        # bg img
        img3=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\wp1.jpg")
        img3=img3.resize((1530,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ADMISSION MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="admission Details",font=("times new roman",12,"bold"))
        left_frame.place(x=30,y=10,width=750,height=585)

        img_left=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\admission-Information1.jpg")
        img_left=img_left.resize((740,140),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=735,height=140)

        # admission information
        class_admission_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="admission information",font=("times new roman",12,"bold"))
        class_admission_frame.place(x=5,y=145,width=735,height=120)

        # Student Name
        Name_lable=Label(class_admission_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        Name_lable.grid(row=0,column=0,padx=10,sticky=W)
        
        Name_combo=ttk.Entry(class_admission_frame,textvariable=self.var_Name,font=("times new roman",12,"bold"),state="read only")
        Name_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Reg.No
        Reg_lable=Label(class_admission_frame,text="Reg.No",font=("times new roman",12,"bold"),bg="white")
        Reg_lable.grid(row=0,column=2,padx=1,sticky=W)

        Reg_combo=ttk.Combobox(class_admission_frame,textvariable=self.var_id,font=("times new roman",12,"bold"),state="read only",width=20)
        Reg_combo["values"]=("U06GO")
        Reg_combo.current(0)
        Reg_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # YEAR
        year_lable=Label(class_admission_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(class_admission_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","I st","II nd","III rd")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester
        semester_lable=Label(class_admission_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_lable.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(class_admission_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","Ist sem","IInd sem","IIIrd sem","IVthn sem","Vth sem","VIth_sem")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class admission information
        admission_information_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="admission information",font=("times new roman",12,"bold"))
        admission_information_frame.place(x=5,y=280,width=735,height=280)

        # Language
        Language_lable=Label(admission_information_frame,text="Language:",font=("times new roman",12,"bold"),bg="white")
        Language_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Language_combo=ttk.Combobox(admission_information_frame,textvariable=self.var_Language,width=20,font=("times new roman",12,"bold"))
        Language_combo["values"]=("Select Language","K/E","K/H","E/K")
        Language_combo.current(0)
        Language_combo.grid(row=0,column=1,padx=1,pady=1,sticky=W)

        # Combination
        Combination_lable=Label(admission_information_frame,text="Combination:",font=("times new roman",12,"bold"),bg="white")
        Combination_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Combination_combo=ttk.Combobox(admission_information_frame,textvariable=self.var_Combination,width=20,font=("times new roman",12,"bold"))
        Combination_combo["values"]=("Select Combination","BSC","BCA","B.COM","BBA","BA")
        Combination_combo.current(0)
        Combination_combo.grid(row=0,column=3,padx=1,pady=1,sticky=W)

        # Category
        Category_lable=Label(admission_information_frame,text="Category:",font=("times new roman",12,"bold"),bg="white")
        Category_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Category_combo=ttk.Combobox(admission_information_frame,textvariable=self.var_Category,width=20,font=("times new roman",12,"bold"))
        Category_combo["values"]=("Select Category","category I","Category II(A)","Category III(A)","Category II(B)")
        Category_combo.current(0)
        Category_combo.grid(row=1,column=1,padx=1,pady=1,sticky=W)

        # Caste Name
        Caste_Name_lable=Label(admission_information_frame,text="Caste Name:",font=("times new roman",12,"bold"),bg="white")
        Caste_Name_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)
               
        Caste_Name_combo=ttk.Combobox(admission_information_frame,textvariable=self.var_Caste_Name,font=("times new roman",12,"bold"),state="read only",width=20)
        Caste_Name_combo["values"]=("Select Caste Name","EDIGA","LINGAYAT","MUSLIM","VOKKALIGA")
        Caste_Name_combo.current(0)
        Caste_Name_combo.grid(row=1,column=3,padx=1,pady=1,sticky=W)

        # DOA
        DOA_lable=Label(admission_information_frame,text="DOA:",font=("times new roman",12,"bold"),bg="white")
        DOA_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        DOA_entry=ttk.Entry(admission_information_frame,textvariable=self.var_DOA,width=20,font=("times new roman",12,"bold"))
        DOA_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Fee Paid & Receipt No
        Fee_Paid_lable=Label(admission_information_frame,text="Fee Paid & Receipt No:",font=("times new roman",12,"bold"),bg="white")
        Fee_Paid_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Fee_Paid_entry=ttk.Entry(admission_information_frame,textvariable=self.var_Fee_paid,width=20,font=("times new roman",12,"bold"))
        Fee_Paid_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Fine Amount if Any
        Fine_Amount_lable=Label(admission_information_frame,text="Fine Amount if Any:",font=("times new roman",12,"bold"),bg="white")
        Fine_Amount_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Fine_Amount_entry=ttk.Entry(admission_information_frame,textvariable=self.var_Fine_Amount,width=20,font=("times new roman",12,"bold"))
        Fine_Amount_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Remarks
        Remarks_lable=Label(admission_information_frame,text="Remarks:",font=("times new roman",12,"bold"),bg="white")
        Remarks_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Remarks_entry=ttk.Entry(admission_information_frame,textvariable=self.var_Remarks,width=20,font=("times new roman",12,"bold"))
        Remarks_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # buttons frame
        btn_frame=Frame(admission_information_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=190,width=730,height=30)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=800,y=20,width=660,height=575)

        #  ===============search system================
        search_frame=LabelFrame(RIGHT_frame,bd=2,relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=645,height=70)

        search_lable=Label(search_frame,text="Search BY:",font=("times new roman",14,"bold"),bg="blue",fg="white")
        search_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        # search
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Name","Reg","semester","Combination")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #==============excel button================
        export_frame = Frame(admission_information_frame, bd=2, relief=RIDGE, bg="white")
        export_frame.place(x=0, y=220, width=730, height=30)

        export_excel_btn = Button(export_frame, text="EXPORT TO EXCEL", command=self.export_to_excel, width=20, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_excel_btn.grid(row=0, column=0)
        
        export_pdf_btn = Button(export_frame, text="Export to PDF", command=self.export_to_pdf, width=20, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_pdf_btn.grid(row=0, column=2)

        # =========== table frame ==========
        table_frame=Frame(RIGHT_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=90,width=645,height=340)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.admission_table=ttk.Treeview(table_frame,column=("Name","Category","Cast","year","Sem","No","Language","Combination","DOA","Fee","Fine","Remarks"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.admission_table.xview)
        Scroll_y.config(command=self.admission_table.yview)

        self.admission_table.heading("Name",text="Student Name")
        self.admission_table.heading("Category",text="Caste Name")
        self.admission_table.heading("Cast",text="Category")
        self.admission_table.heading("year",text="Year")
        self.admission_table.heading("Sem",text="Semester")
        self.admission_table.heading("No",text="Reg.No")
        self.admission_table.heading("Language",text="Language")
        self.admission_table.heading("Combination",text="Combination")
        self.admission_table.heading("DOA",text="Date of Admission")
        self.admission_table.heading("Fee",text="Fee Paid & Receipt No")
        self.admission_table.heading("Fine",text="Fine Paid & Receipt No")
        self.admission_table.heading("Remarks",text="Remarks")         
        
        self.admission_table["show"]="headings"

        self.admission_table.column("Name",width=100)
        self.admission_table.column("Category",width=100)
        self.admission_table.column("Cast",width=100)
        self.admission_table.column("year",width=100)
        self.admission_table.column("Sem",width=100)
        self.admission_table.column("No",width=100)
        self.admission_table.column("Language",width=100)
        self.admission_table.column("Combination",width=100)
        self.admission_table.column("DOA",width=100)
        self.admission_table.column("Fee",width=100)
        self.admission_table.column("Fine",width=100)
        self.admission_table.column("Remarks",width=100)

        self.admission_table.pack(fill=BOTH,expand=1)
        self.admission_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # =================================function declaration=======================     
   
    def add_data(self):
        if (self.var_Combination.get()=="Select Combination"or self.var_Name.get()==""or self.var_id.get()==""):
            messagebox.showerror("Error","ALL Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="it@chi007",database="admission")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Category.get(),
                                                                                                        self.var_Caste_Name.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_Language.get(),
                                                                                                        self.var_Combination.get(),
                                                                                                        self.var_DOA.get(),
                                                                                                        self.var_Fee_paid.get(),
                                                                                                        self.var_Fine_Amount.get(),
                                                                                                        self.var_Remarks.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student admission details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ========================fetch data======================    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="it@chi007",database="admission")
        my_cursor=conn.cursor()
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM admission")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.admission_table.delete(*self.admission_table.get_children())
            for i in data:
                self.admission_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ================get cursor============
    def get_cursor(self,event=""):
        cursor_focus=self.admission_table.focus()
        content=self.admission_table.item(cursor_focus)
        data=content["values"]

        self.var_Name.set(data[0]),
        self.var_id.set(data[5]),
        self.var_year.set(data[3]),
        self.var_sem.set(data[4]),
        self.var_Language.set(data[6]),
        self.var_Combination.set(data[7]),
        self.var_Category.set(data[1]),
        self.var_Caste_Name.set(data[2]),
        self.var_DOA.set(data[8]),
        self.var_Fee_paid.set(data[9]),
        self.var_Fine_Amount.set(data[10]),
        self.var_Remarks.set(data[11])

    # update function 
    def update_data(self):
        if (self.var_Combination.get()=="Select Combination"or self.var_Name.get()==""or self.var_id.get()==" "):
            messagebox.showerror("Error","ALL Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("upadte","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="it@chi007",database="admission")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update admission set Name=%s, Category=%s, caste=%s, year=%s, semester=%s, Language=%s, Combination=%s, DOA=%s, Fee=%s, Fine_Amount_if_Any=%s, Remarks=%s where Reg=%s" ,(
                                                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                                                    self.var_Category.get(),
                                                                                                                                                                                                                    self.var_Caste_Name.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_Language.get(),
                                                                                                                                                                                                                    self.var_Combination.get(),
                                                                                                                                                                                                                    self.var_DOA.get(),
                                                                                                                                                                                                                    self.var_Fee_paid.get(),
                                                                                                                                                                                                                    self.var_Fine_Amount.get(),
                                                                                                                                                                                                                    self.var_Remarks.get(),
                                                                                                                                                                                                                    self.var_id.get()
                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()                
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # delete function 
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Reg.No must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="it@chi007",database="admission")
                    my_cursor=conn.cursor()
                    sql="delete from admission where Reg=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()                
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        # reset
    def reset_data(self): 
        self.var_Name.set("")
        self.var_id.set("U06GO")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_Language.set("Select Language")
        self.var_Combination.set("Select Combination")
        self.var_Category.set("Select Category")
        self.var_Caste_Name.set("Select Caste Name")
        self.var_DOA.set("")
        self.var_Fee_paid.set("")
        self.var_Fine_Amount.set("")
        self.var_Remarks.set("")

    # search data
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Select search by option and enter the search value", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="it@chi007",database="admission")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from admission where " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.admission_table.delete(*self.admission_table.get_children())
                    for i in data:
                        self.admission_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    #========================== excel================
    def export_to_excel(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="it@chi007", database="admission")
            my_cursor = conn.cursor()

            downloads_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
            if not os.path.exists(downloads_path):
                os.makedirs(downloads_path)
            if self.var_com_search.get() == "Select":
                my_cursor.execute("SELECT * FROM admission")
                filename = os.path.join(downloads_path, "admission_Data.xlsx")
            else:
                my_cursor.execute("select * from admission where " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                filename = os.path.join(downloads_path, "admission_filtered_Data.xlsx")

            try:
            # Code to save the file to the filename
                print(f"File saved to {filename}")
            except Exception as e:
                 print(f"Error saving file: {e}")
        
            data = my_cursor.fetchall()
            conn.close()

            if len(data) == 0:
                messagebox.showinfo("Information", "No data available to export")
                return
            
    
            # Create a new Excel workbook
            wb = openpyxl.Workbook()
            ws = wb.active

            # Set font and add a title
            ws['A1'] = "Student Management System Data"
            ws['A1'].font = Font(size=12, bold=True)

            # Define column headers
            headers = ["Student Name","Category","Cast Name","year","Semester","Reg.No","Language","Combination","Date of Admission","Fee paid & receipt No","Fine Amount if any","Remarks"]

            # Add headers to the Excel sheet
            for i, header in enumerate(headers, start=1):
                ws.cell(row=2, column=i).value = header
                ws.cell(row=2, column=i).font = Font(size=12, bold=True)

            # Add student data to the Excel sheet
            for idx, row in enumerate(data, start=3):
                for i, item in enumerate(row, start=1):
                    ws.cell(row=idx, column=i).value = item

            # Save the Excel file
            wb.save(filename)
            messagebox.showinfo("Success", f"Data exported successfully to {filename}")

            # Add a print option
            print_option = messagebox.askyesno("Print", "Do you want to print the exported Excel file?")
            if print_option:
               os.startfile(filename, 'print')

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}")
    # ========================== PDF =====================
    def export_to_pdf(self):
       try:
           conn = mysql.connector.connect(host="localhost", username="root", password="it@chi007", database="admission")
           my_cursor = conn.cursor()

           downloads_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
           if not os.path.exists(downloads_path):
               os.makedirs(downloads_path)
           if self.var_com_search.get() == "Select":
               my_cursor.execute("SELECT * FROM admission")
               filename = os.path.join(downloads_path, "admission_Data.pdf")
           else:
               my_cursor.execute("select * from admission where " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
               filename = os.path.join(downloads_path, "admission_filtered_Data.pdf")
        
           data = my_cursor.fetchall()
           conn.close()

           if len(data) == 0:
               messagebox.showinfo("Information", "No data available to export")
               return
   
           # Create a PDF object with A2 landscape page size
           pdf = FPDF(orientation='L', format='A3')
           pdf.add_page()

           # Set font and add a title
           pdf_title = "Admission Management Data"  # Default title
           title_change = messagebox.askyesno("Change Title", "Do you want to change the PDF title?")
           if title_change:
               pdf_title = simpledialog.askstring("Enter Title", "Enter the new PDF title")
           pdf.set_font("Arial", size=18, style="B")  # Set font to bold and size 18
           pdf.set_text_color(0, 0, 0)  # Set text color to black (dark)
           pdf.cell(0, 15, txt=pdf_title.upper(), ln=True, align='C')  # Convert title to uppercase
           pdf.ln(10)
           pdf.set_font("Arial", size=12)  # Reset font to normal           

            # Define column headers
           headers = ["S.No","Student Name","Category","Cast Name","year","Semester","Reg.No","Language","Combination","Date of Admission","Fee paid & receipt No","Fine Amount if any","Remarks"]

           # Define column widths (adjusted for A2 landscape page size)
           column_widths = [10, 60, 30, 25, 15,20, 40, 25, 28, 38, 45, 40, 20]

           # Function to add table headers with borders
           def add_table_headers():
               pdf.set_font("Arial", size=12, style="B")  # Set font to bold
               for i, header in enumerate(headers):
                   pdf.cell(column_widths[i], 10, header, 1, 0, 'C')
               pdf.ln()
               pdf.set_font("Arial", size=12)  # Reset font to normal

           # Add headers to the PDF
           add_table_headers()

           # Line counter to track the number of lines per page
           line_count = 0
           max_lines_per_page = 25  # Adjust this value based on your font size and page layout

           # Add student data to the PDF with borders
           for idx, row in enumerate(data, start=1):
               if line_count == max_lines_per_page:
                   pdf.add_page()
                   add_table_headers()
                   line_count = 0

               # Add serial number
               pdf.cell(column_widths[0], 10, str(idx), 1, 0, 'C')

               # Add student data
               for i, item in enumerate(row):
                   pdf.cell(column_widths[i + 1], 10, str(item), 1, 0, 'C')
               pdf.ln()
               line_count += 1

           # Save the PDF
           pdf.output(filename)
           messagebox.showinfo("Success", f"Data exported successfully to {filename}")

           # Add a print option
           print_option = messagebox.askyesno("Print", "Do you want to print the exported PDF file?")
           if print_option:
               os.startfile(filename, 'print') 
       except Exception as es:
           messagebox.showerror("Error", f"Due to: {str(es)}")


if __name__ == "__main__":
    root=Tk()
    obj=admission(root)
    root.mainloop()