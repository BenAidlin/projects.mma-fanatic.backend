import mongoengine as me
class EventModel(me.Document):
    id = me.StringField(required=True)
    link = me.StringField(required=False)
    is_completed = me.BooleanField(required=True)
    name = me.StringField(required=True)
    event_date = me.DateTimeField(required=True)

    fights = me.ListField(me.ReferenceField('FightModel'), required=False)

    meta = {
        'collection': 'events'
    }

