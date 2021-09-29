import json
from flask import request, jsonify

from api.views.truck_api import trucks

drivers = [
    {
        "id": 1,
        "name": "Pepito1",
        "last_name": "Perez1",
        "license_number": 111111,
        "trunk_id": 1
    },
    {
        "id": 2,
        "name": "Pepito2",
        "last_name": "Perez2",
        "license_number": 222222,
        "trunk_id": 2
    },
    {
        "id": 3,
        "name": "Pepito3",
        "last_name": "Perez3",
        "license_number": 333333,
        "trunk_id": 3
    }
]


def list_drivers():
    """
    list_drivers --> lists all the drivers
    :return: drivers(dict): Dictionary of Drivers
    """
    return jsonify(drivers)


def get_driver_by_id(driver_id):
    """
    get_driver_by_id --> lists an existing truck from Drivers dictionary
    :param driver_id: int value
    :return: driver(dict) --> A driver
    """
    driver_to_return = {}
    for driver in drivers:
        if driver.get("id") == int(driver_id):
            driver_to_return = driver
            break
    return jsonify(driver_to_return)


def save_driver():
    """
    save_driver --> saves a new driver in the drivers dictionary
    :return: Success message
    """
    driver_json = request.json
    drivers.append(driver_json)
    return jsonify({"message": "The driver was saved successfully"})


def delete_driver_by_id(driver_id):
    """
    delete_driver_by_id --> deletes an existing driver from drivers dictionary
    :param driver_id: int value
    :return: Success message
    """
    for driver in drivers:
        if driver.get("id") == int(driver_id):
            drivers.remove(driver)
            break
    return jsonify({"message": "The driver was deleted successfully"})


def get_truck_by_driver(driver_name):
    """
    get_truck_by_driver --> lists existing truck associated to a driver name
    :param driver_name: string value
    :return: truck(dict): A truck
    """
    truck_to_return = {}
    for driver in drivers:
        if driver.get("name") == driver_name:
            truck_to_return = trucks.__getitem__(driver.get("id")-1)
    return jsonify(truck_to_return)
