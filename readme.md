# grpc-pyserver-jsclient
A demo repo to connect a python server with a js cient using the gRPC framework.

## quick start
```
docker-compose up --build
```

http://localhost:8081/echotest.html


## python server notes
implemented only unary and one-way streaming (server -> client).

### install grpcio via pip
```
python -m pip install grpcio  &&
  python -m pip install grpcio-tools
```

### generate grpc code
```
cd server
python -m grpc_tools.protoc
  -I../common --python_out=.
  --grpc_python_out=. ../common/echo.proto
```

### run docker container with server
(if not using docker-compose)
```
docker build -t grpcmatt/python-server .
docker run -p 9090:9090 grpcmatt/python-server
```


## js client notes
All the js code for this comes straight from here: https://github.com/grpc/grpc-web  

## envoy
Need to use envoy server as middle man between js client to python server.
