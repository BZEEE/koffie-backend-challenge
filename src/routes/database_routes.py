from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from ..utils.database_instance import DatabaseInstance
from ..utils.utils import *
from ..constants import *
from ..utils.logger import Logger
database_routes = APIRouter()


@database_routes.delete("/remove/{vin}")
async def remove_vin_from_cache(vin: str):
    # validate the vin input
    if not valid_vin(vin):
        raise HTTPException(status_code=BAD_REQUEST_CODE,
                            detail=f"{BAD_REQUEST_MESSAGE}: VIN is not a 17 alphanumeric character string")
    try:
        # check if the vin entry is in the cache
        formatted_vin = format_vin(vin)
        db_instance = DatabaseInstance(CACHE_NAME)
        delete_vin_query = f"DELETE from {VIN_CACHE_TABLE_NAME} WHERE vin='{formatted_vin}';"
        db_instance.execute_query(delete_vin_query, None, True)
        db_instance.close_connection()
        return {
            "vin": formatted_vin,
            "cacheDeleteSuccess": True
        }
    except Exception as e:
        Logger.log(e)
        raise HTTPException(status_code=INTERNAL_SERVER_ERROR_CODE, detail=f"{GENERIC_ERROR_MESSAGE}: Unable to remove vin from cache")


@database_routes.get("/export")
async def export_database():
    try:
        file_name = "exported_data.parquet"
        db_instance = DatabaseInstance(CACHE_NAME)
        db_instance.export_database_parquet_format(file_name)
        db_instance.close_connection()
        return FileResponse(file_name)
    except Exception as e:
        Logger.log(e)
        raise HTTPException(status_code=INTERNAL_SERVER_ERROR_CODE, detail=f"{GENERIC_ERROR_MESSAGE}: Unable to export database to file")
