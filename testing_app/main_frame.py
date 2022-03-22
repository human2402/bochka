from tkinter import *
from face_classes.q_face import Main_q
from intep import q_handler

root=Tk()
main_frame = Frame(master = root)


sorted_q_l = q_handler()
print(sorted_q_l)

q_frames_list_main = []
for q in sorted_q_l:
    nq = Main_q(main_frame, q)
    nq.build().pack(anchor='w')
    q_frames_list_main.append(nq)
    

# q_f = Main_q(main_frame, [['one_answ', "What's 2+2?","How are ya doin"], [['3', False], ['4', True], ['22', False]]])
# q_f = Main_q(main_frame, ['single_answ', ["What's 2+2?", 'How are ya'], ['4', '3', '22'], [True, False, False]])
# q_f.build().pack(anchor='w')
# q_f1 = Main_q(main_frame, ['many_answ', ["What's 2+2?", 'How are ya'], ['4', '3', '22'], [True, False, False]])
# q_f1.build().pack(anchor='w')
# q_f2 = Main_q(main_frame, ['txt_answ', ["What's 2+2?", 'How are ya'], ['4', '3', '22'], [True, False, False]])
# q_f2.build().pack(anchor='w')
# q_f3 = Main_q(main_frame, ['rel_answ', ["What's the representacion of different colors in the RBG system?"], ['A)(0,100,0)', 'B)(100,0,0)', 'C)(0,0,100)', '1)Blue', '2)Red', '3)Green', '123'], [False, False, False, False, False, False, True]])
# q_f3.build().pack(anchor='w')

#['rel_answ', ["What's the representacion of different colors in the RBG system?"], ['B)(100,0,0)', 'C)(0,0,100)', '2)Red', '123', '3)Green', '1)Blue', 'A)(0,100,0)'], [False, False, False, True, False, False, False]]
def show_user ():
    print(q_frames_list_main[0].get())
Button(master=main_frame, font=("Helvetica",16), text='show user_answ', command =show_user).pack()


main_frame.pack()
root.mainloop()