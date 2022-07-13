# grpc-microservice
Service providing time-based csv data using grpc

# Pre-requesites
Python 3.5 or higher

```pip``` 9.01 or higher
To update pip:
```python -m pip install --upgrade pip```

To install all required packages:
```pip install -r requirements.txt```

To generate grpc files:
```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. meterusage.proto ```

To run servers:
```python grpc-server.py```
```python http-server.py```