from __future__ import print_function

import random

import grpc

import echo_pb2
import echo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = echo_pb2_grpc.EchoServiceStub(channel)
        response = stub.Echo(echo_pb2.EchoRequest(message="huwwo"))
        print(
            f"received: { response.message }, count = { response.message_count }")


if __name__ == '__main__':
    run()
