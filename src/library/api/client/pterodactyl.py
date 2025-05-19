import backoff
from src.library.api import HttpAPI, METHOD
from src.library.api.handler import JsonResponse, StreamResponse, MultiPartRequest
from src.library.api.session import NoAuthSession, TokenSession
from src.library.api.exceptions import *
from src.library.utils import getenv

PTERODACTYL_API_URL = getenv("PTERODACTYL_API_URL")
PTERODACTYL_TOKEN = getenv("PTERODACTYL_TOKEN", fail_on_none=False)

class PterodactylAPI(HttpAPI):
    def __init__(self) -> None:
        if PTERODACTYL_TOKEN is None:
            session_auth = NoAuthSession()
        else:
            session_auth = TokenSession(
                token=PTERODACTYL_TOKEN,
                scheme="Bearer ",
            )

        super().__init__(
            base_url=PTERODACTYL_API_URL,
            session_auth=session_auth,
            raise_for_status=True)
    
    @backoff.on_exception(backoff.expo, Exception, max_tries=2)
    async def servers_list(self) -> dict:
        handler: JsonResponse = await self._request(METHOD.GET, path=f'application/servers')
        return handler.json()