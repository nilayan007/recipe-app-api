"""
django command to wait for the database to start 
"""
import time
from psycopg2 import OperationalError as psycopg2oError # type: ignore
from django.db.utils import OperationalError  # type: ignore
from django.core.management.base import BaseCommand # type: ignore

class Command(BaseCommand):
    """ commad to wait database"""
    def handle(self, *args, **options):
        # entry point for command
        self.stdout.write("waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2oError, OperationalError):
                self.stdout.write("database unavailable , waiting...")
                time.sleep(1)
        self.stdout.writ(self.style.SUCCESS('Database Available!!'))        
