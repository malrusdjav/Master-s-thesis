from nequip.utils import Config
config = Config.from_file('./example.yaml')

import pprint
pprint.pprint(config.as_dict())
