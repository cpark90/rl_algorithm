import proto.rl_algorithm_prototype_pb2_grpc as rl_algorithm_prototype
import proto.rl_algorithm_prototype_message_pb2 as rl_algorithm_prototype_message
import proto.data_types_pb2 as data_types
from rl_algorithm.algorithms import PrototypeAlgorithm

class PrototypeServicer(rl_algorithm_prototype.RLAlgorithmServicer):
    def Init(self, request, context):
        metadata = dict(context.invocation_metadata())

        result = data_types.ResultType()
        return rl_algorithm_prototype_message.InitResponse(result=result)

    def Act(self, request, context):
        metadata = dict(context.invocation_metadata())

        action = data_types.Action()
        return rl_algorithm_prototype_message.ActResponse(action=action)
        
    def ValueFuncUpdate(self, request, context):
        metadata = dict(context.invocation_metadata())

        result = data_types.ResultType()
        return rl_algorithm_prototype_message.ValueFuncUpdateResponse(result=result)

    def PolicyUpdate(self, request, context):
        metadata = dict(context.invocation_metadata())

        result = data_types.ResultType()
        return rl_algorithm_prototype_message.PolicyUpdateResponse(result=result)

    def GetValueFunc(self, request, context):
        metadata = dict(context.invocation_metadata())

        value_function = data_types.ValueFunction()
        return rl_algorithm_prototype_message.GetValueFuncResponse(value_function=value_function)

    def GetPolicy(self, request, context):
        metadata = dict(context.invocation_metadata())

        policy = data_types.Policy()
        return rl_algorithm_prototype_message.GetPolicyResponse(policy=policy)