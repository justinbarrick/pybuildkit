# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from github.com.moby.buildkit.api.services.control import control_pb2 as github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2


class ControlStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DiskUsage = channel.unary_unary(
        '/moby.buildkit.v1.Control/DiskUsage',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.DiskUsageRequest.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.DiskUsageResponse.FromString,
        )
    self.Prune = channel.unary_stream(
        '/moby.buildkit.v1.Control/Prune',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.PruneRequest.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.UsageRecord.FromString,
        )
    self.Solve = channel.unary_unary(
        '/moby.buildkit.v1.Control/Solve',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.SolveRequest.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.SolveResponse.FromString,
        )
    self.Status = channel.unary_stream(
        '/moby.buildkit.v1.Control/Status',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.StatusRequest.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.StatusResponse.FromString,
        )
    self.Session = channel.stream_stream(
        '/moby.buildkit.v1.Control/Session',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.BytesMessage.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.BytesMessage.FromString,
        )
    self.ListWorkers = channel.unary_unary(
        '/moby.buildkit.v1.Control/ListWorkers',
        request_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.ListWorkersRequest.SerializeToString,
        response_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.ListWorkersResponse.FromString,
        )


class ControlServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DiskUsage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Prune(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Solve(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Session(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DiskUsage': grpc.unary_unary_rpc_method_handler(
          servicer.DiskUsage,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.DiskUsageRequest.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.DiskUsageResponse.SerializeToString,
      ),
      'Prune': grpc.unary_stream_rpc_method_handler(
          servicer.Prune,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.PruneRequest.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.UsageRecord.SerializeToString,
      ),
      'Solve': grpc.unary_unary_rpc_method_handler(
          servicer.Solve,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.SolveRequest.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.SolveResponse.SerializeToString,
      ),
      'Status': grpc.unary_stream_rpc_method_handler(
          servicer.Status,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.StatusRequest.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.StatusResponse.SerializeToString,
      ),
      'Session': grpc.stream_stream_rpc_method_handler(
          servicer.Session,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.BytesMessage.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.BytesMessage.SerializeToString,
      ),
      'ListWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.ListWorkers,
          request_deserializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.ListWorkersRequest.FromString,
          response_serializer=github_dot_com_dot_moby_dot_buildkit_dot_api_dot_services_dot_control_dot_control__pb2.ListWorkersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'moby.buildkit.v1.Control', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))