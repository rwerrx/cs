import sqlite3
from random import choice

con = sqlite3.connect("answers.sqlite")
cur = con.cursor()
list_id = cur.execute("""SELECT id FROM answers_el""").fetchall()
this_id = choice(list_id)[0]
query = """SELECT question, correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3 FROM answers_el 
        WHERE id = ?"""
list_qa = cur.execute(query, (this_id,)).fetchone()
question = list_qa[0]
answers = [list_qa[1], list_qa[2], list_qa[3], list_qa[4]]
print(question, answers)
con.close()
