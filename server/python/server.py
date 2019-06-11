"""The Python implementation of the GRPC echo server."""

from concurrent import futures
import time
import logging

import grpc

import echo_pb2
import echo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Echo(echo_pb2_grpc.EchoServiceServicer):

    def Echo(self, request, context):
        print(f"received an echo request (unary)... { request.message }")
        return echo_pb2.EchoResponse(
            message='Hello, %s!' % request.message,
            message_count=22
        )

    def ServerStreamingEcho(self, request, context):
        print(
            f"received an echo request (streaming)... "
            f"{ request.message } / { request.message_count } / "
            f"{ request.message_interval }")
        for i in range(0, request.message_count):
            yield echo_pb2.ServerStreamingEchoResponse(
                message='Streamin @ ya, %s!' % request.message
            )
            time.sleep(request.message_interval / 1000)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServiceServicer_to_server(Echo(), server)
    server.add_insecure_port('[::]:9090')
    server.start()
    print("server started listening on port 9090")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
