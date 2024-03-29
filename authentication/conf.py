import warnings

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django.test.signals import setting_changed
from django.utils import six
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string


DJOSER_SETTINGS_NAMESPACE = 'DJOSER'


class ObjDict(dict):
    def __getattribute__(self, item):
        try:
            if isinstance(self[item], str):
                self[item] = import_string(self[item])
            value = self[item]
        except KeyError:
            value = super(ObjDict, self).__getattribute__(item)

        return value


default_settings = {
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SET_PASSWORD_RETYPE': False,
    'SET_USERNAME_RETYPE': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': False,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': False,
    'PASSWORD_VALIDATORS': [],
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'SERIALIZERS': ObjDict({
        'activation':
                'authentication.serializers.ActivationSerializer',
        'activation_client':
                'authentication.serializers.ClientActivationSerializer',
        'password_reset':
            'authentication.serializers.PasswordResetSerializer',
        'password_reset_confirm':
            'authentication.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype':
            'authentication.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password':
            'authentication.serializers.SetPasswordSerializer',
        'set_password_retype':
            'authentication.serializers.SetPasswordRetypeSerializer',
        'set_username':
            'authentication.serializers.SetUsernameSerializer',
        'set_username_retype':
            'authentication.serializers.SetUsernameRetypeSerializer',
        'user_create':
            'authentication.serializers.UserCreateSerializer',
        'client_create':
            'authentication.serializers.ClientCreateSerializer',
        'user_delete':
            'authentication.serializers.UserDeleteSerializer',
        'user':
            'authentication.serializers.UserSerializer',
        'client':
            'authentication.serializers.UserSerializer',
        'current_user':
            'authentication.serializers.CurrentUserSerializer',
        'token':
            'authentication.serializers.TokenSerializer',
        'token_create':
            'authentication.serializers.TokenCreateSerializer',
    }),
    'EMAIL': ObjDict({
        'activation': 'authentication.email.ActivationEmail',
        'confirmation': 'authentication.email.ConfirmationEmail',
        'password_reset': 'authentication.email.PasswordResetEmail',
    }),
    'LOGOUT_ON_PASSWORD_CHANGE': False,
    'USER_EMAIL_FIELD_NAME': 'email',
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'authentication.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [],
}

SETTINGS_TO_IMPORT = ['TOKEN_MODEL', 'SOCIAL_AUTH_TOKEN_STRATEGY']


class Settings(object):
    def __init__(self, default_settings, explicit_overriden_settings=None):
        if explicit_overriden_settings is None:
            explicit_overriden_settings = {}

        overriden_settings = getattr(
            django_settings, DJOSER_SETTINGS_NAMESPACE, {}
        ) or explicit_overriden_settings

        self._load_default_settings()
        self._override_settings(overriden_settings)
        self._init_settings_to_import()

    def _load_default_settings(self):
        for setting_name, setting_value in six.iteritems(default_settings):
            if setting_name.isupper():
                setattr(self, setting_name, setting_value)

    def _override_settings(self, overriden_settings):
        for setting_name, setting_value in six.iteritems(overriden_settings):
            value = setting_value
            if isinstance(setting_value, dict):
                value = getattr(self, setting_name, {})
                value.update(ObjDict(setting_value))
            setattr(self, setting_name, value)

    def _init_settings_to_import(self):
        for setting_name in SETTINGS_TO_IMPORT:
            value = getattr(self, setting_name)
            if isinstance(value, str):
                setattr(self, setting_name, import_string(value))


class LazySettings(LazyObject):
    def _setup(self, explicit_overriden_settings=None):
        self._wrapped = Settings(default_settings, explicit_overriden_settings)

    def get(self, key):
        """
        This function is here only to provide backwards compatibility in
        case anyone uses old settings interface.
        It is strongly encouraged to use dot notation.
        """
        warnings.warn(
            'The settings.get(key) is superseded by the dot attribute access.',
            PendingDeprecationWarning
        )
        try:
            return getattr(self, key)
        except AttributeError:
            raise ImproperlyConfigured('Missing settings: {}[\'{}\']'.format(
                DJOSER_SETTINGS_NAMESPACE, key)
            )


settings = LazySettings()


def reload_djoser_settings(*args, **kwargs):
    global settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == DJOSER_SETTINGS_NAMESPACE:
        settings._setup(explicit_overriden_settings=value)


setting_changed.connect(reload_djoser_settings)
