import mongoengine as me

class EventModel(me.DynamicDocument):
    id: me.StringField(required=False)
    name: me.StringField(required=True)
    cards: me.ListField(me.ReferenceField('CardModel'), required=True)
    meta = {
        'collection': 'events',
        'strict': False,
    }


class CardModel(me.DynamicDocument):
    id: me.StringField(required=False)
    hdr: me.StringField(required=True)
    status: me.StringField(required=True)
    mtchs: me.ListField(me.ReferenceField('FightModel'), required=True)


class FightModel(me.DynamicDocument):
    id: me.StringField(required=False)
    awy: me.ReferenceField('FighterModel', required=True)
    hme: me.ReferenceField('FighterModel', required=True)
    nte: me.StringField(required=True)
    status: me.ReferenceField('FightStatusModel', required=True)
    dt: me.DateTimeField(required=True)

class FightStatusModel(me.DynamicDocument):
    id: me.StringField(required=False)
    state: me.StringField(required=True)

class FighterModel(me.DynamicDocument):
    id: me.StringField(required=False)
    gndr: me.StringField(required=True)
    country: me.StringField(required=True)
    firstNm: me.StringField(required=True)
    lstNm: me.StringField(required=True)
    dspNm: me.StringField(required=True)
    rec: me.StringField(required=True)
    shrtDspNm: me.StringField(required=True)

class FighterStats(me.DynamicDocument):
    age: me.IntField(required=True)
    ht: me.StringField(required=True)
    rch: me.StringField(required=True)
    sigstrkacc: me.StringField(required=True)
    sigstrklpm: me.StringField(required=True)
    stnce: me.StringField(required=True)
    subavg: me.StringField(required=True)
    tdacc: me.StringField(required=True)
    tdavg: me.StringField(required=True)
    wt: me.StringField(required=True)
