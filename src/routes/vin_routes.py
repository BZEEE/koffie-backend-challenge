import requests
from fastapi import APIRouter, HTTPException
from ..utils.utils import *
from ..constants import *
from ..utils.database_instance import DatabaseInstance
from ..utils.logger import Logger
vin_routes = APIRouter()


@vin_routes.get("/lookup")
async def get_vin(vin: str):
    # validate the vin input
    if not valid_vin(vin):
        raise HTTPException(status_code=BAD_REQUEST_CODE, detail=f"{BAD_REQUEST_MESSAGE}: VIN is not a 17 alphanumeric character string")

    try:
        # check if the vin entry is in the cache
        formatted_vin = format_vin(vin)
        db_instance = DatabaseInstance(CACHE_NAME)
        cache_response = get_vin_in_cache(db_instance, formatted_vin)
        if cache_response is not None:
            cache_response["cachedResult"] = True
            db_instance.close_connection()
            return cache_response

        # make API call to VIN service api if we have a cache miss
        vin_service_response = requests.get(f"{VIN_SERVICE_BASE_URL}/vehicles/DecodeVin/{formatted_vin}?format=json", verify=False)
        if vin_service_response.status_code != HTTP_OK_CODE:
            raise HTTPException(status_code=vin_service_response.status_code, detail=GENERIC_ERROR_MESSAGE)
        vin_results = vin_service_response.json()["Results"]
        make = find_item_in_list(vin_results, "VariableId", MAKE_VARIABLE_ID, "Value")
        model = find_item_in_list(vin_results, "VariableId", MODEL_VARIABLE_ID, "Value")
        model_year = find_item_in_list(vin_results, "VariableId", MODEL_YEAR_VARIABLE_ID, "Value")
        body_class = find_item_in_list(vin_results, "VariableId", BODY_CLASS_VARIABLE_ID, "Value")

        vin_data = {
            "vin": formatted_vin,
            "make": make,
            "model": model,
            "modelYear": model_year,
            "bodyClass": body_class,
        }
        add_vin_entry_to_cache(db_instance, vin_data)
        db_instance.close_connection()
        vin_data["cachedResult"] = False
        return vin_data
    except Exception as e:
        Logger.log(e)
        raise HTTPException(status_code=INTERNAL_SERVER_ERROR_CODE, detail=f"{GENERIC_ERROR_MESSAGE}: Unable to retrieve vin information)")

