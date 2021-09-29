import json
from flask import request, jsonify

from truck_delivery_rayus007.client import Client
from truck_delivery_rayus007.client_manager import ClientManager


def list_clients():
    """
    list_clients --> lists all the clients
    :return: clients(dict): Dictionary of Clients
    """
    connector = ClientManager()
    result = connector.get_all()
    return jsonify(result)


def save_client():
    """
    save_client --> saves a new client in the clients dictionary
    :return: Success message
    """
    a = request.json
    keys = ["ci", "name", "email", "cellphone", "address", "contract_number", "nit"]
    for k in keys:
        if k not in a:
            raise jsonify({"message": f"{k} parameters are required"})
    client_obj = Client(a["ci"],
                        a["name"],
                        a["email"],
                        a["cellphone"],
                        a["address"],
                        a["contract_number"],
                        a["nit"]
                        )
    connector = ClientManager()
    test1 = connector.save_document(client_obj.ci, client_obj.to_dict())
    return jsonify({"message": f"Client {client_obj.ci} was saved successfully"})


def get_client_by_id(client_id):
    """
    get_client_by_id --> lists an existing client from Clients dictionary
    :param client_id: int value
    :return: client(dict) --> A client
    """
    connector = ClientManager()
    result = connector.get_document(client_id)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Client Not found"}), 404


def delete_client_by_id(client_id):
    """
    delete_client_by_id --> deletes an existing client from clients dictionary
    :param client_id: int value
    :return: Success message
    """
    connector = ClientManager()
    result = connector.get_document(client_id)
    if result:
        connector.delete(client_id)
        return jsonify({"message": f"Client {client_id} was deleted successfully"})
    else:
        return jsonify({"message": "Client Not found, unable to delete."}), 404
