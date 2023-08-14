import os
from dotenv import load_dotenv, find_dotenv  # for using dotenv

load_dotenv(find_dotenv()) # loading up the .env file

class Config(object):
    DEBUG                           = True # auto reloading the app
    TESTING                         = False
    CSRF_ENABLED                    = True
    apphost                         = os.getenv("HOST")  #<===> where it's being hosted
    port                            = os.getenv("PORT")  #<===> which port is being hosted on
    db_unique                       = True

    #<========================================================> jwt
    jwt_expiration_time = 72
    jwt_def_algo        = 'HS256'
    #<========================================================> jwt

    #<========================================================> cookie handling HTTPS and other security
    SESSION_COOKIE_SECURE   = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    #<========================================================> cookie handling HTTPS and other security

    #<========================================================> mailing
    DEFAULT_FROM   = os.getenv('DEFAULT_FROM')
    MAIL_SERVER    = 'smtp.gmail.com'
    MAIL_PORT      = 587 #<===================================> the better port for sending email
    MAIL_USE_TLS   = False
    MAIL_USE_SSL   = True
    MAIL_USERNAME  = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD  = os.getenv("MAIL_PASSWORD")
    #<========================================================> mailing

    #<========================================================> database
    db_ip          = os.getenv("ip")
    db_name        = os.getenv("db")
    db_username    = os.getenv("username")
    db_password    = os.getenv("password")
    #<========================================================> database

    #<========================================================> isntabot
    user_name_insta = os.getenv("instagram_login_username")
    pass_word_insta = os.getenv("instagram_login_password")
    #<========================================================> isntabot


class ProductionConfig(Config):
    DEBUG                           = False
    SECRET_KEY                      = os.getenv("secret_key_production")
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    Threaded                        = True

    # isntabot
    # user_name_insta_production = os.getenv("instagram_login_username")
    # pass_word_insta_production = os.getenv("instagram_login_password") 


class DevelopmentConfig(Config):
    ENV                             = "Development"
    DEVELOPMENT                     = True
    SECRET_KEY                      = os.getenv("secret_key_dev")
    OAUTHLIB_INSECURE_TRANSPORT     = True
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

    # isntabot
    # user_name_insta_dev = os.getenv("instagram_login_username")
    # pass_word_insta_dev = os.getenv("instagram_login_password")
