from address import Address
from mailing import Mailing

from_address = Address(
    "123800",
    "Москва",
    "Личная",
    "10",
    "6"
)

to_address = Address(
    "190000",
    "Санкт-Петербург",
    "Мытная",
    "13",
    "26"
)
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="12312ХХХХ"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.flat}. "
    f"Стоимость {mailing.cost} рублей."
)
