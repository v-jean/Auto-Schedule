from . import main_bp
from flask import session, render_template, request, flash, redirect, url_for
from .. import db
from ..models import *
from flask_login import login_required, current_user

#user routes
@main_bp.route("/", methods=["GET","POST"])
def home():
    courses = Course.query.all()
    return render_template("home.html", courses=courses)

@main_bp.route("/mis_cursos")
@login_required
def my_courses():
    courses = Course.query.all()
    matches = current_user.matches
    return render_template("myCourses.html", courses=matches)

#-----in construction------
@main_bp.route("/select_course/<int:id>", methods=["POST", "GET"])
@login_required
def select_course(id):
    course = Course.query.filter_by(id=id).first()
    course.users.append(current_user)
    db.session.commit()
    return redirect(url_for("main.home"))

@main_bp.route("/deselect_course/<int:id>", methods=["POST", "GET"])
@login_required
def deselect_course(id):
    course = Course.query.filter_by(id=id).first()
    current_user.matches.remove(course)
    db.session.commit()
    return redirect(url_for("main.home"))

#admin routes
@main_bp.route("/admin", methods=["GET","POST"])
def admin():
    return render_template("adminPanel.html")

@main_bp.route("/admin/add_user", methods=["GET","POST"])
def add_user():
    if request.method == "POST":
        user_name = request.form["user_name"]
        user = User(name=user_name)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.admin"))

@main_bp.route("/admin/delete_user/<int:id>", methods=["GET", "POST"])
def delete_user(id):
    if request.method == "POST":
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("main.data_list"))

@main_bp.route("/admin/add_course", methods=["GET","POST"])
def add_course():
    if request.method == "POST":
        course_name = str(request.form["course_name"])
        start1 = int(request.form["start1"])
        end1 = int(request.form["end1"])
        start2 = int(request.form["start2"])
        end2 = int(request.form["end2"])
        day1 = int(request.form["day1"])
        day2 = int(request.form["day2"])
        type1 = str(request.form["type1"])
        type2 = str(request.form["type2"])
        section = str(request.form["section"])
        try:
            split_time = request.form["split_time"]
            split_time = True
        except:
            split_time = False
        course = Course(name=course_name, start1=start1, end1=end1, day1=day1, day2=day2, start2=start2, end2=end2, split_time=split_time, type1=type1, type2=type2, section=section)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for("main.admin"))

@main_bp.route("/admin/delete_course/<int:id>/", methods=["GET","POST"])
def delete_course(id):
    if request.method == "POST":
        course = Course.query.filter_by(id=id).first()
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for("main.data_list"))

@main_bp.route("/admin/data_list")
def data_list():
    courses = Course.query.all()
    users = User.query.all()
    return render_template("adminList.html", courses=courses, users=users)