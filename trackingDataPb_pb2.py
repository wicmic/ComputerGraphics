# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trackingDataPb.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14trackingDataPb.proto\x12\x0etrackingDataPb\"y\n\x0bkeyPointMSG\x12\x0c\n\x04posX\x18\x01 \x01(\x02\x12\x0c\n\x04posY\x18\x02 \x01(\x02\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x0f\n\x07\x61\x62sPosX\x18\x05 \x01(\x02\x12\x0f\n\x07\x61\x62sPosY\x18\x06 \x01(\x02\x12\x0f\n\x07\x61\x62sPosZ\x18\x07 \x01(\x02\"\x99\x01\n\x07poseMSG\x12\n\n\x02id\x18\x01 \x01(\r\x12-\n\x08pitchPos\x18\x02 \x01(\x0b\x32\x1b.trackingDataPb.keyPointMSG\x12.\n\tkeyPoints\x18\x03 \x03(\x0b\x32\x1b.trackingDataPb.keyPointMSG\x12\x10\n\x08\x61\x63tivity\x18\x04 \x01(\x02\x12\x11\n\tidentDesc\x18\x05 \x03(\x02\"\x1b\n\tcameraMSG\x12\x0e\n\x06hPitch\x18\x01 \x03(\x02\"\xa1\x01\n\x08\x66rameMSG\x12\r\n\x05index\x18\x01 \x01(\r\x12,\n\x07\x62\x61llPos\x18\x02 \x01(\x0b\x32\x1b.trackingDataPb.keyPointMSG\x12)\n\x08poseData\x18\x03 \x03(\x0b\x32\x17.trackingDataPb.poseMSG\x12-\n\ncameraData\x18\x04 \x01(\x0b\x32\x19.trackingDataPb.cameraMSG\"R\n\x10videoMetadataMSG\x12\x11\n\tframeRate\x18\x01 \x01(\x02\x12\x0f\n\x07nFrames\x18\x02 \x01(\r\x12\x0c\n\x04resX\x18\x03 \x01(\r\x12\x0c\n\x04resY\x18\x04 \x01(\r\"\x85\x01\n\x0ctrackingData\x12\x13\n\x0binput_video\x18\x01 \x01(\t\x12+\n\tframeData\x18\x02 \x03(\x0b\x32\x18.trackingDataPb.frameMSG\x12\x33\n\tvideoMeta\x18\x03 \x01(\x0b\x32 .trackingDataPb.videoMetadataMSGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trackingDataPb_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KEYPOINTMSG']._serialized_start=40
  _globals['_KEYPOINTMSG']._serialized_end=161
  _globals['_POSEMSG']._serialized_start=164
  _globals['_POSEMSG']._serialized_end=317
  _globals['_CAMERAMSG']._serialized_start=319
  _globals['_CAMERAMSG']._serialized_end=346
  _globals['_FRAMEMSG']._serialized_start=349
  _globals['_FRAMEMSG']._serialized_end=510
  _globals['_VIDEOMETADATAMSG']._serialized_start=512
  _globals['_VIDEOMETADATAMSG']._serialized_end=594
  _globals['_TRACKINGDATA']._serialized_start=597
  _globals['_TRACKINGDATA']._serialized_end=730
# @@protoc_insertion_point(module_scope)
