.PHONY: setup run test

setup:
	@if [ -f backend/requirements.txt ]; then pip install -r backend/requirements.txt; fi
	@if [ -f mcp-server/requirements.txt ]; then pip install -r mcp-server/requirements.txt; fi
	@if [ -f agents/requirements.txt ]; then pip install -r agents/requirements.txt || true; fi
	@if [ -f frontend/package.json ]; then cd frontend && npm install; fi

run:
	cd ap2-payment-safety && python3.11 simulate_payment_flow.py

test:
	python3.11 -m pytest tests

