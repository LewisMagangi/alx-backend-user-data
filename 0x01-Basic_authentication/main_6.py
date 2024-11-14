#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth
    from models.user import User

    """ Create a user test """
    user_email = "u3@gmail.com"
    user_clear_pwd = "pwd"
    user = User()
    user.email = user_email
    user.password = user_clear_pwd
    user.save()

    ba = BasicAuth()
    res = ba.user_object_from_credentials(user_email, user_clear_pwd)
    if res is None:
        print("user_object_from_credentials must return the User object linked to 'user_email' and 'user_pwd'")
        exit(1)
    
    if type(res) is not User:
        print("user_object_from_credentials must return the User object linked to 'user_email' and 'user_pwd': {}".format(res))
        exit(1)
    
    if res.id != user.id:
        print("user_object_from_credentials must return the User object linked to 'user_email' and 'user_pwd': {}".format(res))
        exit(1)
    
    print("OK", end="")