from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(20))
    contact_addr = db.Column(db.String(50))
    student_id= db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", backref="contacts")

class Name(db.Model):
    __tablename__ = 'name'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(20))
    last = db.Column(db.String(20))
    student_id= db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", backref="name")

class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    vnu_email = db.Column(db.String(40))
    other_email = db.Column(db.String(40))
    student_id= db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", backref="email")



class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(8))
    dob = db.Column(db.String(10))
    gender = db.Column(db.String(10))
  

    # name = Name
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title

class NameSchema(ma.Schema):
    class Meta:
        model = Name
        fields = ("first", "last")

class EmailsSchema(ma.Schema):
    class Meta:
        model = Email
        fields = ("vnu_email", "other_email")

class ContactSchema(ma.Schema):
    class Meta:
        model = Contact
        fields = ("contact_name", "contact_addr")

class StudentSchema(ma.Schema):
    name = NameSchema()
    emails = EmailsSchema()
    contacts = ContactSchema(many=True)

    class Meta:
        model = Student
        fields = ("id", "sid", "name", "dob", "gender", "emails", "contacts")


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return students_schema.dump(students)

    def post(self):
        new_student = Student(
            dob=request.json['dob'],
            sid=request.json['sid'],
            description=request.json['description']
        )
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student)


class StudentResource(Resource):
    def get(self, id):
        student = Student.query.get_or_404(id)
        return student_schema.dump(student)

    def patch(self, post_id):
        student = Student.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return students_schema.dump(student)

    def delete(self, post_id):
        student = Student.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

# api end-point
api.add_resource(StudentListResource, '/students')
api.add_resource(StudentResource, '/students/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)