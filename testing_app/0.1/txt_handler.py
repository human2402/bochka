import random
def q_handler():
    with open('text.txt') as txt:
        text=txt.read()
    rows = [row.strip() for row in text.split('\n') if row.strip!=""]


    qestions, new_q = [], []
    for text in rows:
        if text != "===":
            new_q.append(text)
        else:
            qestions.append(new_q)
            new_q=[]
    qestions.append(new_q)
    print(qestions)

q_handler()
