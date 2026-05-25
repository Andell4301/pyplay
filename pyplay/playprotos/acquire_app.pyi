from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcquireRequest(_message.Message):
    __slots__ = ("package", "f8", "version", "offer_type", "f15", "nonce", "f25", "m30")
    class Package(_message.Message):
        __slots__ = ("payload", "f2")
        class Payload(_message.Message):
            __slots__ = ("package_name", "f2", "f3")
            PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
            F2_FIELD_NUMBER: _ClassVar[int]
            F3_FIELD_NUMBER: _ClassVar[int]
            package_name: str
            f2: int
            f3: int
            def __init__(self, package_name: _Optional[str] = ..., f2: _Optional[int] = ..., f3: _Optional[int] = ...) -> None: ...
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        F2_FIELD_NUMBER: _ClassVar[int]
        payload: AcquireRequest.Package.Payload
        f2: int
        def __init__(self, payload: _Optional[_Union[AcquireRequest.Package.Payload, _Mapping]] = ..., f2: _Optional[int] = ...) -> None: ...
    class Version(_message.Message):
        __slots__ = ("version_code", "f3")
        VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
        F3_FIELD_NUMBER: _ClassVar[int]
        version_code: int
        f3: int
        def __init__(self, version_code: _Optional[int] = ..., f3: _Optional[int] = ...) -> None: ...
    class Message30(_message.Message):
        __slots__ = ("f1", "f2")
        F1_FIELD_NUMBER: _ClassVar[int]
        F2_FIELD_NUMBER: _ClassVar[int]
        f1: int
        f2: int
        def __init__(self, f1: _Optional[int] = ..., f2: _Optional[int] = ...) -> None: ...
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    F8_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    F15_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    F25_FIELD_NUMBER: _ClassVar[int]
    M30_FIELD_NUMBER: _ClassVar[int]
    package: AcquireRequest.Package
    f8: Field
    version: AcquireRequest.Version
    offer_type: int
    f15: int
    nonce: str
    f25: int
    m30: AcquireRequest.Message30
    def __init__(self, package: _Optional[_Union[AcquireRequest.Package, _Mapping]] = ..., f8: _Optional[_Union[Field, _Mapping]] = ..., version: _Optional[_Union[AcquireRequest.Version, _Mapping]] = ..., offer_type: _Optional[int] = ..., f15: _Optional[int] = ..., nonce: _Optional[str] = ..., f25: _Optional[int] = ..., m30: _Optional[_Union[AcquireRequest.Message30, _Mapping]] = ...) -> None: ...

class AcquireResponseWrapper(_message.Message):
    __slots__ = ("acquire_response",)
    class AcquireResponse(_message.Message):
        __slots__ = ("acquire_payload",)
        class AcquirePayload(_message.Message):
            __slots__ = ("purchase", "package")
            class PurchaseWrapper(_message.Message):
                __slots__ = ("status", "m8", "signature", "response", "game_purchase", "app_purchase")
                class Purchase(_message.Message):
                    __slots__ = ("label", "properties")
                    class Properties(_message.Message):
                        __slots__ = ("entries",)
                        ENTRIES_FIELD_NUMBER: _ClassVar[int]
                        entries: _containers.RepeatedCompositeFieldContainer[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase.Entry]
                        def __init__(self, entries: _Optional[_Iterable[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase.Entry, _Mapping]]] = ...) -> None: ...
                    class Entry(_message.Message):
                        __slots__ = ("key", "bool_value", "int_value")
                        KEY_FIELD_NUMBER: _ClassVar[int]
                        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
                        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
                        key: str
                        bool_value: str
                        int_value: int
                        def __init__(self, key: _Optional[str] = ..., bool_value: _Optional[str] = ..., int_value: _Optional[int] = ...) -> None: ...
                    LABEL_FIELD_NUMBER: _ClassVar[int]
                    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                    label: str
                    properties: AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase.Properties
                    def __init__(self, label: _Optional[str] = ..., properties: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase.Properties, _Mapping]] = ...) -> None: ...
                class Message8(_message.Message):
                    __slots__ = ("some_things",)
                    SOME_THINGS_FIELD_NUMBER: _ClassVar[int]
                    some_things: _containers.RepeatedCompositeFieldContainer[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.SomeThing]
                    def __init__(self, some_things: _Optional[_Iterable[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.SomeThing, _Mapping]]] = ...) -> None: ...
                class SomeThing(_message.Message):
                    __slots__ = ("f1", "f2", "f3", "f4", "f6")
                    F1_FIELD_NUMBER: _ClassVar[int]
                    F2_FIELD_NUMBER: _ClassVar[int]
                    F3_FIELD_NUMBER: _ClassVar[int]
                    F4_FIELD_NUMBER: _ClassVar[int]
                    F6_FIELD_NUMBER: _ClassVar[int]
                    f1: int
                    f2: int
                    f3: Field
                    f4: Field
                    f6: str
                    def __init__(self, f1: _Optional[int] = ..., f2: _Optional[int] = ..., f3: _Optional[_Union[Field, _Mapping]] = ..., f4: _Optional[_Union[Field, _Mapping]] = ..., f6: _Optional[str] = ...) -> None: ...
                STATUS_FIELD_NUMBER: _ClassVar[int]
                M8_FIELD_NUMBER: _ClassVar[int]
                SIGNATURE_FIELD_NUMBER: _ClassVar[int]
                RESPONSE_FIELD_NUMBER: _ClassVar[int]
                GAME_PURCHASE_FIELD_NUMBER: _ClassVar[int]
                APP_PURCHASE_FIELD_NUMBER: _ClassVar[int]
                status: int
                m8: AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Message8
                signature: str
                response: AcquireResponseWrapper.AcquireResponse.Response
                game_purchase: AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase
                app_purchase: AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase
                def __init__(self, status: _Optional[int] = ..., m8: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Message8, _Mapping]] = ..., signature: _Optional[str] = ..., response: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.Response, _Mapping]] = ..., game_purchase: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase, _Mapping]] = ..., app_purchase: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper.Purchase, _Mapping]] = ...) -> None: ...
            class Package(_message.Message):
                __slots__ = ("payload",)
                class OuterPayload(_message.Message):
                    __slots__ = ("app_info", "encoded_payload", "sub_payload")
                    APP_INFO_FIELD_NUMBER: _ClassVar[int]
                    ENCODED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
                    SUB_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
                    app_info: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.AppInfo
                    encoded_payload: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.EncodedPayload
                    sub_payload: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.InnerPayload
                    def __init__(self, app_info: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.AppInfo, _Mapping]] = ..., encoded_payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.EncodedPayload, _Mapping]] = ..., sub_payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.InnerPayload, _Mapping]] = ...) -> None: ...
                class InnerPayload(_message.Message):
                    __slots__ = ("app_info", "encoded_payload", "f5")
                    APP_INFO_FIELD_NUMBER: _ClassVar[int]
                    ENCODED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
                    F5_FIELD_NUMBER: _ClassVar[int]
                    app_info: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.AppInfo
                    encoded_payload: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.EncodedPayload
                    f5: int
                    def __init__(self, app_info: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.AppInfo, _Mapping]] = ..., encoded_payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.EncodedPayload, _Mapping]] = ..., f5: _Optional[int] = ...) -> None: ...
                class AppInfo(_message.Message):
                    __slots__ = ("package_name", "seven")
                    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
                    SEVEN_FIELD_NUMBER: _ClassVar[int]
                    package_name: str
                    seven: int
                    def __init__(self, package_name: _Optional[str] = ..., seven: _Optional[int] = ...) -> None: ...
                class EncodedPayload(_message.Message):
                    __slots__ = ("encoded",)
                    ENCODED_FIELD_NUMBER: _ClassVar[int]
                    encoded: str
                    def __init__(self, encoded: _Optional[str] = ...) -> None: ...
                PAYLOAD_FIELD_NUMBER: _ClassVar[int]
                payload: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.OuterPayload
                def __init__(self, payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package.OuterPayload, _Mapping]] = ...) -> None: ...
            PURCHASE_FIELD_NUMBER: _ClassVar[int]
            PACKAGE_FIELD_NUMBER: _ClassVar[int]
            purchase: AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper
            package: AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package
            def __init__(self, purchase: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.PurchaseWrapper, _Mapping]] = ..., package: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload.Package, _Mapping]] = ...) -> None: ...
        class Response(_message.Message):
            __slots__ = ("status", "payload")
            class Payload(_message.Message):
                __slots__ = ("data",)
                class Data(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: int
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
                DATA_FIELD_NUMBER: _ClassVar[int]
                data: AcquireResponseWrapper.AcquireResponse.Response.Payload.Data
                def __init__(self, data: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.Response.Payload.Data, _Mapping]] = ...) -> None: ...
            STATUS_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            status: int
            payload: AcquireResponseWrapper.AcquireResponse.Response.Payload
            def __init__(self, status: _Optional[int] = ..., payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.Response.Payload, _Mapping]] = ...) -> None: ...
        ACQUIRE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        acquire_payload: AcquireResponseWrapper.AcquireResponse.AcquirePayload
        def __init__(self, acquire_payload: _Optional[_Union[AcquireResponseWrapper.AcquireResponse.AcquirePayload, _Mapping]] = ...) -> None: ...
    ACQUIRE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    acquire_response: AcquireResponseWrapper.AcquireResponse
    def __init__(self, acquire_response: _Optional[_Union[AcquireResponseWrapper.AcquireResponse, _Mapping]] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
