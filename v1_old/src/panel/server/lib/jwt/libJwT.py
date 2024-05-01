import django
django.setup()

import jwt
from datetime import datetime, timedelta
from configs.config import Config, DevelopmentConfig, ProductionConfig

class JWTAuthenticator:
    def __init__(self):
        # self.secret_key    = ProductionConfig.SECRET_KEY
        self.secret_key      = DevelopmentConfig.SECRET_KEY
        self.algorithm       = Config.jwt_def_algo
        self.expiration_time = timedelta(hours=Config.jwt_expiration_time)

    def generate_token(self, payload):
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token, model="Customer"):
        try:
            payload   = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            api_key   = payload['api_key']
            full_name = payload['full_name']

            # if api_key and full_name: #TODO: Make this integration modular for all around usage
            if model == "Customer":
                from Login.models import Customer

                user = Customer.objects.get(api_key=api_key, full_name=full_name)

                if user:
                    return True

            elif model == "Employee":
                from Login.models import EmployeeUser
                
                user = EmployeeUser.objects.get(api_key=api_key, full_name=full_name)

                if user:
                    return True

            else:
                return None
            
            return False
            
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        


# Python
# import jwt
# from Login.models import Customer

# authenticator = JWTAuthenticator()

# # Generate a token
# payload = {
#     "api_key": "my_api_key",
#     "full_name": "John Doe"
# }

# token = authenticator.generate_token(payload)

# # Decode the token
# decoded_token = authenticator.decode_token(token, model="Customer")

# # Check if the token is valid
# if decoded_token:
#     print("The token is valid")

#     # Get the customer from the database
#     customer = Customer.objects.get(api_key=decoded_token["api_key"], full_name=decoded_token["full_name"])

#     # Do something with the customer
#     print(customer)
# else:
#     print("The token is invalid")
