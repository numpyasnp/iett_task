from typing import Optional

from model_bakery import baker


class BaseDriverMixin:

    def create_driver(
        self,
        personal_id: Optional[str] = None,
        license_number: Optional[str] = None,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
    ):
        personal_id = personal_id or "123"
        license_number = license_number or "456"
        name = name or "John Doe"
        phone_number = phone_number or "+905553331122"
        return baker.make(
            "driver.Driver",
            name=name,
            personal_id=personal_id,
            license_number=license_number,
            phone_number=phone_number,
        )
