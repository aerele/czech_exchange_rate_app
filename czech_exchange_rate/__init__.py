
__version__ = '0.0.1'

from erpnext.setup import utils as target
from czech_exchange_rate import czech_api as source
target.get_exchange_rate = source.get_exchange_rate
