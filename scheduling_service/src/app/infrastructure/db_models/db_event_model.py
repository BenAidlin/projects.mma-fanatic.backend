import mongoengine as me
from scheduling_service.src.app.domains.schedule.models.event_model import (
    EventModel,
    CardModel,
    FightModel,
    FighterModel,
    FighterStats,
)


class FighterStatsDb(me.EmbeddedDocument):
    age = me.StringField(required=False, null=True)
    ht = me.StringField(required=False, null=True)
    rch = me.StringField(required=False, null=True)
    sigstrkacc = me.StringField(required=False, null=True)
    sigstrklpm = me.StringField(required=False, null=True)
    stnce = me.StringField(required=False, null=True)
    subavg = me.StringField(required=False, null=True)
    tdacc = me.StringField(required=False, null=True)
    tdavg = me.StringField(required=False, null=True)
    wt = me.StringField(required=False, null=True)
    odds = me.StringField(required=False, null=True)

    def to_pydantic(self):
        return FighterStats(
            age=self.age,
            ht=self.ht,
            rch=self.rch,
            sigstrkacc=self.sigstrkacc,
            sigstrklpm=self.sigstrklpm,
            stnce=self.stnce,
            subavg=self.subavg,
            tdacc=self.tdacc,
            tdavg=self.tdavg,
            wt=self.wt,
            odds=self.odds,
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: FighterStats):
        return FighterStatsDb(
            age=str(pydantic_model.age) if pydantic_model.age else None,
            ht=str(pydantic_model.ht) if pydantic_model.ht else None,
            rch=str(pydantic_model.rch) if pydantic_model.rch else None,
            sigstrkacc=(
                str(pydantic_model.sigstrkacc) if pydantic_model.sigstrkacc else None
            ),
            sigstrklpm=(
                str(pydantic_model.sigstrklpm) if pydantic_model.sigstrklpm else None
            ),
            stnce=str(pydantic_model.stnce) if pydantic_model.stnce else None,
            subavg=str(pydantic_model.subavg) if pydantic_model.subavg else None,
            tdacc=str(pydantic_model.tdacc) if pydantic_model.tdacc else None,
            tdavg=str(pydantic_model.tdavg) if pydantic_model.tdavg else None,
            wt=str(pydantic_model.wt) if pydantic_model.wt else None,
            odds=str(pydantic_model.odds) if pydantic_model.odds else None,
        )


class FighterModelDb(me.EmbeddedDocument):
    original_id = me.StringField(required=False, null=True)
    gndr = me.StringField(required=False, null=True)
    country = me.StringField(required=False, null=True)
    first_name = me.StringField(required=False, null=True)
    last_name = me.StringField(required=False, null=True)
    display_name = me.StringField(required=False, null=True)
    rec = me.StringField(required=False, null=True)
    short_display_name = me.StringField(required=False, null=True)
    stats = me.EmbeddedDocumentField(FighterStatsDb, required=False, null=True)

    def to_pydantic(self):
        return FighterModel(
            original_id=self.original_id,
            gender=self.gndr,
            country=self.country,
            first_name=self.first_name,
            last_name=self.last_name,
            display_name=self.display_name,
            rec=self.rec,
            short_display_name=self.short_display_name,
            stats=self.stats.to_pydantic(),
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: FighterModel):
        return FighterModelDb(
            original_id=(
                str(pydantic_model.original_id) if pydantic_model.original_id else None
            ),
            gndr=str(pydantic_model.gender) if pydantic_model.gender else None,
            country=str(pydantic_model.country) if pydantic_model.country else None,
            first_name=(
                str(pydantic_model.first_name) if pydantic_model.first_name else None
            ),
            last_name=(
                str(pydantic_model.last_name) if pydantic_model.last_name else None
            ),
            display_name=(
                str(pydantic_model.display_name)
                if pydantic_model.display_name
                else None
            ),
            rec=str(pydantic_model.rec) if pydantic_model.rec else None,
            short_display_name=(
                str(pydantic_model.short_display_name)
                if pydantic_model.short_display_name
                else None
            ),
            stats=FighterStatsDb.from_pydantic(pydantic_model.stats),
        )


class FightModelDb(me.EmbeddedDocument):
    original_id = me.StringField(required=False, null=True)
    awy = me.EmbeddedDocumentField(FighterModelDb, required=False, null=True)
    hme = me.EmbeddedDocumentField(FighterModelDb, required=False, null=True)
    nte = me.StringField(required=False, null=True)
    status = me.StringField(required=False, null=True)
    dt = me.DateTimeField(required=False, null=True)

    def to_pydantic(self):
        return FightModel(
            original_id=self.original_id,
            awy=self.awy.to_pydantic(),
            hme=self.hme.to_pydantic(),
            nte=self.nte,
            status=self.status,
            dt=self.dt,
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: FightModel):
        return FightModelDb(
            original_id=(
                str(pydantic_model.original_id) if pydantic_model.original_id else None
            ),
            awy=FighterModelDb.from_pydantic(pydantic_model.awy),
            hme=FighterModelDb.from_pydantic(pydantic_model.hme),
            nte=str(pydantic_model.nte) if pydantic_model.nte else None,
            status=str(pydantic_model.status) if pydantic_model.status else None,
            dt=pydantic_model.dt if pydantic_model.dt else None,
        )


class CardModelDb(me.EmbeddedDocument):
    original_id = me.StringField(required=False, null=True)
    hdr = me.StringField(required=False, null=True)
    status = me.StringField(required=False, null=True)
    mtchs = me.ListField(
        me.EmbeddedDocumentField(FightModelDb), required=False, null=True
    )

    def to_pydantic(self):
        return CardModel(
            original_id=self.original_id,
            hdr=self.hdr,
            status=self.status,
            mtchs=[match.to_pydantic() for match in self.mtchs],
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: CardModel):
        return CardModelDb(
            original_id=(
                str(pydantic_model.original_id) if pydantic_model.original_id else None
            ),
            hdr=str(pydantic_model.hdr) if pydantic_model.hdr else None,
            status=str(pydantic_model.status) if pydantic_model.status else None,
            mtchs=[FightModelDb.from_pydantic(match) for match in pydantic_model.mtchs],
        )


class EventModelDb(me.Document):
    original_id = me.StringField(required=False, null=True)
    is_completed = me.BooleanField(required=False, null=True)
    postponed_or_canceled = me.BooleanField(required=False, null=True)
    event_date = me.DateTimeField(required=False, null=True)
    name = me.StringField(required=False, null=True)
    cards = me.ListField(
        me.EmbeddedDocumentField(CardModelDb), required=False, null=True
    )
    meta = {
        "collection": "events",
        "strict": False,
    }

    @classmethod
    def get_data(cls):
        return cls.objects(cards__exists=True, cards__0__exists=True)

    def to_pydantic(self):
        return EventModel(
            id=str(self.pk),
            original_id=self.original_id,
            is_completed=self.is_completed,
            postponed_or_canceled=self.postponed_or_canceled,
            event_date=self.event_date,
            name=self.name,
            cards=[card.to_pydantic() for card in self.cards],
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: EventModel):
        return EventModelDb(
            id=str(pydantic_model.id) if pydantic_model.id else None,
            original_id=(
                str(pydantic_model.original_id) if pydantic_model.original_id else None
            ),
            is_completed=(bool(pydantic_model.is_completed)),
            postponed_or_canceled=(bool(pydantic_model.postponed_or_canceled)),
            event_date=pydantic_model.event_date if pydantic_model.event_date else None,
            name=str(pydantic_model.name) if pydantic_model.name else None,
            cards=[CardModelDb.from_pydantic(card) for card in pydantic_model.cards],
        )
