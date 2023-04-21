from jwt_authentication import models, create_app
from database import engine


models.Base.metadata.create_all(engine)

app = create_app()
