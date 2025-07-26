import logging
from dependency_injector import containers, providers
from app.config.database import get_db
from app.persistence.repository.familia_repository.interface.interface_familia_repository import IFamiliaRepository
from app.persistence.repository.parcialidad_repository.interface.interface_parcialidad_repository import IParcialiadRepository
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.manager import Manager
from app.utils.enviroment import settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.routers.main_router"])

    db_session = providers.Resource(get_db)

    repository_factory = providers.Factory(
        RepositoryFactory,
        db=db_session,
    )

    usuario_repository = providers.Factory(
        lambda factory: factory.get_repository(IUsuarioRepository),
        factory=repository_factory
    )
    persona_repository = providers.Factory(
        lambda factory: factory.get_repository(IPersonaRepository),
        factory=repository_factory
    )

    familia_repository = providers.Factory(
        lambda factory: factory.get_repository(IFamiliaRepository),
        factory=repository_factory
    )

    parcialidad_repository = providers.Factory(
        lambda factory: factory.get_repository(IParcialiadRepository),
        factory=repository_factory
    )

    logger = providers.Singleton(logging.getLogger, __name__)

    manager = providers.Factory(
        Manager,
        logger=logger,
        usuario_repository=usuario_repository,
        persona_repository=persona_repository,
        familia_repository=familia_repository,
        parcialidad_repository=parcialidad_repository
    )
