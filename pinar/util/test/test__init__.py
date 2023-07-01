"""
Test config module.
"""
import unittest
import logging

from pinar.util import log_level

class TestUtilInit(unittest.TestCase):
    """Test util __init__ methods"""

    def test_log_level_pass(self):
        """Test log level context manager passes"""
        #Check loggers are set to level
        with self.assertLogs('pinar', level='INFO') as cm:
             with log_level('WARNING'):
                logging.getLogger('pinar').info('info')
                logging.getLogger('pinar').error('error')
                self.assertEqual(cm.output, ['ERROR:pinar:error'])
        #Check if only pinar loggers level change
        with self.assertLogs('matplotlib', level='DEBUG') as cm:
            with log_level('ERROR', name_prefix='pinar'):
                logging.getLogger('pinar').info('info')
            logging.getLogger('matplotlib').debug('debug')
            self.assertEqual(cm.output, ['DEBUG:matplotlib:debug'])

# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestUtilInit)
    unittest.TextTestRunner(verbosity=2).run(TESTS)
