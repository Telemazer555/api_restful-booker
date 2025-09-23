import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type
from const_data import BASE_URL
from const_data import UserSchema2, UpdateBookingSchema


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = BASE_URL  # Можно также передавать в конструктор, если он может меняться

    def get_items(self):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/booking")
        if response.status_code != 200:
            response.raise_for_status()

        return response

    def get_item(self, id_item):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/booking/{id_item}")

        if response.status_code != 200:
            response.raise_for_status()

        return response

    def create_item(self, item_data):
        """Отправляет запрос на создание item."""
        response = self.auth_session.post(f"{self.base_url}/booking", json=item_data)
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status()  # Выбросит HTTPError для плохих статусов

        return response

    def update_item(self, item_id, upd_item_data):
        """Отправляет запрос на обновление item."""
        response = self.auth_session.put(f"{self.base_url}/booking/{item_id}", json=upd_item_data)
        if response.status_code != 200:
            response.raise_for_status()
        return response

    def delete_item(self, item_id):
        """Отправляет запрос на удаление item."""
        response = self.auth_session.delete(f"{self.base_url}/booking/{item_id}")

        if response.status_code != 200:  # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response  # или response.status_code

    def validate_response(self, response: Response,
                          model: Type[BaseModel],
                          expected_status: int = 200,
                          expected_data: dict | None = None
                          ) -> BaseModel:
        if response.status_code != expected_status:
            pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")
        try:
            data = response.json()
        except Exception as e:
            pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")
        try:
            parsed = model(**data)
        except ValidationError as e:
            pytest.fail(f"Pydantic валидация не прошла:\n{e}")
        if expected_data:
            # Обернём данные в такую же модель для сравнения
            expected_model = model(**expected_data)
            if parsed.model_dump(exclude_unset=True) != expected_model.model_dump(exclude_unset=True):
                pytest.fail(
                    f"Данные ответа не совпадают с ожидаемыми:\n"
                    f"Expected: {expected_model.model_dump()}\n"
                    f"Actual:   {parsed.model_dump()}"
                )

        return parsed


class ItemScenarios:
    def __init__(self, api_client: ItemApiClient):  # Типизация для ясности
        self.api_client = api_client

    def create_item_and_immediately_delete(self, item_data):
        """
        Сценарий: создать item, проверить его ответ через валидатор и сразу же его удалить.
        Возвращает ID созданного и удаленного item.
        """
        created_item_data = self.api_client.create_item(item_data)
        self.api_client.validate_response(created_item_data, expected_data=created_item_data.json(), model=UserSchema2)
        item_id = created_item_data.json().get("bookingid")
        self.api_client.get_item(item_id)
        print(
            f"\n ID {item_id} успешно создан.\n ID {item_id} Успешно удалён. статус код: {self.api_client.delete_item(item_id).status_code}.")
        return item_id

    def get_and_verify_items_exist(self):
        """
        Сценарий: получить список items и проверить, что он не пуст.
        """
        items = self.api_client.get_items().json()
        assert len(items) > 0, "Список items пуст"
        print(f"\nПолучено {len(items)} items.")
        return items

    def update_item_and_verify_changes_and_delete(self, item_data, upd_item_data):
        create_booking = self.api_client.create_item(item_data)
        self.api_client.validate_response(create_booking, expected_data=create_booking.json(), model=UserSchema2)

        id = create_booking.json()['bookingid']
        firstname = create_booking.json()['booking']['firstname']
        lastname = create_booking.json()['booking']['lastname']

        up_booking_data = self.api_client.update_item(id, upd_item_data)
        self.api_client.validate_response(up_booking_data, expected_data=up_booking_data.json(),
                                          model=UpdateBookingSchema)

        up_firstname = up_booking_data.json()['firstname']
        up_lastname = up_booking_data.json()['lastname']

        assert up_firstname != firstname, "Имя  совпадает"
        assert up_lastname != lastname, "Фамилия  совпадает"

        print(f"\nУспешно удалён item с ID:{id} и стаскодом {self.api_client.delete_item(id).status_code}")
