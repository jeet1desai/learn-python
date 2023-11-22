# Import built in
import os
print(os.name)

import logging
logger = logging.getLogger("MAIN")
logger.error("This is error!!")

# From file
import dictionaries
print(dictionaries.this_dict)

from dictionaries import data
print(data)

