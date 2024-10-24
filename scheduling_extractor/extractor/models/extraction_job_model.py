import mongoengine as me

class ExtractionJobModel(me.Document):
    time = me.DateTimeField(required=True)
    success = me.BooleanField(required=True)
    length = me.IntField(required=True)
    meta = {
        'collection': 'extraction_jobs'
    }
