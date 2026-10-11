from requests import Response
from http import HTTPStatus

class ResponseSpecs:
    @staticmethod
    def request_ok(): # случай успеха в авторизации пользователя
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.OK, response.text #проверка на статус 200
        return confirm

    @staticmethod
    def request_created(): #случай успеха в создании кошелька от юзера
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.CREATED, response.text #проверка на статус 201 при создании кошелька
        return confirm

    @staticmethod
    def request_bad():# случай ошибки 400
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST, response.text # проверка на ошибку 400
        return confirm

    @staticmethod
    def request_unprocessable():# случай ошибки 422 (погашение кредита, неверная сумма погашения)
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, response.text # проверка на ошибку 400
        return confirm

