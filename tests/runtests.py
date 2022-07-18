from testfunctions import test_csv_to_json
from testgrpcserver import run_grpc_tests

if __name__ == '__main__':
    test_csv_to_json()
    run_grpc_tests()