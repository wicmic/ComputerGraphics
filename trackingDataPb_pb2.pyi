from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class keyPointMSG(_message.Message):
    __slots__ = ("posX", "posY", "score", "type", "absPosX", "absPosY", "absPosZ")
    POSX_FIELD_NUMBER: _ClassVar[int]
    POSY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ABSPOSX_FIELD_NUMBER: _ClassVar[int]
    ABSPOSY_FIELD_NUMBER: _ClassVar[int]
    ABSPOSZ_FIELD_NUMBER: _ClassVar[int]
    posX: float
    posY: float
    score: float
    type: int
    absPosX: float
    absPosY: float
    absPosZ: float
    def __init__(self, posX: _Optional[float] = ..., posY: _Optional[float] = ..., score: _Optional[float] = ..., type: _Optional[int] = ..., absPosX: _Optional[float] = ..., absPosY: _Optional[float] = ..., absPosZ: _Optional[float] = ...) -> None: ...

class poseMSG(_message.Message):
    __slots__ = ("id", "pitchPos", "keyPoints", "activity", "identDesc")
    ID_FIELD_NUMBER: _ClassVar[int]
    PITCHPOS_FIELD_NUMBER: _ClassVar[int]
    KEYPOINTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    IDENTDESC_FIELD_NUMBER: _ClassVar[int]
    id: int
    pitchPos: keyPointMSG
    keyPoints: _containers.RepeatedCompositeFieldContainer[keyPointMSG]
    activity: float
    identDesc: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, id: _Optional[int] = ..., pitchPos: _Optional[_Union[keyPointMSG, _Mapping]] = ..., keyPoints: _Optional[_Iterable[_Union[keyPointMSG, _Mapping]]] = ..., activity: _Optional[float] = ..., identDesc: _Optional[_Iterable[float]] = ...) -> None: ...

class cameraMSG(_message.Message):
    __slots__ = ("hPitch",)
    HPITCH_FIELD_NUMBER: _ClassVar[int]
    hPitch: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, hPitch: _Optional[_Iterable[float]] = ...) -> None: ...

class frameMSG(_message.Message):
    __slots__ = ("index", "ballPos", "poseData", "cameraData")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    BALLPOS_FIELD_NUMBER: _ClassVar[int]
    POSEDATA_FIELD_NUMBER: _ClassVar[int]
    CAMERADATA_FIELD_NUMBER: _ClassVar[int]
    index: int
    ballPos: keyPointMSG
    poseData: _containers.RepeatedCompositeFieldContainer[poseMSG]
    cameraData: cameraMSG
    def __init__(self, index: _Optional[int] = ..., ballPos: _Optional[_Union[keyPointMSG, _Mapping]] = ..., poseData: _Optional[_Iterable[_Union[poseMSG, _Mapping]]] = ..., cameraData: _Optional[_Union[cameraMSG, _Mapping]] = ...) -> None: ...

class videoMetadataMSG(_message.Message):
    __slots__ = ("frameRate", "nFrames", "resX", "resY")
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    NFRAMES_FIELD_NUMBER: _ClassVar[int]
    RESX_FIELD_NUMBER: _ClassVar[int]
    RESY_FIELD_NUMBER: _ClassVar[int]
    frameRate: float
    nFrames: int
    resX: int
    resY: int
    def __init__(self, frameRate: _Optional[float] = ..., nFrames: _Optional[int] = ..., resX: _Optional[int] = ..., resY: _Optional[int] = ...) -> None: ...

class trackingData(_message.Message):
    __slots__ = ("input_video", "frameData", "videoMeta")
    INPUT_VIDEO_FIELD_NUMBER: _ClassVar[int]
    FRAMEDATA_FIELD_NUMBER: _ClassVar[int]
    VIDEOMETA_FIELD_NUMBER: _ClassVar[int]
    input_video: str
    frameData: _containers.RepeatedCompositeFieldContainer[frameMSG]
    videoMeta: videoMetadataMSG
    def __init__(self, input_video: _Optional[str] = ..., frameData: _Optional[_Iterable[_Union[frameMSG, _Mapping]]] = ..., videoMeta: _Optional[_Union[videoMetadataMSG, _Mapping]] = ...) -> None: ...
