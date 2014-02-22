# -*- coding: UTF-8 -*-
from app import app, db
from flask import request, render_template, session, url_for, redirect, flash
from controls import *
from random import shuffle

app.secret_key = '\xba\xf2\xac\xa7C\x00\x12\xee_\x8ex \xf9\x17G\xe7g\xc1\xd2\xe7\x02\x89o\x83' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exam')
def exam():
    if 'username' in session:
        exams = get_exams_details(db)
        return render_template('exam.html', exams=exams)
    else:
        # flash("You must login first!")
        error = "You must login first!"
        return render_template('login.html', page='exam', error=error)

@app.route('/exam/<link>', methods=['GET','POST'])
def exam_link(link):
    if (request.method == 'POST') and ('username' in session) and (link in get_exam_links(db)):
        exam_details = get_exam_details(db, link)
        make_details = get_make_details(db, session['username'], link)
        
        still_deadline = get_deadline(exam_details['deadline'])
        
        if still_deadline and (make_details==None or (make_details and get_now() < make_details['deadline'])):
            while make_details==None:
                user = session['username']
                question_amount = exam_details['question_amount']
                create_make(db, user, link, question_amount)
                
                make_details = get_make_details(db, user, link)
                
            duration = int((make_details['deadline'] - get_now()).total_seconds())
            submitted = make_details['submitted']
            
            if request.form['doexam']==u'Tiếp tục' or request.form['doexam']==u'Bắt đầu':
                user = session['username']
                questions = get_questions(db, user, link)
                
                for question in questions:
                    question[1] = question[1].items()
                    shuffle(question[1])

            elif request.form['doexam']==u'Nộp bài' or request.form['doexam']==u'Nộp lại':
                user = session['username']
                
                #Theo dõi số lần submit
                submitted += 1
                
                #Khi ấn nộp bài 1.Cập nhật bài làm
                update_make(db, user, link, request.form, submitted)
                
                #2.Sau đó lại lấy dữ liệu bài làm -> hiển thị ra cho người dùng nộp lại cho đến khi hết giờ
                questions = get_questions(db, user, link)
                
                #Randomize answers in each question 
                for question in questions:
                    question[1] = question[1].items()
                    shuffle(question[1])
                
                #3.Chấm điểm (mỗi lần nộp bài sẽ tiến hành cập nhật lại điểm
                mark_point(db, user, link)
                
            else:
                return "Bạn đang cố gắng hack vào hệ thống?"

            return render_template('exam_process2.html', duration=duration, submitted=submitted, questions=questions)
        else:
            return redirect(url_for('exam_link', link=link))
    elif ('username' in session) and (link in get_exam_links(db)):
        exam_details = get_exam_details(db, link)
        make_details = get_make_details(db, session['username'], link)

        still_deadline = get_deadline(exam_details['deadline'])
        now = get_now()

        return render_template('exam_process1.html', exam_details=exam_details, make_details=make_details, still_deadline=still_deadline, now=now)
    else:
        return redirect(url_for('exam'))

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/login', methods=['GET','POST'])
def login():
    page = request.args.get('page', 'index')
    if page not in ['exam', 'index']:
        return redirect(url_for('login'))
        
    #Nếu đã login mà vào /login thì chuyển 
    if 'username' in session:
        return redirect(url_for(page))
    error = None
    if request.method == 'POST':
        if valid_login(db, request.form['username'], request.form['password']):
            session['fullname'] = db.users.find_one({'username': request.form['username']})['fullname']
            session['username'] = request.form['username']
            return redirect(url_for(page))
        error = "Invalid username/password"
    return render_template('login.html', error=error, page=page)

@app.route('/logout')
def logout():
    #Xóa session
    session.pop('username', None)
    session.pop('fullname', None)
    
    #Chuyển về trang chủ
    return redirect(url_for('index'))
    
@app.route('/admin')
def admin():
    page = request.args.get('page', 'index')
    if page not in ['exam', 'index']:
        return redirect(url_for('login'))
    if 'manage' in session:
        return redirect(url_for(page))
    error = None
    if request.method == 'POST':
        if valid_login(db, request.form['username'], request.form['password']):
            session['manage'] = [request.form['username'], db.users.find_one({'username': request.form['username']})['fullname'], db.users.find_one({'username': request.form['username']})['level']]
            return redirect(url_for(page))
        error = "Invalid username/password"

    return render_template('admin/index.html')