import pytest
import cards


@pytest.fixture(scope='session')
def db(tmp_path_factory):
    """CardsDB object connected to a temporary database."""
    db_path = tmp_path_factory.mktemp()
    db = cards.CardsDB(db_path)
    yield db
    db.close()
