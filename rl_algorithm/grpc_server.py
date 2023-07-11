from concurrent import futures
import grpc

class GrpcServer(object):

    def __init__(self, service_grpc_module, servicer_name, servicer_module, addr='0.0.0.0:50051', max_workers=10):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        getattr(service_grpc_module, "add_" + servicer_name + "_to_server")(servicer_module(), self.server)
        self.server.add_insecure_port(addr)
    
    def serve(self):
        print("run server")
        self.server.start()
        self.server.wait_for_termination()