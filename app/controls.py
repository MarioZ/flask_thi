# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import random

def valid_login(db, username, password):
    return db.users.find({'username':username, 'password':password}).count() == 1
    
def get_exam_links(db):
    """returns list of link of exams"""
    result = []
    for exam in db.exams.find({'status': True}):
        result.append(exam['link'])
    return result
    
def get_exams_details(db):
    """get multi exams, returns list of exams"""
    return list(db.exams.find({'status': True}))
    
def get_exam_details(db, link):
    """get a exam, returns dict of a exam"""
    return db.exams.find_one({'link': link})
    
def get_make_details(db, user, exam_link):
    """get a make, returns dict of a make"""
    return db.makes.find_one({'name': user, 'exam': exam_link})
    
def get_deadline(deadline):
    """returns True if still time to make test"""
    return datetime.now() <= deadline
    
def get_now():
    return datetime.now()
    
def get_random_questions_and_correct(db, question_amount):
    questions = []
    correct = []
    while question_amount > 0:
        ques_detail = db.questions.find_one( {'random_point' : {'$near' : [random.random(), 0]} })
        
        ques = ques_detail['question']
        ans = {}
        ans_correct = ques_detail['answers']
        for a in ques_detail['answers'].keys():
            ans[a] = False
        type = ques_detail['type']
        
        if [ques, ans, type] not in questions:
        
            questions.append([ques, ans, type])
            correct.append([ques, ans_correct, type])
            
            question_amount -= 1
            
    return [questions, correct]

def create_make(db, user, exam_link, question_amount):
    exam = db.exams.find_one({'link': exam_link})
    questions, correct = get_random_questions_and_correct(db, question_amount)
    
    new = {'name': user, 'exam': exam_link, 'point': 0, 'deadline': datetime.now() + timedelta(seconds=exam['duration'] * 60), 'submitted': 0, 'questions': questions, 'correct': correct}
    db.makes.insert(new)
    
def update_make(db, user, exam_link, re_form, submitted):
    questions = get_questions(db, user, exam_link)
    
    for ques in questions:
        re_answer = re_form.getlist(ques[0])
        
        #Cho tất cả các câu trả lời về False
        for ans in ques[1]:
            ques[1][ans] = False
        
        #Kiểm tra từng câu trả lời được gửi đến, câu trả lời nào (đúng thuộc ques) đc gửi đến thì đổi thành True
        for r_a in re_answer:
            if r_a in ques[1]:
                ques[1][r_a] = True
        
    db.makes.update({'name': user, 'exam': exam_link}, { '$set' : {'questions': questions, 'submitted': submitted} })
    
def get_questions(db, user, exam_link):
    make = db.makes.find_one({'name': user, 'exam': exam_link})
    return make['questions']

def mark_point(db, user, exam_link):
    make = db.makes.find_one({'name': user, 'exam': exam_link})
    
    correct = make['correct']
    questions = make['questions']
    question_amount = float(len(correct))
    
    count = 0
    for ques in correct:
        if ques in questions:
            count += 1

    point = int(round(count / question_amount * 100))

    db.makes.update({'name': user, 'exam': exam_link}, { '$set' : {'point': point} })
    
if __name__ == '__main__':
    from pymongo import MongoClient,  GEO2D
    client = MongoClient()
    db = client.cstd
