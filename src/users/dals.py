from src.models.src.dals import BaseDAL
from src.models.src.modules.users import User


class UserDAL(BaseDAL[User]):
    pass


user_dal = UserDAL(User)
