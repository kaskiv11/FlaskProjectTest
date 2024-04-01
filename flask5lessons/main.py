from flask import Flask
from flask import render_template, request
from sqlalc import Session, Base, engine, create_db, drop_db
from group import Group
from sqlalchemy import select
from student import Student


app = Flask(__name__)

create_db()

@app.route("/")
def main():
    return render_template("main.html")

@app.route('/groups', methods=["GET", "POST"])
def group_management():
    with Session() as session:
        if request.method == "POST":
            session.add(Group(name=request.form.get('name')))
            session.commit()
        data = session.query(Group).all()

    return render_template('group/management.html', iterable=data,)


@app.route("/groups/<int:id>", methods=["GET"])
def group_get(id):
    with Session() as sesion:
        data = sesion.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template("main.html", content=data)



@app.route('/students/', methods=["GET", "POST"])
def student_management():
    with Session() as session:
        if request.method == "POST":
            item = Student(
                surname=request.form.get('surname'),
                name=request.form.get('name'),
                age=request.form.get('age')
            )

            session.add(item)
            session.commit()
        data = session.query(Student).all()

        return render_template('student/management.html', iterable=data,)

@app.route("/students/<int:id>", methods=["GET"])
def students_get(id):
    with Session() as sesion:
        data = sesion.scalars(select(Student).where(Student.id == id)).first()
        print(data)
    return render_template("main.html", content=data)


if __name__ == '__main__':
    app.run()


