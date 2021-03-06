# -*- coding: utf-8 *-*
from selene import constants
from selene.base import BaseForm
from wtforms import HiddenField, TextField, PasswordField, SelectField
from wtforms.validators import Required, Email


class RegisterForm(BaseForm):

    full_name = TextField(validators=[
        Required(constants.FULL_NAME_IS_REQUIRED)])
    email = TextField(validators=[Required(constants.EMAIL_IS_REQUIRED),
                                  Email(constants.EMAIL_IS_INVALID)])
    password = PasswordField(validators=[
        Required(constants.PASSWORD_IS_REQUIRED)])


class LoginForm(BaseForm):

    email = TextField(validators=[Required(constants.EMAIL_IS_REQUIRED),
                                  Email(constants.EMAIL_IS_INVALID)])
    password = PasswordField(validators=[
        Required(constants.PASSWORD_IS_REQUIRED)])
    next_ = HiddenField()


class RequestNewPasswordForm(BaseForm):

    email = TextField(validators=[Required(constants.EMAIL_IS_REQUIRED),
                                  Email(constants.EMAIL_IS_INVALID)])


class ResetPasswordForm(BaseForm):

    password = PasswordField(validators=[
        Required(constants.PASSWORD_IS_REQUIRED)])
    reset_hash = HiddenField()


class AccountForm(BaseForm):

    def __init__(self, formdata=None, obj=None, prefix='', locale_code='en_US',
        language_choices=[], **kwargs):
        super(AccountForm, self).__init__(formdata, obj, prefix,
            locale_code=locale_code, **kwargs)
        self.language.choices = language_choices

    full_name = TextField(validators=[
        Required(constants.FULL_NAME_IS_REQUIRED)])
    email = TextField(validators=[Required(constants.EMAIL_IS_REQUIRED),
                                  Email(constants.EMAIL_IS_INVALID)])
    password = PasswordField()
    language = SelectField(validators=[
        Required(constants.LANGUAGE_IS_REQUIRED)])
