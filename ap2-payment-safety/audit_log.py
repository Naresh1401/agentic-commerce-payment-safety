from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

AUDIT_LOG: List[Dict[str, Any]] = []


def record(event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    event = {"event_type": event_type, "timestamp": datetime.now(timezone.utc).isoformat(), "payload": payload}
    AUDIT_LOG.append(event)
    return event
