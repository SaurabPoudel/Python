# import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

# to log in a separate file

# logging.basicConfig(filename='intermediate_python/logging/app.log', filemode='w',
#                     format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# import logging

# logging.basicConfig(
#     format='%(asctime)s -%(levelname)s %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

# name = 'John'

# logging.error(f'{name} raised an error')

# import logging

# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning')

#  example_logger is not shown in output , it can't be configured with basicConfig()
# So let's use handlers

import logging_example
