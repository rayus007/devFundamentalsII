from flask import Flask, jsonify, request

trucks = [
    {
        "id": 1,
        "plate": "abc111",
        "type": "Big111",
        "color": "Yellow111"
    },
    {
        "id": 2,
        "plate": "abc222",
        "type": "SuperBig222",
        "color": "Green222"
    },
    {
        "id": 3,
        "plate": "abc333",
        "type": "SuperBigBig333",
        "color": "Blue333"
    }
]

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

app = Flask(__name__)
API_NAME = "/api/v1"


@app.route(f"{API_NAME}/trucks")
def list_trucks():
    """
    list_trucks --> lists all the trucks
    :return: trucks(dict): Dictionary of Trucks
    """
    return jsonify(trucks)


@app.route(f"{API_NAME}/trucks/<truck_id>")
def get_truck_by_id(truck_id):
    """
    get_truck_by_id --> lists an existing truck from Trucks dictionary
    :param truck_id: int value
    :return: truck(dict) --> A truck
    """
    truck_to_return = {}
    for truck in trucks:
        if truck.get("id") == int(truck_id):
            truck_to_return = truck
            break
    return jsonify(truck_to_return)


@app.route(f"{API_NAME}/trucks", methods=["POST"])
def save_truck():
    """
    save_truck --> saves a new truck in the trucks dictionary
    :return: Success message
    """
    truck_json = request.json
    trucks.append(truck_json)
    return jsonify({"message": "The truck was saved successfully"})


@app.route(f"{API_NAME}/trucks/<truck_id>", methods=["DELETE"])
def delete_truck_by_id(truck_id):
    """
    delete_truck_by_id --> deletes an existing truck from trucks dictionary
    :param truck_id: int value
    :return: Success message
    """
    for truck in trucks:
        if truck.get("id") == int(truck_id):
            trucks.remove(truck)
            break
    return jsonify({"message": "The truck was deleted successfully"})


@app.route(f"{API_NAME}/drivers")
def list_drivers():
    """
    list_drivers --> lists all the drivers
    :return: drivers(dict): Dictionary of Drivers
    """
    return jsonify(drivers)


@app.route(f"{API_NAME}/drivers/<driver_id>")
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


@app.route(f"{API_NAME}/drivers", methods=["POST"])
def save_driver():
    """
    save_driver --> saves a new driver in the drivers dictionary
    :return: Success message
    """
    driver_json = request.json
    drivers.append(driver_json)
    return jsonify({"message": "The driver was saved successfully"})


@app.route(f"{API_NAME}/drivers/<driver_id>", methods=["DELETE"])
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


@app.route(f"{API_NAME}/driver/<driver_name>/truck")
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


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True, port=5000)
