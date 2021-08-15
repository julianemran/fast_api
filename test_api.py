import requests
#import pytest


def getUserResponse(id):
    URL = "http://localhost:8000/user/{0}".format(id)
    res = requests.get(url=URL).json()
    return res


def test_getting_users():
    # to test the API with valid inputs
    assert getUserResponse("1")["name"] != None
    # to test the API by requesting user doesn't exist in db
    assert getUserResponse("3")["code"] == 404
    # to test the API by request without user id
    assert getUserResponse("")["detail"] == "Not Found"


def addUserResponse(id, name, age):
    URL = "http://localhost:8000/users/{0}".format(id)
    newUser = {"name": name, "age": age}
    res = requests.post(URL, json=newUser)
    return res.json()


def test_adding_users():
    # to test the API by adding valid user inputs
    addUserResponse(3, "Julian", 21)
    assert getUserResponse("3")["name"] == "Julian"

    # to test the API by adding a user with an empty name

    addUserResponse(4, "", 29)
    assert getUserResponse("4")["code"] == 404

    # to test the API by adding a user with an exist id
    addUserResponse(1, "Messi", 35)
    assert getUserResponse("1")["name"] != "Messi"


def deleteUserResponse(id, pas):
    URL = "http://localhost:8000/users/{0}".format(id)
    password = {"password": pas}
    res = requests.delete(url=URL, json=password)
    return res.json()


def test_deleting_users():
    # to test the API by deleting a user with valid inputs
    deleteUserResponse(1, "1234")
    assert getUserResponse("1")["code"] == 404
    # to test the API by deleting a user with invalid password
    deleteUserResponse(2, "123")
    assert getUserResponse("2")["name"] != None
    # to test the API by deleting a user that didn't exist in db
    deleteUserResponse(5, "1234")["code"] == 404


"""
import requests
#import pytest


def getCourse(id):
    URL = "http://localhost/courses-svc/courses/{0}".format(id)
    res = requests.get(url=URL)
    return res


def createCourse(name, disc):
    URL = "http://localhost/courses-svc/courses"
    newCourse = {"course_name": name,
                 "profile_image": "https://altooro.com/design/logo/course_image_large.webp", "description": disc}
    res = requests.post(URL, json=newCourse)
    return res


def test_creating_courses():
    courseID = createCourse("TestName", "thisIsTest").json()[
        "data"]["course_id"]
    assert getCourse(courseID).json()["data"]["course_name"] == "TestName"
    assert createCourse("", "thisIsTest").status_code == 400
    assert createCourse("    ", "thisIsTest").status_code == 400



def deleteUserResponse(id, pas):
    URL = "http://127.0.0.1:8000/users/{0}".format(id)
    password = {"password": pas}
    res = requests.delete(url=URL, json=password)
    return res.json()


def test_deleting_users():
    # to test the API by deleting a user with valid inputs
    deleteUserResponse(1, "1234")
    assert getUserResponse("1")["code"] == 404
    # to test the API by deleting a user with invalid password
    deleteUserResponse(2, "123")
    assert getUserResponse("2")["name"] != None
    # to test the API by deleting a user that didn't exist in db
    deleteUserResponse(5, "1234")["code"] == 404
"""
