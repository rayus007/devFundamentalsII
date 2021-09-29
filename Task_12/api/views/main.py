from flask import Flask, jsonify, request
from api.views import client_api, truck_api, driver_api

app = Flask(__name__)
API_NAME = "/api/v1"

app.add_url_rule(f"{API_NAME}/clients", view_func=client_api.list_clients)
app.add_url_rule(f"{API_NAME}/clients", view_func=client_api.save_client, methods=["POST"])
app.add_url_rule(f"{API_NAME}/clients/<client_id>", view_func=client_api.get_client_by_id)
app.add_url_rule(f"{API_NAME}/clients/<client_id>", view_func=client_api.delete_client_by_id, methods=["DELETE"])

app.add_url_rule(f"{API_NAME}/trucks", view_func=truck_api.list_trucks)
app.add_url_rule(f"{API_NAME}/trucks/<truck_id>", view_func=truck_api.get_truck_by_id)
app.add_url_rule(f"{API_NAME}/trucks", view_func=truck_api.save_truck, methods=["POST"])
app.add_url_rule(f"{API_NAME}/trucks/<truck_id>", view_func=truck_api.delete_truck_by_id, methods=["DELETE"])

app.add_url_rule(f"{API_NAME}/drivers", view_func=driver_api.list_drivers)
app.add_url_rule(f"{API_NAME}/drivers/<driver_id>", view_func=driver_api.get_driver_by_id)
app.add_url_rule(f"{API_NAME}/drivers", methods=["POST"], view_func=driver_api.save_driver)
app.add_url_rule(f"{API_NAME}/drivers/<driver_id>", view_func=driver_api.delete_driver_by_id, methods=["DELETE"])
app.add_url_rule(f"{API_NAME}/driver/<driver_name>/truck", view_func=driver_api.get_truck_by_driver)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True, port=5000)
