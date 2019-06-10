# python server for grpc

### install grpcio via pip
```
python -m pip install grpcio  &&
  python -m pip install grpcio-tools
```

### generate grpc code
```
python -m grpc_tools.protoc
  -I../../common --python_out=.
  --grpc_python_out=. ../../common/echo.proto
```


### run docker container with server
(if not using docker-compose)
```
docker build -t grpcmatt/python-server .
docker run -p 9090:9090 grpcmatt/python-server
```