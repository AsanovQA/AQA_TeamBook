import os
from faker import Faker


class RegisterPageData:
    fake = Faker()
    REGISTER_PAGE_URL = os.getenv("REG_URL")
    FIRST_NAME_VALID = fake.first_name()[:10]
    FIRST_NAME_INVALID = fake.first_name()[:1]
    LAST_NAME_VALID = fake.last_name()
    LAST_NAME_INVALID = fake.last_name()[:1]
    ORGANIZATION_NAME_VALID = fake.text(max_nb_chars=10)
    ORGANIZATION_NAME_INVALID = fake.text(max_nb_chars=200)
    BUSINESS_EMAIL_VALID = fake.email()
    BUSINESS_EMAIL_INVALID = "invalid-gmailka.com"
    PASSWORD_VALID = "12345678Q"
    PASSWORD_INVALID = "AaAaAaAa"
# fake.email().replace('@example.com', 'invalid-gmailka.com')
