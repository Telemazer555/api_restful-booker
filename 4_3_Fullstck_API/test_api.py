from  const_data import UserSchema
class TestBookingsApiclient:


    def test_get_items(self, api_client, auth_session):
        items_id = api_client.get_items()

        print(f"Успешно получили: {items_id}")

    def test_get_item(self, api_client, auth_session): # Готово!
        item_id = api_client.get_item(10)
        response = item_id
        print(f"Успешно получили: {response.status_code}")
        api_client.validate_response(response,expected_data=response.json(), model=UserSchema)


    def test_create_booking(self, api_client, auth_session, booking_data):
        create_booking = api_client.create_item(booking_data).json()
        uuid = create_booking["bookingid"]

        print(f"Успешно создан item с ID: {uuid}")
        # api_client.delete_item(uuid)

        print(f"Успешно удалён item с ID: {api_client.delete_item(uuid).status_code}")

    def test_client_update(self, api_client, auth_session):
        data = {
            "firstname": "Гонишь не иначе",
            "lastname": "та ты шо",
            "totalprice": 8434,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Breakfast"
        }
        api_client.update_item(1710, upd_item_data=data)

    def test_client_del(self, api_client, auth_session):
        api_client.delete_item(1710)
        print(f"Успешно создан и удален item с ID: {api_client}")

"""

1.Дописать сценарии тестов
2.Надо понять где производить проверку validate_response
3.Может имеет смысл изменить функцию validate_response
4.Почитать ещё раз что писал ментр
5.Реализовать функцию которая будет вытаскивать "bookingid"
"""


class TestBookingScenarios:
    def test_get_and_verify(self,item_scenarios,booking_data):  # Готово!
        item_scenarios.get_and_verify_items_exist()

    def test_create_item_and_delete(self,item_scenarios,booking_data):  # Готово!
        item_scenarios.create_item_and_immediately_delete(item_data=booking_data)

    def test_create_item_and_delete1(self,item_scenarios,booking_data):  # Готово!
        item_scenarios.create_item_and_immediately_delete(item_data=booking_data)

    def test_update_and_get_and_delete(self, item_scenarios, booking_data, booking_data_hard): # Готово!
        item_scenarios.update_item_and_verify_changes_and_delete(item_data=booking_data,upd_item_data=booking_data_hard)

    def test_update(self,item_scenarios, api_client, booking_data, booking_data_hard): # Почти говтово
        crate_booking = api_client.create_item(booking_data).json()
        id = crate_booking['bookingid']
        item_scenarios.update_item_and_verify_changes(id,upd_item_data=booking_data)