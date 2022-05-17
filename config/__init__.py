from base_setting import BaseSetting
from dev_setting import DevSetting
from product_setting import ProductSetting
from test_setting import TestSetting
from local_setting import LocalSetting

config_dict = {
    'default': LocalSetting,
    'dev': DevSetting,
    'test': TestSetting,
    'local': LocalSetting,
    'product': ProductSetting
}


# pip freeze > requirements.txt