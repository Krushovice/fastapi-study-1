from core.models import User
from .model_generic import ModelDepGeneric


class UserDep(ModelDepGeneric[User]):
    model = User
