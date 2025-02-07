import mongoengine
from decouple import config
from prediction_service.src.app.domains.prediction_domain.adapters.abstract_msg_client import (
    AbstractMsgClient,
)
from prediction_service.src.app.domains.prediction_domain.facade.prediction_facade import (
    PredictionFacade,
)
from scheduling_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)

if __name__ == "__main__":
    DIContainer.initialize()
    mongoengine.connect(
        db=config("MONGO_DB"),
        host=f"mongodb://{config('MONGO_HOST')}:{config('MONGO_PORT')}/{config('MONGO_DB')}",
        username=config("MONGO_USER"),
        password=config("MONGO_PASSWORD"),
    )
    msg_client: AbstractMsgClient = DIContainer.resolve("AbstractMsgClient")
    msg_client.consume_messages(PredictionFacade.handle_fight_msg_update)
