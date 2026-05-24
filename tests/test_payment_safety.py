import importlib.util
import sys
from pathlib import Path

module_dir = Path('ap2-payment-safety').resolve()
sys.path.insert(0, str(module_dir))
spec = importlib.util.spec_from_file_location('simulate_payment_flow', module_dir / 'simulate_payment_flow.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_payment_success_and_duplicate_block():
    mandate = module.create_mandate()
    first = module.authorize_payment(mandate, 'pytest_idem')
    second = module.authorize_payment(mandate, 'pytest_idem')
    assert first['status'] == 'authorized'
    assert second['status'] == 'duplicate_blocked'

