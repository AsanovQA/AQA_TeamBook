from faker import Faker

fake = Faker()


class RegisterPageData:
    REGISTER_PAGE_URL = 'https://web.teambooktest.com/register'
    REGISTER_FIRST_NAME_VALID = fake.name()
    REGISTER_FIRST_NAME_INVALID = fake.name(max_nb_chars=21)
    REGISTER_LAST_NAME_VALID = fake.surname()
    REGISTER_LAST_NAME_INVALID = fake.surname(max_nb_chars=21)
    REGISTER_ORGANIZATION_NAME_VALID = fake.text(max_nb_chars=10)
    REGISTER_ORGANIZATION_NAME_INVALID = fake.text(max_nb_chars=200)
    REGISTER_BUSINESS_EMAIL_VALID = fake.email()
    REGISTER_BUSINESS_EMAIL_INVALID = fake.email().replace('@example.com', '@invalid-gmailka.com')
    REGISTERED_BUSINESS_EMAIL_VALID = "regiSTR23_@gmail.com"
    REGISTER_PASSWORD_VALID = "12345678Q"
    REGISTER_PASSWORD_INVALID = "AaAaAaAa"
