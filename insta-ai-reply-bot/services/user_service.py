from sqlalchemy.orm import Session

from memory.database import get_session
from memory.models import User


def get_or_create_user(instagram_id: str):

    db: Session = get_session()

    user = (
        db.query(User)
        .filter(
            User.instagram_id == instagram_id
        )
        .first()
    )

    if user:
        return user.id


    user = User(
        instagram_id=instagram_id,
        humor_style="sarcastic friend",
        language="english"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user.id