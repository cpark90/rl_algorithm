import grpc
import proto.data_types_pb2 as data_types_pb2
import proto.rl_algorithm_prototype_message_pb2 as rl_algorithm_prototype_message_pb2
import proto.rl_algorithm_prototype_pb2_grpc as rl_algorithm_prototype_pb2_grpc

def run():
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
    
        stub = rl_algorithm_prototype_pb2_grpc.RLAlgorithmStub(channel)

        request = rl_algorithm_prototype_message_pb2.GetValueFuncRequest(data="get value function")

        response = stub.GetValueFunc(request)
        print(response)

if __name__ == "__main__":
    run()