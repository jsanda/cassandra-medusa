# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: medusa.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='medusa.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmedusa.proto\"d\n\rBackupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x04mode\x18\x02 \x01(\x0e\x32\x13.BackupRequest.Mode\"\"\n\x04Mode\x12\x10\n\x0c\x44IFFERENTIAL\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\"\x10\n\x0e\x42\x61\x63kupResponse\")\n\x13\x42\x61\x63kupStatusRequest\x12\x12\n\nbackupName\x18\x01 \x01(\t\"\x83\x01\n\x14\x42\x61\x63kupStatusResponse\x12\x15\n\rfinishedNodes\x18\x01 \x03(\t\x12\x17\n\x0funfinishedNodes\x18\x02 \x03(\t\x12\x14\n\x0cmissingNodes\x18\x03 \x03(\t\x12\x11\n\tstartTime\x18\x04 \x01(\t\x12\x12\n\nfinishTime\x18\x05 \x01(\t\"#\n\x13\x44\x65leteBackupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x14\x44\x65leteBackupResponse\"\x13\n\x11GetBackupsRequest\"5\n\x12GetBackupsResponse\x12\x1f\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32\x0e.BackupSummary\"u\n\rBackupSummary\x12\x12\n\nbackupName\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x12\n\nfinishTime\x18\x03 \x01(\x03\x12\x12\n\ntotalNodes\x18\x04 \x01(\x05\x12\x15\n\rfinishedNodes\x18\x05 \x01(\x05\"\x15\n\x13ReloadConfigRequest\"\x16\n\x14ReloadConfigResponse2\xa1\x02\n\x06Medusa\x12)\n\x06\x42\x61\x63kup\x12\x0e.BackupRequest\x1a\x0f.BackupResponse\x12;\n\x0c\x42\x61\x63kupStatus\x12\x14.BackupStatusRequest\x1a\x15.BackupStatusResponse\x12;\n\x0c\x44\x65leteBackup\x12\x14.DeleteBackupRequest\x1a\x15.DeleteBackupResponse\x12\x35\n\nGetBackups\x12\x12.GetBackupsRequest\x1a\x13.GetBackupsResponse\x12;\n\x0cReloadConfig\x12\x14.ReloadConfigRequest\x1a\x15.ReloadConfigResponseb\x06proto3'
)



_BACKUPREQUEST_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='BackupRequest.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIFFERENTIAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=82,
  serialized_end=116,
)
_sym_db.RegisterEnumDescriptor(_BACKUPREQUEST_MODE)


_BACKUPREQUEST = _descriptor.Descriptor(
  name='BackupRequest',
  full_name='BackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BackupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='BackupRequest.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BACKUPREQUEST_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=116,
)


_BACKUPRESPONSE = _descriptor.Descriptor(
  name='BackupResponse',
  full_name='BackupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=134,
)


_BACKUPSTATUSREQUEST = _descriptor.Descriptor(
  name='BackupStatusRequest',
  full_name='BackupStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='BackupStatusRequest.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=177,
)


_BACKUPSTATUSRESPONSE = _descriptor.Descriptor(
  name='BackupStatusResponse',
  full_name='BackupStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='finishedNodes', full_name='BackupStatusResponse.finishedNodes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unfinishedNodes', full_name='BackupStatusResponse.unfinishedNodes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missingNodes', full_name='BackupStatusResponse.missingNodes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='BackupStatusResponse.startTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishTime', full_name='BackupStatusResponse.finishTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=311,
)


_DELETEBACKUPREQUEST = _descriptor.Descriptor(
  name='DeleteBackupRequest',
  full_name='DeleteBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DeleteBackupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=348,
)


_DELETEBACKUPRESPONSE = _descriptor.Descriptor(
  name='DeleteBackupResponse',
  full_name='DeleteBackupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=372,
)


_GETBACKUPSREQUEST = _descriptor.Descriptor(
  name='GetBackupsRequest',
  full_name='GetBackupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=393,
)


_GETBACKUPSRESPONSE = _descriptor.Descriptor(
  name='GetBackupsResponse',
  full_name='GetBackupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backups', full_name='GetBackupsResponse.backups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=448,
)


_BACKUPSUMMARY = _descriptor.Descriptor(
  name='BackupSummary',
  full_name='BackupSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='BackupSummary.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='BackupSummary.startTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishTime', full_name='BackupSummary.finishTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalNodes', full_name='BackupSummary.totalNodes', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishedNodes', full_name='BackupSummary.finishedNodes', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=567,
)


_RELOADCONFIGREQUEST = _descriptor.Descriptor(
  name='ReloadConfigRequest',
  full_name='ReloadConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=590,
)


_RELOADCONFIGRESPONSE = _descriptor.Descriptor(
  name='ReloadConfigResponse',
  full_name='ReloadConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=614,
)

_BACKUPREQUEST.fields_by_name['mode'].enum_type = _BACKUPREQUEST_MODE
_BACKUPREQUEST_MODE.containing_type = _BACKUPREQUEST
_GETBACKUPSRESPONSE.fields_by_name['backups'].message_type = _BACKUPSUMMARY
DESCRIPTOR.message_types_by_name['BackupRequest'] = _BACKUPREQUEST
DESCRIPTOR.message_types_by_name['BackupResponse'] = _BACKUPRESPONSE
DESCRIPTOR.message_types_by_name['BackupStatusRequest'] = _BACKUPSTATUSREQUEST
DESCRIPTOR.message_types_by_name['BackupStatusResponse'] = _BACKUPSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteBackupRequest'] = _DELETEBACKUPREQUEST
DESCRIPTOR.message_types_by_name['DeleteBackupResponse'] = _DELETEBACKUPRESPONSE
DESCRIPTOR.message_types_by_name['GetBackupsRequest'] = _GETBACKUPSREQUEST
DESCRIPTOR.message_types_by_name['GetBackupsResponse'] = _GETBACKUPSRESPONSE
DESCRIPTOR.message_types_by_name['BackupSummary'] = _BACKUPSUMMARY
DESCRIPTOR.message_types_by_name['ReloadConfigRequest'] = _RELOADCONFIGREQUEST
DESCRIPTOR.message_types_by_name['ReloadConfigResponse'] = _RELOADCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackupRequest = _reflection.GeneratedProtocolMessageType('BackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupRequest)
  })
_sym_db.RegisterMessage(BackupRequest)

BackupResponse = _reflection.GeneratedProtocolMessageType('BackupResponse', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupResponse)
  })
_sym_db.RegisterMessage(BackupResponse)

BackupStatusRequest = _reflection.GeneratedProtocolMessageType('BackupStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSTATUSREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupStatusRequest)
  })
_sym_db.RegisterMessage(BackupStatusRequest)

BackupStatusResponse = _reflection.GeneratedProtocolMessageType('BackupStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSTATUSRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupStatusResponse)
  })
_sym_db.RegisterMessage(BackupStatusResponse)

DeleteBackupRequest = _reflection.GeneratedProtocolMessageType('DeleteBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:DeleteBackupRequest)
  })
_sym_db.RegisterMessage(DeleteBackupRequest)

DeleteBackupResponse = _reflection.GeneratedProtocolMessageType('DeleteBackupResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:DeleteBackupResponse)
  })
_sym_db.RegisterMessage(DeleteBackupResponse)

GetBackupsRequest = _reflection.GeneratedProtocolMessageType('GetBackupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPSREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:GetBackupsRequest)
  })
_sym_db.RegisterMessage(GetBackupsRequest)

GetBackupsResponse = _reflection.GeneratedProtocolMessageType('GetBackupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPSRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:GetBackupsResponse)
  })
_sym_db.RegisterMessage(GetBackupsResponse)

BackupSummary = _reflection.GeneratedProtocolMessageType('BackupSummary', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSUMMARY,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupSummary)
  })
_sym_db.RegisterMessage(BackupSummary)

ReloadConfigRequest = _reflection.GeneratedProtocolMessageType('ReloadConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELOADCONFIGREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:ReloadConfigRequest)
  })
_sym_db.RegisterMessage(ReloadConfigRequest)

ReloadConfigResponse = _reflection.GeneratedProtocolMessageType('ReloadConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _RELOADCONFIGRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:ReloadConfigResponse)
  })
_sym_db.RegisterMessage(ReloadConfigResponse)



_MEDUSA = _descriptor.ServiceDescriptor(
  name='Medusa',
  full_name='Medusa',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=617,
  serialized_end=906,
  methods=[
  _descriptor.MethodDescriptor(
    name='Backup',
    full_name='Medusa.Backup',
    index=0,
    containing_service=None,
    input_type=_BACKUPREQUEST,
    output_type=_BACKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BackupStatus',
    full_name='Medusa.BackupStatus',
    index=1,
    containing_service=None,
    input_type=_BACKUPSTATUSREQUEST,
    output_type=_BACKUPSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBackup',
    full_name='Medusa.DeleteBackup',
    index=2,
    containing_service=None,
    input_type=_DELETEBACKUPREQUEST,
    output_type=_DELETEBACKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBackups',
    full_name='Medusa.GetBackups',
    index=3,
    containing_service=None,
    input_type=_GETBACKUPSREQUEST,
    output_type=_GETBACKUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReloadConfig',
    full_name='Medusa.ReloadConfig',
    index=4,
    containing_service=None,
    input_type=_RELOADCONFIGREQUEST,
    output_type=_RELOADCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEDUSA)

DESCRIPTOR.services_by_name['Medusa'] = _MEDUSA

# @@protoc_insertion_point(module_scope)
