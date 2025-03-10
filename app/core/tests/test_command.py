"""test custom django management commands"""
from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2Error # type: ignore
from django.core.management import call_command # type: ignore
from django.db.utils import OperationalError # type: ignore
from django.test import SimpleTestCase # type: ignore

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """test waiting if the database is ready"""

    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True 
        
        call_command('wait_for_db')
        
        patched_check.assert_called_once_with(databases=['default'])
        
    @patch('time.sleep')    
    def test_wait_for_db_delay(self,patched_sleep, patched_check):
        """test waiting for database when getting operationalerror"""
        patched_check.side_effect = [psycopg2Error] * 2 +\
            [OperationalError] * 3 + [True]
            
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
            
