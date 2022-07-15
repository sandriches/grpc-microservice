import grpc
import os

from concurrent import futures

from common import METER_FILE_PATH, MAX_WORKERS, GRPC_PORT_NUMBER
import meterusage_pb2
import meterusage_pb2_grpc

class UsageServer(meterusage_pb2_grpc.MeterUsageServicer):
     def GetMeterUsage(self, request, context):
        if not os.path.isfile(METER_FILE_PATH):
            return meterusage_pb2.MeterUsageRes(data=None)
        
        file = open(METER_FILE_PATH, 'r')
        file_content=file.read()
        
        return meterusage_pb2.MeterUsageRes(data=file_content)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    meterusage_pb2_grpc.add_MeterUsageServicer_to_server(
        UsageServer(), server)

    server.add_insecure_port('[::]:' + GRPC_PORT_NUMBER)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
