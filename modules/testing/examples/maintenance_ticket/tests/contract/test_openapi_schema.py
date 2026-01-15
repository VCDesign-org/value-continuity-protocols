import os
import schemathesis

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

schema = schemathesis.from_path("openapi.yaml", base_url=BASE_URL)

@schema.parametrize()
def test_openapi_contract(case):
    """
    Contract test:
    - Request/response should conform to OpenAPI.
    - We deliberately do NOT assert internal rules here.
    """
    response = case.call()
    case.validate_response(response)
