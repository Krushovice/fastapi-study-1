from fastapi_users.authentication import (
    AuthenticationBackend,
)

from core.authentication.transport import bearer_transport
from api.dependencies.authentification.stategy import get_database_strategy

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
