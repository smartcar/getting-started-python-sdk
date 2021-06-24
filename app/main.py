import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

# SETUP: Export your client id, secret, and redirect URI as environment variables.
# #
# # Open your terminal
# # export SMARTCAR_CLIENT_ID=<your client id>
# # export SMARTCAR_CLIENT_SECRET=<your client secret>
# # export SMARTCAR_REDIRECT_URI=<your redirect URI>


app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None

# Ensure SETUP is completed, then instantiate an AuthClient
client = smartcar.AuthClient(test_mode=True)

# scope of permissions
scope = ['read_vehicle_info']


@app.route('/login', methods=['GET'])
def login():
    auth_url = client.get_auth_url(scope)
    return redirect(auth_url)


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')

    # access our global variable and store our access tokens
    global access

    # in a production app you'll want to store this in some kind of
    # persistent storage
    access = client.exchange_code(code)
    return '', 200


@app.route('/vehicle', methods=['GET'])
def vehicle():
    # access our global variable to retrieve our access tokens
    global access

    # receive a `Vehicles` NamedTuple, which has an attribute of 'vehicles' and 'meta'
    V = smartcar.get_vehicle_ids(access['access_token'])

    # get the first vehicle
    id_of_first_vehicle = V.vehicles[0]

    # instantiate the first vehicle in the vehicle id list
    vehicle = smartcar.Vehicle(id_of_first_vehicle, access['access_token'])

    # use the attributes() method to call to Smartcar API and get information about the vehicle.
    # These vehicle methods return NamedTuples with attributes
    attributes = vehicle.attributes()

    # play around with the info attributes
    print(attributes.make)
    print(attributes.model)
    print(attributes.year)

    # Check out the meta attribute,
    # which contains the response headers (and other information) about the request
    print(attributes.meta)

    # NamedTuples can be transformed into a dictionary
    attributes_dict = attributes._asdict()

    return jsonify(attributes_dict)


if __name__ == '__main__':
    app.run(port=8000)
