from sqlalchemy.orm import Session
from typing import Optional
from app.persistence.model.usuario import Usuario
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

class UsuarioRepository(BaseRepository, IUsuarioRepository):
    def __init__(self, db: Session):
        super().__init__(Usuario, db)

    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def update_password(self, email: str, password: str) -> Optional[Usuario]:
        usuario = self.get_by_email(email)
        if usuario:
            usuario.password = password
            self.db.commit()
            self.db.refresh(usuario)
        return usuario
