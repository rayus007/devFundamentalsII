import json
from flask import request, jsonify

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


def list_trucks():
    """
    list_trucks --> lists all the trucks
    :return: trucks(dict): Dictionary of Trucks
    """
    return jsonify(trucks)


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


def save_truck():
    """
    save_truck --> saves a new truck in the trucks dictionary
    :return: Success message
    """
    truck_json = request.json
    trucks.append(truck_json)
    return jsonify({"message": "The truck was saved successfully"})


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
