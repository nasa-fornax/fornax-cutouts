from fornax_cutouts.auth.base import AbstractAuthProvider
from fornax_cutouts.auth.registry import AuthRegistry
from fornax_cutouts.models.auth import Principal


class _Provider(AbstractAuthProvider):
    name = "test-provider"
    anon_limit_hit_info = "Send a token to raise this limit"

    async def resolve(self, request) -> Principal | None:
        return None


def test_anon_limit_hit_info_uses_base_default_without_provider():
    registry = AuthRegistry()
    assert registry.anon_limit_hit_info() == AbstractAuthProvider.anon_limit_hit_info


def test_anon_limit_hit_info_uses_registered_provider():
    registry = AuthRegistry()
    registry.register_provider(_Provider)
    assert registry.anon_limit_hit_info() == "Send a token to raise this limit"
