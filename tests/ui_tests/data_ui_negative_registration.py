import os
from dotenv import load_dotenv
from faker import Faker

fake = Faker()
load_dotenv()


class RegisterPageData:
    REGISTER_PAGE_URL = os.getenv("REG_URL")
    FIRST_NAME_VALID = fake.name()
    FIRST_NAME_INVALID = fake.name(max_nb_chars=21)
    LAST_NAME_VALID = fake.surname()
    LAST_NAME_INVALID = fake.surname(max_nb_chars=21)
    ORGANIZATION_NAME_VALID = fake.text(max_nb_chars=10)
    ORGANIZATION_NAME_INVALID = fake.text(max_nb_chars=200)
    BUSINESS_EMAIL_VALID = fake.email()
    BUSINESS_EMAIL_INVALID = fake.email().replace('@example.com', '@invalid-gmailka.com')
    PASSWORD_VALID = "12345678Q"
    PASSWORD_INVALID = "AaAaAaAa"
