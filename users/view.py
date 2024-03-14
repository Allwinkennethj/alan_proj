from flask import request,Blueprint,jsonify
from users.service import s_getall,s_adduser,s_ifexists,s_edit_user,s_getuser,checkpass

users=Blueprint("users",__name__,url_prefix="/user")

@users.route("/getall",methods=["GET"])
def getuser():
    data=s_getall()
    return jsonify({
        "message":data,
        "status_code":200
    }),200

@users.route("/login",methods=["POST"])
def login():
    payload=request.get_json()
    email=payload.get("email")
    password=payload.get("password")
    data=checkpass(email,password)
    if data is True:
        values=s_getuser(email)
        return jsonify({
            "message": "Success",
            "data":values,
            "status_code": 200
        }), 200
    else:
        return jsonify({
            "message": "Fail",
            "status_code": 500
        }), 500


@users.route("/getuser",methods=["POST"])
def getoneuser():
    payload=request.get_json()
    email=payload.get("email")
    print(email)
    data=s_getuser(email)
    if data is not None:
        return jsonify({
            "message":data,
            "status_code":200
        }),200
    else:
        return jsonify({
            "message":"Not found",
            "status_code":404
        }),404

@users.route("/adduser",methods=["POST"])
def adduser():
    payload=request.get_json()
    email=payload.get("email")
    password=payload.get("password")
    res=s_adduser(email,password)
    if res==True:
        return jsonify({
            "message":"Success",
            "status_code":200
        }),200
    else:
        return jsonify({
            "message":"Fail",
            "status_code":500
        }),500

@users.route("/ifexist",methods=["POST"])
def checkuser():
    payload=request.get_json()
    email=payload.get("email")
    res=s_ifexists(email)
    if res==True:
        return jsonify({
            "message":"Exists",
            "status_code":200
        }),400
    else:
        return jsonify({
            "message": "Not present",
            "status_code": 400
        }), 200

@users.route("/edit",methods=["POST"])
def edituser():
    payload=request.get_json()
    email=payload.get("email")
    name=payload.get("name")
    designation=payload.get("designation")
    age=payload.get("age")
    print(name,age,designation,email)
    data=s_edit_user(email,name,designation,age)
    if data:
        return jsonify({
            "message": "Success",
            "data":data,
            "status_code": 200
        }), 200
    return jsonify({
        "message": "Fail",
        "status_code": 500
    }), 500
