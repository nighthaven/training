from src.Models import Base
import sqlalchemy as sa
import enum
import decimal
from sqlalchemy.orm import relationship
import sqlalchemy.orm as sa_orm
from sqlalchemy import Integer, String, ForeignKey

class CharactersStatus(enum.Enum):
    HEALTHY = "en bonne santé"
    CECITY = "cécité"
    BURN = "brulure"
    FROZEN = "gelé"
    POISON = "empoisonné"
    CONFUSION = "confus"





class Characters(Base):
    __tablename__= "characters"

    id = sa.Column(Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(128), nullable=False)
    specieId = sa.Column(String, ForeignKey("specie.id"))
    status = sa.Column(sa.Enum(CharactersStatus, create_constraint=False), nullable=True)
    reputation = sa.Column(sa.Integer, nullable=False, default=50, )
    bounty: decimal.Decimal = sa.Column(
        sa.Numeric(10, 2),
        index=True,
        nullable=False,
    )
    gender = sa.Column(sa.String(128), nullable=False)


class Specie(Base):
    __tablename__= "specie"

    id = sa.Column(Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(128), nullable=False)
    description = sa.Column(sa.String(255), nullable=False)
    character = relationship("characters", back_populates="specie")