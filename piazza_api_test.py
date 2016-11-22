from piazza_api import Piazza
p = Piazza()
p.user_login( 'your_email_address','your_password' )

user_profile = p.get_user_profile()
cs189 = p.network("h15qm84dl14t3x2")
cs189.get_post(20)

posts = cs189.iter_all_posts(limit=10)

for post in posts:
    print post


