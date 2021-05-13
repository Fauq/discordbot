import aiohttp
import asyncio
from datetime import datetime
from async_timeout import timeout


class APITimeoutError(Exception):
    pass


class User:
    def __init__(self, http: "HTTPClient", data: dict):
        self._http = http
        self.user_id: int = data["user_id"]
        self.guild_id: int = data["guild_id"]
        self.cash: int = data["cash"]
        self.bank: int = data["bank"]
        self.total: int = data['total']
    
    def __repr__(self):
        return f'User(id={self.user_id} guild_id={self.guild_id} cash={self.cash} bank={self.bank} total={self.total})'

    def _update(self, data: dict):
        self.cash = data["cash"]
        self.bank = data["bank"]
        self.total = data['total']

    async def update_balance(self):
        data = await self._http.get_user_balance(self.guild_id, self.user_id)
        self._update(data)

    async def add_money(self, cash_or_bank: str, amount: int, reason: str = None):
        await self._http.increment_user_balance(self.guild_id, self.user_id, cash_or_bank, amount, reason)

    async def set_money_to(self, cash_or_bank: str, amount: int, reason: str = None):
        await self._http.set_user_balance_to(self.guild_id, self.user_id, cash_or_bank, amount, reason)


class HTTPClient:
    BASE = "https://unbelievaboat.com/api"

    def __init__(self, token: str):
        headers = {"Authorization": token}
        self.__session = aiohttp.ClientSession(headers=headers)
        self._rate_limits = []

    async def _request(self, method: str, url: str, json: dict = None):
        resp = None
        if method == "GET":
            resp = await self.__session.get(url, json=json)
        elif method == "POST":
            resp = await self.__session.post(url, json=json)
        elif method == "PUT":
            resp = await self.__session.put(url, json=json)
        elif method == "PATCH":
            resp = await self.__session.patch(url, json=json)
        return resp

    async def request(self, method: str, url: str, json: dict = None) -> dict:
        method = method.upper()
        try:
            async with timeout(5):
                resp = await self._request(method, url, json)
        except (asyncio.TimeoutError, asyncio.CancelledError):
            raise APITimeoutError()
        if resp is None:
            raise ValueError("Invalid method")
        resp_json = await resp.json()

        if resp.status == 429:
            self._rate_limits.append({"time": datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S"),
                                      "retry-after": resp_json["retry-after"]})
        resp.raise_for_status()
        return resp_json

    async def get_user_balance(self, guild_id: int, user_id: int):
        route = f"{self.BASE}/guilds/{guild_id}/users/{user_id}"
        resp = await self.request("GET", route)
        resp["guild_id"] = guild_id
        return resp

    async def set_user_balance_to(self, guild_id: int, user_id: int, cash_or_bank: str, amount: int,
                                  reason: str = None):
        route = f"{self.BASE}/guilds/{guild_id}/users/{user_id}"
        request_json = {cash_or_bank: amount, "reason": reason}
        resp = await self.request("PUT", route, request_json)
        resp["guild_id"] = guild_id
        return resp

    async def increment_user_balance(self, guild_id: int, user_id: int, cash_or_bank: str, amount: int,
                                     reason: str = None):
        route = f"{self.BASE}/guilds/{guild_id}/users/{user_id}"
        request_json = {cash_or_bank: amount, "reason": reason}
        resp = await self.request("PATCH", route, request_json)
        resp["guild_id"] = guild_id
        return resp

    async def close(self):
        await self.__session.close()


class Bot:
    def __init__(self, token: str):
        self.http = HTTPClient(token)

    async def get_bal(self, guild_id: int, user_id: int):
        data = await self.http.get_user_balance(guild_id, user_id)
        return User(self.http, data)

    async def set_bal_to(self, guild_id: int, user_id: int, cash_or_bank: str, amount: int, reason: str = None):
        data = await self.http.set_user_balance_to(guild_id, user_id, cash_or_bank, amount, reason)
        return User(self.http, data)

    async def increment_bal(self, guild_id: int, user_id: int, cash_or_bank: str, amount: int, reason: str = None):
        data = await self.http.increment_user_balance(guild_id, user_id, cash_or_bank, amount, reason)
        return User(self.http, data)

    async def close(self):
        await self.http.close()
