from rl_algorithm.grpc_server import GrpcServer
from rl_algorithm.services.prototype_service import PrototypeServicer
import proto.rl_algorithm_prototype_pb2_grpc as rl_algorithm_prototype_pb2_grpc

if __name__ == "__main__":
    server = GrpcServer(rl_algorithm_prototype_pb2_grpc, "RLAlgorithmServicer", PrototypeServicer)
    server.serve()