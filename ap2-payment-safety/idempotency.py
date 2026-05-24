from __future__ import annotations

from typing import Dict

_SEEN: Dict[str, str] = {}


def check_and_store(key: str, result_id: str) -> tuple[bool, str]:
    if key in _SEEN:
        return False, _SEEN[key]
    _SEEN[key] = result_id
    return True, result_id
