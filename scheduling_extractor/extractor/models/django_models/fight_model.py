import mongoengine as me
class FightModel(me.Document):
    id = me.StringField(required=True)