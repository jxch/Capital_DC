from flask import Flask
import py_eureka_client.eureka_client as eureka_client
from config import config_dict

app = Flask(__name__)
app.config.from_object(config_dict['default'])

eureka_client.init(eureka_server=app.config.get('EUREKA_SERVER'),
                   app_name=app.config.get('APP_NAME'),
                   instance_host=app.config.get('SERVER_HOST'),
                   instance_port=app.config.get('SERVER_PORT'),
                   ha_strategy=eureka_client.HA_STRATEGY_RANDOM)

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'),
            threaded=app.config.get('THREADED'),
            port=app.config.get('SERVER_PORT'),
            host=app.config.get('HOST'))
