import requests

from clients.clients import config


def check_admin_login():
    credentials = {"username": "admin",
                   "password": config.admin_password}  # shall define your own password hereapi/rest-auth
    response = requests.post("http://localhost:8000/api/rest-auth/login/", data=credentials)  # must end with slash

    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)


def client():
    headers = {"Authorization": config.my_token}

    response = requests.get("http://localhost:8000/api/profiles",
                            headers=headers)
    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)


def test3():
    data = {"username": "restTest",
            "email": "test@rest.com",
            "password1": config.password_test,
            "password2": config.password_test,
            }
    response = requests.post("http://localhost:8000/api/rest-auth/registration/", data=data)
    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    # check_admin_login()
    # client()
    test3()