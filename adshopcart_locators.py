from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
old_username = fake.user_name()
new_username = old_username[0:15]
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
phone = fake.phone_number()
subject = 'Some BBQ and soda would be real good right about now, but lets first get this sorted out.'