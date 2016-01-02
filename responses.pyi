from typing import Any, Callable, Union, re

DELETE = 'DELETE'
GET = 'GET'
HEAD = 'HEAD'
OPTIONS = 'OPTIONS'
PATCH = 'PATCH'
POST = 'POST'
PUT = 'PUT'
calls = int


def activate(func: Callable) -> Callable: pass


def add(method: str, url: re.Pattern, body: Union[str, bytes] = '',
        match_querystring: bool = False,
        status: int = 200, adding_headers: None = None,
        stream: bool = False, content_type: str = 'text/plain',
        json: Union[dict, None] = None) -> None: pass


def add_callback(method: str, url: re.Pattern,
                 callback: Callable[['requests.Response'], Any],
                 match_querystring: bool = False,
                 content_type: str = 'text/plain') -> None: pass


def reset() -> None: pass
def start() -> None: pass
def stop() -> None: pass
