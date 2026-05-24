# AP2-Style Payment Safety

This is a local simulation. It does not process payment.

Rules:

- Agent cannot place an order without explicit user confirmation.
- Payment requires a payment mandate.
- Idempotency keys block duplicate order/payment attempts.
- Audit logs record payment-sensitive events.
- Declined, success, and duplicate paths are simulated.
