class UserFilter:
    @staticmethod
    def is_fancode_user(user):
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        return -40 <= lat <= 5 and 5 <= lng <= 100

    @classmethod
    def get_fancode_users(cls, users):
        return [user for user in users if cls.is_fancode_user(user)]
