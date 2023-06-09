import pytest
from ambien import assert_matches_shape, config, parametrize_from


@pytest.mark.fullregression
@parametrize_from("get_vin_positive_case.yaml")
def test_get_vin_positive_case(client, data):
    vin_details = client.get(f"{config['base_url']}/lookup?vin={data['vin']}")
    assert_matches_shape(vin_details.status_code, data["response_code"])
    assert_matches_shape(vin_details.json(), data["response"])


@pytest.mark.fullregression
@parametrize_from("get_vin_negative_case.yaml")
def test_get_vin_negative_case(client, data):
    vin_details = client.get(f"{config['base_url']}/lookup?vin={data['vin']}")
    assert_matches_shape(vin_details.status_code, data["response_code"])