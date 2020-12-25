import json


class User:

    def __init__(self, name, surname, login, password, is_employee=False):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.is_employee = is_employee

    # def to_json(self):
    #     '''
    #     convert the instance of this class to json
    #     '''
    #     return json.dumps(self, indent=4, default=lambda o: o.__dict__)







# jsonified_user = json.dumps(user1, indent=2, default=encoder_user)
# jsonified_user2 = json.dumps(user2, indent=2, default=encoder_user)
# users = [jsonified_user, jsonified_user2]
# print(users)
# for x, elem in enumerate(users):
#     print(elem)
# JsonHandler.serialize_user_to_json(jsonified_user)
# JsonHandler.serialize_user_to_json(users)

# decoded_users = JsonHandler.deserialize_users()
# print(decoded_users)
# # print(decoded_users['name'])
#
# for name in decoded_users['name']:
#     print(name)

# JsonHandler.serialize_user_to_json(user1)