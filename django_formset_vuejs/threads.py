import threading
import time

from django_formset_vuejs.models import Book


def start_cleanup_job():
    def cleanup_db():
        while True:
            time.sleep(60*60)
            print('hello')
            Book.objects.all().delete()

    thread1 = threading.Thread(target=cleanup_db)

    thread1.start()
