# from this import s
from tkinter import *

def sort_answ_4_rel(rl):
    div = (len(rl)-2)//2
    l1, l2 = [],[]
    for i in range(len(rl)-1):
        if i <= div:
            l1.append(rl[i])
        else:
            l2.append(rl[i])
    return [l1, l2]


#
class Lbl_img:
    def __init__(self, master, is_img, text):
        self.master, self.is_img, self.text = master, is_img, text

    def get(self):
        if not self.is_img: return self.get_lbl()
        else: return self.try_img()

    def get_lbl(self): return Label(master=self.master, text=self.text, font=("Helvetica",14))

    def get_img(self): return Label(master=self.master, image=PhotoImage('assets/'+self.text))

    def try_img(self):
        # try:
        return self.get_img()
        # except BaseException as be:
        #     print(be)
        #     return self.get_lbl()

class Main_q:
    def __init__(self, master ,orig_qestion_list):
        self.master = master
        self.type = orig_qestion_list[0]
        self.qestion = orig_qestion_list[1]
        self.answers = orig_qestion_list[2]
        self.user_answ = ''
        self.is_img = False
        if 'img' in orig_qestion_list[0]:
            self.is_img = True


    def single_answ_q(self, master):
        q_frame = Frame(master=master)
        self.user_answ = IntVar(q_frame, 10)
        r_i = -1
        for answ in self.answers:
            r_i+=1
            rb = Radiobutton(master=q_frame, text=answ[0], font=("Helvetica",14), variable=self.user_answ, value=r_i)
            rb.pack(anchor='w')
        q_frame.pack(anchor='w')


    def many_answ_q(self, master):
        self.user_answ = []
        for i in self.answers:
            self.user_answ.append(IntVar())
        q_frame = Frame(master=master)
        for i in range(len(self.answers)):
                Checkbutton(master=q_frame, text=self.answers[i], variable = self.user_answ[i],  font=("Helvetica",14)).pack(anchor='w')
        q_frame.pack(anchor='w',)


    def txt_answ_q (self, master):
        q_frame = Frame(master=master)

        self.user_answ = Entry(master=q_frame, font=("Helvetica",10))
        self.user_answ.pack()

        q_frame.pack(anchor='w')

    
    def rel_answ_q(self, master):
        m_frame = Frame(master=master)
        q_frame = Frame(master=m_frame)
        a_frame= Frame(master=m_frame)

        self.answers = sort_answ_4_rel(self.answers)
        print(self.answers)
        for col in range(2):
            for row in range(len(self.answers[0])):
                Label(master=q_frame, font=("Helvetica",14), text=self.answers[col][row]).grid(column=col, row=row, sticky='w', padx=10)
        
        

        af1 = ['A', 'B', "C"]
        self.user_answ= []
        for i in range(len(self.answers[0])): self.user_answ.append(0)

        for i in range(0,len(self.answers[0])):
            answ_lbl = Label(master=a_frame, font=("Tahoma",15), text=af1[i], width=3)
            answ_lbl.grid(row=0, column=i,  padx=1, pady=1)
            self.user_answ[i] = Entry(master=a_frame, font=("Tahoma",15), justify="center", width=3)
            self.user_answ[i].grid(row=1, column=i, pady=1)

        q_frame.grid(row=0, sticky='w', column=0)
        a_frame.grid(row=0, sticky=W+N, column=1)
        m_frame.pack(anchor='w')


    def test_q(self, master):
        for i in self.answers:
            Lbl_img(master,self.is_img ,i).get().pack()

    def build(self): 
        print(self.qestion, self.answers)
        main_q_frame = Frame(master=self.master, padx=30, pady=20)

        #label job
        for lbl in self.qestion:
            q_label = Label(master=main_q_frame, text=lbl, font=("Helvetica",16))
            q_label.pack(anchor='w')

        #answers job
        if 'single_answ' in self.type:
            self.single_answ_q(main_q_frame)
        elif 'many_answ' in self.type:
            self.many_answ_q(main_q_frame)
        elif 'txt_answ' in self.type:
            self.txt_answ_q(main_q_frame)
        elif 'rel_answ' in self.type:
            self.rel_answ_q(main_q_frame)
        elif 'test' in self.type:
            self.test_q(main_q_frame)
        
        return main_q_frame
    
    
