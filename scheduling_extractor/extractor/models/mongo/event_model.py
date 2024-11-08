import mongoengine as me
class ExtractedEventModel(me.Document):
    espn_id = me.StringField(required=True)
    link = me.StringField(required=False)
    is_completed = me.BooleanField(required=True)
    name = me.StringField(required=True)
    event_date = me.DateTimeField(required=True)
    cards = me.ListField(me.DynamicField(), required=False)
    meta = {
        'collection': 'events'
    }

