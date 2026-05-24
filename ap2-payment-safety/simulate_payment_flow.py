from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from audit_log import AUDIT_LOG, record
from idempotency import check_and_store


def create_mandate(total_amount: float = 22.41, confirmation: str = "I confirm this mock order."):
    mandate = {
        "user_id": "demo_customer_001",
        "cart_id": "cart_capstone",
        "total_amount": total_amount,
        "currency": "USD",
        "merchant_id": "demo_grocery_merchant",
        "allowed_payment_method": "demo_tokenized_card",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_confirmation_text": confirmation,
    }
    mandate["signature_simulated"] = hashlib.sha256(json.dumps(mandate, sort_keys=True).encode()).hexdigest()
    record("payment_mandate_created", mandate)
    return mandate


def authorize_payment(mandate, idempotency_key: str, force_decline: bool = False):
    allowed, existing = check_and_store(idempotency_key, "payment_auth_demo")
    if not allowed:
        result = {"status": "duplicate_blocked", "original_result_id": existing}
        record("duplicate_request_blocked", result)
        return result
    if force_decline:
        result = {"status": "declined", "reason": "simulated_decline"}
        record("payment_declined", result)
        return result
    if "confirm" not in mandate["user_confirmation_text"].lower():
        result = {"status": "blocked", "reason": "confirmation_required"}
        record("payment_blocked", result)
        return result
    result = {"status": "authorized", "authorization_id": "auth_demo_001"}
    record("payment_authorized", result)
    return result


if __name__ == "__main__":
    mandate = create_mandate()
    success = authorize_payment(mandate, "idem_001")
    duplicate = authorize_payment(mandate, "idem_001")
    declined = authorize_payment(create_mandate(99.99), "idem_002", force_decline=True)
    print(json.dumps({"mandate": mandate, "success": success, "duplicate": duplicate, "declined": declined, "audit_log": AUDIT_LOG}, indent=2))
