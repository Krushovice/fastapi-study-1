from core.models import AccessToken
from .model_generic import ModelDepGeneric


class AccessTokenDep(ModelDepGeneric[AccessToken]):
    model = AccessToken
