import pytest
from SRC.main.api.models.create_user_request import CreateUserRequest
from SRC.main.api.generators.model_generator import RandomModelGenerator
from SRC.main.api.db.crud.user_crud import UserCrudDb as User
from SRC.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session


@pytest.mark.api
class TestCreateUser:
    # проверка авторизации админа и получение админ токена
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(self, api_manager: ApiManager, create_user_request: CreateUserRequest,
                               db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username, 'Имя созданного пользователя совпадать с запросом'
        assert create_user_request.role == response.role, 'Роль созданного пользователя совпадать с запросом'

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, 'Имя пользователя в БД должно совпадать с запросом'

    # прогон входных данных, заведомо ложных, различного характера по условию к проекту
    @pytest.mark.parametrize("username,password",
                             [("абв", "Pas!sw0rd"),
                              ("ab", "Pas!sw0rd"),
                              ("abv!", "Pas!sw0rd"),
                              ("Maxx1", "Pas!sw0rд"),
                              ("Maxx2", "Pas!sw0"),
                              ("Maxx3", "pas!sw0rd"),
                              ("Maxx4", "PAS!SWORD"),
                              ("Maxx5", "PASSSWORD"),
                              ("Maxx6", "PAS!SWRRD")])
    def test_create_user_invalid(self, username: str, password: str, api_manager: ApiManager, db_session: Session):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)
        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, 'Пользователь создан, ошибка'
