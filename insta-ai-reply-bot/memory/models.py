from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
    JSON,
    text
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from memory.database import Base



class User(Base):

    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    instagram_id = Column(
        String,
        unique=True,
        nullable=False
    )

    humor_style = Column(
        String,
        default="sarcastic friend"
    )

    language = Column(
        String,
        default="english"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    user_message = Column(
        Text
    )

    bot_response = Column(
        Text
    )

    response_type = Column(
        String
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class AgentState(Base):

    __tablename__ = "agent_state"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    state_json = Column(
        JSON
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
