import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()
for row in c.execute(
    """
    select * from users_user;
    """
):
    print(row)

# auth_group                   users_address
# auth_group_permissions       users_profile
# auth_permission              users_profile_addresses
# django_admin_log             users_user
# django_content_type          users_user_groups
# django_migrations            users_user_user_permissions
# django_session
# sqlite>
