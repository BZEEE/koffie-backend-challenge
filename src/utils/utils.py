import re
from ..constants import VIN_CACHE_TABLE_NAME
from ..utils.database_instance import FetchOptions


def valid_vin(vin: str):
    vin_regex_pattern = "^[0-9A-Za-z]{17}$"
    return vin is not None and re.match(vin_regex_pattern, vin)


def format_vin(vin: str):
    return vin.upper()


def find_item_in_list(item_list, key_name_to_match, target, key_name_to_return):
    for item in item_list:
        if item[key_name_to_match] == target:
            return item[key_name_to_return]
    return None


def create_cache_if_doesnt_exist(database):
    create_table_query = f"CREATE TABLE IF NOT EXISTS {VIN_CACHE_TABLE_NAME} (`vin` char(17) NOT NULL,`make` varchar(30) NULL,`model` varchar(30) NULL,`model_year` varchar(4) NULL,`body_class` varchar(50) NULL,PRIMARY KEY  (`vin`));"
    database.execute_query(create_table_query, None, True)


def get_vin_in_cache(database, vin: str):
    create_cache_if_doesnt_exist()
    get_vin_in_cache_query = f"SELECT vin, make, model, model_year, body_class FROM {VIN_CACHE_TABLE_NAME} WHERE vin='{vin}';"
    cache_response = database.execute_query(get_vin_in_cache_query, FetchOptions.FETCH_ONE, False)
    if cache_response is None or len(cache_response) == 0:
        return None
    return {
        "vin": cache_response[0],
        "make": cache_response[1],
        "model": cache_response[2],
        "modelYear": cache_response[3],
        "bodyClass": cache_response[4]
    }


def add_vin_entry_to_cache(database, data):
    create_cache_if_doesnt_exist()
    add_vin_query = f"INSERT INTO {VIN_CACHE_TABLE_NAME} (vin, make, model, model_year, body_class) VALUES ('{data['vin']}', '{data['make']}', '{data['model']}', '{data['modelYear']}', '{data['bodyClass']}');"
    database.execute_query(add_vin_query, None, True)


def delete_vin_from_cache(database, vin: str):
    create_cache_if_doesnt_exist()
    delete_vin_query = f"DELETE FROM {VIN_CACHE_TABLE_NAME} WHERE vin='{vin}';"
    database.execute_query(delete_vin_query, None, True)
