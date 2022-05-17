from base_setting import BaseSetting
from develop_setting import DevelopSetting
from production_setting import ProductionSetting
from test_setting import TestSetting

config_dict = {
    'default': DevelopSetting,
    'development': DevelopSetting,
    'testing': TestSetting,
    'production': ProductionSetting
}


# pip freeze > requirements.txt