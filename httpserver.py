from flask import Flask, make_response
from flask_cors import CORS

import grpc
import json

from common import GRPC_PORT_NUMBER, HTTP_PORT_NUMBER
import meterusage_pb2
import meterusage_pb2_grpc

app = Flask(__name__)
CORS(app)

def csv_to_json(metrics_data):
    data = metrics_data.split('\n')[1:-1]
    json_response = []

    for singleline in data:
        columns = singleline.split(',')
        json_response.append({"time": columns[0], "meterusage": columns[1]})
    
    return json.dumps(json_response)

def get_meter_data(stub):
    response = stub.GetMeterUsage(meterusage_pb2.MeterUsageReq())
    return response.data


@app.route('/')
def get_meter_usage_json():
    with grpc.insecure_channel('localhost:' + GRPC_PORT_NUMBER) as channel:
        stub = meterusage_pb2_grpc.MeterUsageStub(channel)
        meter_data = get_meter_data(stub)
        response = make_response(csv_to_json(meter_data))
        return response

if __name__ == '__main__':
    app.run(port=HTTP_PORT_NUMBER)