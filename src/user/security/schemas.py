from drf_spectacular.authentication import TokenScheme
from drf_spectacular.plumbing import build_bearer_security_scheme_object

class JWTScheme(TokenScheme):
    target_class = "user.security.auth.JWTAuthentication"
    name = "JWTScheme"
    
    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )