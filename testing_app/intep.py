from random import shuffle

def q_handler():
    readed_txt_list = read_txt()
    return shuffling(readed_txt_list)

def read_txt():
    text = open("test_input1.txt").read()
    rows = [row.strip() for row in text.split('\n') if row.strip!='']


    new_q, q_list = [], []

    for i in rows:
        if i[0:3] != '===':
            new_q.append(i)
        else:
            q_list.append(new_q)
            new_q=[]

    q_list_sorted = []
    for q in q_list:
        new_q, new_qpiece=[],[]
        q_flag = False
        for i in q:
            if not q_flag:
                if i[0:3] == '---':
                    new_q.append(new_qpiece)
                    new_qpiece = []
                    q_flag = True
                else:
                    new_qpiece.append(i)
            if q_flag:
                if i[0:3] != '---':
                    cor_bol = False
                    new_i = i
                    if i[-3:-1] == "**": 
                        new_i = i[0:-3]
                        cor_bol = True
                    new_answ = [new_i, cor_bol]
                    new_qpiece.append(new_answ)
        new_q.append(new_qpiece)
        q_list_sorted.append(new_q)
    return (q_list_sorted)

def sorting_in_2(recive_l):
    l1, l2 = [],[]
    for li in recive_l:
        l1.append(li[0])
        l2.append(li[1])
    return [l1, l2]

def shuffling(q_list):
    new_q_l = []
    for q_item in q_list:
        new_q = [q_item[0][0],q_item[0],q_item[1]]
        del new_q[1][0]
        #shuffles the answers
        if not 'rel_answ' in new_q[0]:
            print(new_q[0])
            shuffle(new_q[2])
        sorted_answ = sorting_in_2(new_q[2])
        del new_q[2]
        new_q.append(sorted_answ[0])
        new_q.append(sorted_answ[1])
        # print(new_q)
        new_q_l.append(new_q)
    #shuffles the whole q_list
    shuffle(new_q_l)
    return new_q_l