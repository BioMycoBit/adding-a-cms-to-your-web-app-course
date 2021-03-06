from pyramid.request import Request

from pypi.services import user_service
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.email = self.request_dict.get('email')
        self.password = self.request_dict.get('password')

        if self.email:
            self.email = self.email.strip().lower()

        if self.email and self.password:
            self.__user = user_service.login_user(self.email, self.password)
            if self.__user:
                self.user_id = self.__user.id

    def validate(self):
        if not self.user:
            self.error = 'The user could not found or the password is incorrect.'
