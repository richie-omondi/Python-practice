from abc import ABC, abstractmethod #decorator #ABC stands for Abstract Base Clas

class User:
    first_name = ''
    last_name = ''
    password = ''

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_all_users(self, user_id):
        pass

    @abstractmethod
    def get_user_by_id(self):
        pass

class UserManager(UserAbstract):
    def create_user(self, user:User):
        print("user information")

    def get_all_users(self, user_id):
        return super().get_all_users(user_id)

user_manager = UserManager()
user_manager.get_user_by_id



    