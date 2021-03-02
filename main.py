from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


# class Name(db.Model):
#     first = db.Column(db.String(20))
#     last = db.Column(db.String(20))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dob = db.Column(db.String(10))
    sid = db.Column(db.String(8))

    # name = Name
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title



class StudentSchema(ma.Schema):
    class Meta:
        model = Student
        fields = ("id", "dob", "sid", "description")


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
        return students_schema.dump(new_student)


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


api.add_resource(StudentListResource, '/students')
api.add_resource(StudentResource, '/students/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)