from datetime import timedelta

PROPAGATE_EXCEPTIONS = True

# Database configuration
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://uysql6vnmrhfekwq:mqG7EqQvmvxhFkXLfImw@btsycof16y4ge6iev5oy-mysql.services.clever-cloud.com:3306/btsycof16y4ge6iev5oy"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False
# flask-jwt configuration
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
JWT_SECRET_KEY = "123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789"
