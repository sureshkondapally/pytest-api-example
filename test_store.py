from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    """
    Validates that an order can be partially updated using PATCH
    """

    order_id = 1
    test_endpoint = f"/store/order/{order_id}"

    payload = {
        "status": "delivered"
    }

    response = api_helpers.patch_api_data(test_endpoint, payload)

    # Validate response code
    assert response.status_code == 200

    body = response.json()

    # Validate response message
    assert body["message"] == "Order and pet status updated successfully"

    # Validate updated value
    assert body["order"]["status"] == "delivered"
