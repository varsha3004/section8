from models.user import UserModel
from flask_restful import Resource,reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type = str,
            required = True,
            help = "This field can not be blank!!")
    parser.add_argument('password',
            type = str,
            required = True,
            help = "This field can not be blank!!")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message" : "User with name {} already exists".format(data["username"])},400
        user=UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message":"User created successfully"},201
