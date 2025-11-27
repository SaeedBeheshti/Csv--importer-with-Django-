import csv
from io import StringIO
from celery import shared_task
from .models import Book, ImportJob

@shared_task
def process_csv(file_data, job_id):
    job = ImportJob.objects.get(id=job_id)
    job.status = 'processing'
    job.save()

    errors = {}
    reader = csv.DictReader(StringIO(file_data))
    for i, row in enumerate(reader, start=1):
        try:
            Book.objects.create(
                title=row['title'],
                author=row['author'],
                isbn=row['isbn'],
                published_date=row.get('published_date') or None
            )
        except Exception as e:
            errors[f'row_{i}'] = str(e)

    job.errors = errors
    job.status = 'done' if not errors else 'failed'
    job.save()
