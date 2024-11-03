from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from linked_list import LinkedList

app = Flask(__name__)
linked_list = LinkedList()

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Poorv123",
    database="student_db"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_no = request.form['roll_no']
    grade = request.form['grade']
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, roll_no, grade) VALUES (%s, %s, %s)", (name, roll_no, grade))
    db.commit()
    linked_list.add_student(name, roll_no, grade)
    return redirect(url_for('index'))

@app.route('/delete/<int:roll_no>', methods=['GET'])
def delete_student(roll_no):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_no,))
    db.commit()
    linked_list.delete_student(roll_no)
    return redirect(url_for('index'))

@app.route('/update/<int:roll_no>', methods=['GET', 'POST'])
def update_student(roll_no):
    if request.method == 'POST':
        new_grade = request.form['grade']
        cursor = db.cursor()
        cursor.execute("UPDATE students SET grade=%s WHERE roll_no=%s", (new_grade, roll_no))
        db.commit()
        linked_list.update_student(roll_no, new_grade)
        return redirect(url_for('index'))
    else:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll_no,))
        student = cursor.fetchone()
        return render_template('update.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
