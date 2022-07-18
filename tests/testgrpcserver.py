from concurrent import futures
from grpcserver import UsageServer

import grpc
import unittest

import meterusage_pb2
import meterusage_pb2_grpc

class MeterUsageServerTest(unittest.TestCase):
    server_class = UsageServer
    port = 50051
    

    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        meterusage_pb2_grpc.add_MeterUsageServicer_to_server(UsageServer(), self.server)
        self.server.add_insecure_port('[::]:%s' % self.port)
        self.server.start()

    def tearDown(self):
        self.server.stop(None)

    def get_server_responses(self) -> meterusage_pb2.MeterUsageRes:
        with grpc.insecure_channel(f'localhost:{self.port}') as channel:
            stub = meterusage_pb2_grpc.MeterUsageStub(channel)
            response = stub.GetMeterUsage(meterusage_pb2.MeterUsageReq())
        return response

    def test_server(self):
        meter_usage_readings = self.get_server_responses()
        self.assertIsNotNone(meter_usage_readings)

def run_grpc_tests():
    unittest.main()