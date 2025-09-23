from pydantic import BaseModel
from typing import Optional
import json
import os
import dotenv

dotenv.load_dotenv()
HEADERS = os.environ.get('HEADERS')
HEADERS = json.loads(HEADERS)
BASE_URL = os.environ.get('BASE_URL')
JSON_BODY = os.environ.get('JSON_BODY')
JSON_BODY = json.loads(JSON_BODY)


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BaseBookingSchema(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: dict
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

class UserSchema2(BaseModel):
    bookingid: int
    booking: BaseBookingSchema


class UpdateBookingSchema(BaseBookingSchema):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None