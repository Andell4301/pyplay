from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AndroidAppDeliveryData(_message.Message):
    __slots__ = ("download_size", "sha1", "download_url", "additional_file", "download_auth_cookie", "forward_locked", "refund_timeout", "server_initiated", "post_install_refund_window_millis", "immediate_start_needed", "patch_data", "encryption_params", "compressed_download_url", "compressed_size", "split_delivery_data", "install_location", "type", "compressed_app_data", "sha256", "dex_metadata")
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FILE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_AUTH_COOKIE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_LOCKED_FIELD_NUMBER: _ClassVar[int]
    REFUND_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVER_INITIATED_FIELD_NUMBER: _ClassVar[int]
    POST_INSTALL_REFUND_WINDOW_MILLIS_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_START_NEEDED_FIELD_NUMBER: _ClassVar[int]
    PATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_DELIVERY_DATA_FIELD_NUMBER: _ClassVar[int]
    INSTALL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_APP_DATA_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    DEX_METADATA_FIELD_NUMBER: _ClassVar[int]
    download_size: int
    sha1: str
    download_url: str
    additional_file: _containers.RepeatedCompositeFieldContainer[AppFileMetadata]
    download_auth_cookie: _containers.RepeatedCompositeFieldContainer[HttpCookie]
    forward_locked: bool
    refund_timeout: int
    server_initiated: bool
    post_install_refund_window_millis: int
    immediate_start_needed: bool
    patch_data: AndroidAppPatchData
    encryption_params: EncryptionParams
    compressed_download_url: str
    compressed_size: int
    split_delivery_data: _containers.RepeatedCompositeFieldContainer[SplitDeliveryData]
    install_location: int
    type: int
    compressed_app_data: CompressedAppData
    sha256: str
    dex_metadata: DexMetadata
    def __init__(self, download_size: _Optional[int] = ..., sha1: _Optional[str] = ..., download_url: _Optional[str] = ..., additional_file: _Optional[_Iterable[_Union[AppFileMetadata, _Mapping]]] = ..., download_auth_cookie: _Optional[_Iterable[_Union[HttpCookie, _Mapping]]] = ..., forward_locked: _Optional[bool] = ..., refund_timeout: _Optional[int] = ..., server_initiated: _Optional[bool] = ..., post_install_refund_window_millis: _Optional[int] = ..., immediate_start_needed: _Optional[bool] = ..., patch_data: _Optional[_Union[AndroidAppPatchData, _Mapping]] = ..., encryption_params: _Optional[_Union[EncryptionParams, _Mapping]] = ..., compressed_download_url: _Optional[str] = ..., compressed_size: _Optional[int] = ..., split_delivery_data: _Optional[_Iterable[_Union[SplitDeliveryData, _Mapping]]] = ..., install_location: _Optional[int] = ..., type: _Optional[int] = ..., compressed_app_data: _Optional[_Union[CompressedAppData, _Mapping]] = ..., sha256: _Optional[str] = ..., dex_metadata: _Optional[_Union[DexMetadata, _Mapping]] = ...) -> None: ...

class DexMetadata(_message.Message):
    __slots__ = ("download_size", "sha256", "download_url")
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_size: int
    sha256: str
    download_url: str
    def __init__(self, download_size: _Optional[int] = ..., sha256: _Optional[str] = ..., download_url: _Optional[str] = ...) -> None: ...

class SplitDeliveryData(_message.Message):
    __slots__ = ("name", "download_size", "compressed_size", "sha1", "download_url", "compressed_download_url", "patch_data", "compressed_app_data", "sha256")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    PATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_APP_DATA_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    name: str
    download_size: int
    compressed_size: int
    sha1: str
    download_url: str
    compressed_download_url: str
    patch_data: AndroidAppPatchData
    compressed_app_data: CompressedAppData
    sha256: str
    def __init__(self, name: _Optional[str] = ..., download_size: _Optional[int] = ..., compressed_size: _Optional[int] = ..., sha1: _Optional[str] = ..., download_url: _Optional[str] = ..., compressed_download_url: _Optional[str] = ..., patch_data: _Optional[_Union[AndroidAppPatchData, _Mapping]] = ..., compressed_app_data: _Optional[_Union[CompressedAppData, _Mapping]] = ..., sha256: _Optional[str] = ...) -> None: ...

class AndroidAppPatchData(_message.Message):
    __slots__ = ("base_version_code", "base_sha1", "download_url", "patch_format", "max_patch_size")
    BASE_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    BASE_SHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    PATCH_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_PATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    base_version_code: int
    base_sha1: str
    download_url: str
    patch_format: int
    max_patch_size: int
    def __init__(self, base_version_code: _Optional[int] = ..., base_sha1: _Optional[str] = ..., download_url: _Optional[str] = ..., patch_format: _Optional[int] = ..., max_patch_size: _Optional[int] = ...) -> None: ...

class CompressedAppData(_message.Message):
    __slots__ = ("type", "size", "download_url")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    type: int
    size: int
    download_url: str
    def __init__(self, type: _Optional[int] = ..., size: _Optional[int] = ..., download_url: _Optional[str] = ...) -> None: ...

class AppFileMetadata(_message.Message):
    __slots__ = ("file_type", "version_code", "download_size", "download_url", "patch_data", "compressed_size", "compressed_download_url", "sha1")
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    PATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    file_type: int
    version_code: int
    download_size: int
    download_url: str
    patch_data: AndroidAppPatchData
    compressed_size: int
    compressed_download_url: str
    sha1: str
    def __init__(self, file_type: _Optional[int] = ..., version_code: _Optional[int] = ..., download_size: _Optional[int] = ..., download_url: _Optional[str] = ..., patch_data: _Optional[_Union[AndroidAppPatchData, _Mapping]] = ..., compressed_size: _Optional[int] = ..., compressed_download_url: _Optional[str] = ..., sha1: _Optional[str] = ...) -> None: ...

class EncryptionParams(_message.Message):
    __slots__ = ("version", "encryption_key", "hmac_key")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    HMAC_KEY_FIELD_NUMBER: _ClassVar[int]
    version: int
    encryption_key: str
    hmac_key: str
    def __init__(self, version: _Optional[int] = ..., encryption_key: _Optional[str] = ..., hmac_key: _Optional[str] = ...) -> None: ...

class HttpCookie(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("name", "address_line1", "address_line2", "city", "state", "postal_code", "postal_country", "dependent_locality", "sorting_code", "language_code", "phone_number", "deprecated_is_reduced", "first_name", "last_name", "email")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_LOCALITY_FIELD_NUMBER: _ClassVar[int]
    SORTING_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_IS_REDUCED_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    address_line1: str
    address_line2: str
    city: str
    state: str
    postal_code: str
    postal_country: str
    dependent_locality: str
    sorting_code: str
    language_code: str
    phone_number: str
    deprecated_is_reduced: bool
    first_name: str
    last_name: str
    email: str
    def __init__(self, name: _Optional[str] = ..., address_line1: _Optional[str] = ..., address_line2: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., postal_code: _Optional[str] = ..., postal_country: _Optional[str] = ..., dependent_locality: _Optional[str] = ..., sorting_code: _Optional[str] = ..., language_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., deprecated_is_reduced: _Optional[bool] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class BrowseLink(_message.Message):
    __slots__ = ("name", "data_url", "server_logs_cookie", "icon")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_URL_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_url: str
    server_logs_cookie: bytes
    icon: Image
    def __init__(self, name: _Optional[str] = ..., data_url: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ..., icon: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class BrowseResponse(_message.Message):
    __slots__ = ("contents_url", "promo_url", "category", "breadcrumb", "quick_link", "server_logs_cookie", "title", "backend_id", "browse_tab", "landing_tab_index", "quick_link_tab_index", "quick_link_fallback_tab_index", "is_family_safe", "share_url")
    CONTENTS_URL_FIELD_NUMBER: _ClassVar[int]
    PROMO_URL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB_FIELD_NUMBER: _ClassVar[int]
    QUICK_LINK_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ID_FIELD_NUMBER: _ClassVar[int]
    BROWSE_TAB_FIELD_NUMBER: _ClassVar[int]
    LANDING_TAB_INDEX_FIELD_NUMBER: _ClassVar[int]
    QUICK_LINK_TAB_INDEX_FIELD_NUMBER: _ClassVar[int]
    QUICK_LINK_FALLBACK_TAB_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_FAMILY_SAFE_FIELD_NUMBER: _ClassVar[int]
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    contents_url: str
    promo_url: str
    category: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    breadcrumb: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    quick_link: _containers.RepeatedCompositeFieldContainer[QuickLink]
    server_logs_cookie: bytes
    title: str
    backend_id: int
    browse_tab: BrowseTab
    landing_tab_index: int
    quick_link_tab_index: int
    quick_link_fallback_tab_index: int
    is_family_safe: bool
    share_url: str
    def __init__(self, contents_url: _Optional[str] = ..., promo_url: _Optional[str] = ..., category: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ..., breadcrumb: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ..., quick_link: _Optional[_Iterable[_Union[QuickLink, _Mapping]]] = ..., server_logs_cookie: _Optional[bytes] = ..., title: _Optional[str] = ..., backend_id: _Optional[int] = ..., browse_tab: _Optional[_Union[BrowseTab, _Mapping]] = ..., landing_tab_index: _Optional[int] = ..., quick_link_tab_index: _Optional[int] = ..., quick_link_fallback_tab_index: _Optional[int] = ..., is_family_safe: _Optional[bool] = ..., share_url: _Optional[str] = ...) -> None: ...

class DirectPurchase(_message.Message):
    __slots__ = ("details_url", "purchase_item_id", "parent_item_id", "offer_type")
    DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    details_url: str
    purchase_item_id: str
    parent_item_id: str
    offer_type: int
    def __init__(self, details_url: _Optional[str] = ..., purchase_item_id: _Optional[str] = ..., parent_item_id: _Optional[str] = ..., offer_type: _Optional[int] = ...) -> None: ...

class RedeemGiftCard(_message.Message):
    __slots__ = ("prefill_code", "partner_payload")
    PREFILL_CODE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    prefill_code: str
    partner_payload: str
    def __init__(self, prefill_code: _Optional[str] = ..., partner_payload: _Optional[str] = ...) -> None: ...

class ResolvedLink(_message.Message):
    __slots__ = ("details_url", "browse_url", "search_url", "direct_purchase", "home_url", "redeem_gift_card", "server_logs_cookie", "doc_id", "wishlist_url", "backend", "query", "my_account_url", "help_center")
    DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    BROWSE_URL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_URL_FIELD_NUMBER: _ClassVar[int]
    DIRECT_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    REDEEM_GIFT_CARD_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    WISHLIST_URL_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MY_ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    HELP_CENTER_FIELD_NUMBER: _ClassVar[int]
    details_url: str
    browse_url: str
    search_url: str
    direct_purchase: DirectPurchase
    home_url: str
    redeem_gift_card: RedeemGiftCard
    server_logs_cookie: bytes
    doc_id: DocId
    wishlist_url: str
    backend: int
    query: str
    my_account_url: str
    help_center: HelpCenter
    def __init__(self, details_url: _Optional[str] = ..., browse_url: _Optional[str] = ..., search_url: _Optional[str] = ..., direct_purchase: _Optional[_Union[DirectPurchase, _Mapping]] = ..., home_url: _Optional[str] = ..., redeem_gift_card: _Optional[_Union[RedeemGiftCard, _Mapping]] = ..., server_logs_cookie: _Optional[bytes] = ..., doc_id: _Optional[_Union[DocId, _Mapping]] = ..., wishlist_url: _Optional[str] = ..., backend: _Optional[int] = ..., query: _Optional[str] = ..., my_account_url: _Optional[str] = ..., help_center: _Optional[_Union[HelpCenter, _Mapping]] = ...) -> None: ...

class HelpCenter(_message.Message):
    __slots__ = ("context_id",)
    CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    context_id: str
    def __init__(self, context_id: _Optional[str] = ...) -> None: ...

class QuickLink(_message.Message):
    __slots__ = ("name", "image", "link", "display_required", "server_logs_cookie", "backend_id", "prism_style")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ID_FIELD_NUMBER: _ClassVar[int]
    PRISM_STYLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    image: Image
    link: ResolvedLink
    display_required: bool
    server_logs_cookie: bytes
    backend_id: int
    prism_style: bool
    def __init__(self, name: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., link: _Optional[_Union[ResolvedLink, _Mapping]] = ..., display_required: _Optional[bool] = ..., server_logs_cookie: _Optional[bytes] = ..., backend_id: _Optional[int] = ..., prism_style: _Optional[bool] = ...) -> None: ...

class BrowseTab(_message.Message):
    __slots__ = ("title", "server_logs_cookie", "list_url", "browse_link", "quick_link", "quick_link_title", "categories_title", "backend_id", "highlights_banner_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LIST_URL_FIELD_NUMBER: _ClassVar[int]
    BROWSE_LINK_FIELD_NUMBER: _ClassVar[int]
    QUICK_LINK_FIELD_NUMBER: _ClassVar[int]
    QUICK_LINK_TITLE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_TITLE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ID_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTS_BANNER_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    server_logs_cookie: bytes
    list_url: str
    browse_link: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    quick_link: _containers.RepeatedCompositeFieldContainer[QuickLink]
    quick_link_title: str
    categories_title: str
    backend_id: int
    highlights_banner_url: str
    def __init__(self, title: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ..., list_url: _Optional[str] = ..., browse_link: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ..., quick_link: _Optional[_Iterable[_Union[QuickLink, _Mapping]]] = ..., quick_link_title: _Optional[str] = ..., categories_title: _Optional[str] = ..., backend_id: _Optional[int] = ..., highlights_banner_url: _Optional[str] = ...) -> None: ...

class BuyResponse(_message.Message):
    __slots__ = ("purchase_response", "checkoutinfo", "continue_via_url", "purchase_status_url", "checkout_service_id", "checkout_token_required", "base_checkout_url", "tos_checkbox_html", "iab_permission_error", "purchase_status_response", "purchase_cookie", "challenge", "add_instrument_prompt_html", "confirm_button_text", "permission_error_title_text", "permission_error_message_text", "server_logs_cookie", "encoded_delivery_token", "unknown_token")
    class CheckoutInfo(_message.Message):
        __slots__ = ("item", "sub_item", "checkoutoption", "deprecated_checkout_url", "add_instrument_url", "footer_html", "eligible_instrument_family", "footnote_html", "eligible_instrument")
        class CheckoutOption(_message.Message):
            __slots__ = ("form_of_payment", "encoded_adjusted_cart", "instrument_id", "item", "sub_item", "total", "footer_html", "instrument_family", "deprecated_instrument_inapplicable_reason", "selected_instrument", "summary", "footnote_html", "instrument", "purchase_cookie", "disabled_reason")
            FORM_OF_PAYMENT_FIELD_NUMBER: _ClassVar[int]
            ENCODED_ADJUSTED_CART_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
            ITEM_FIELD_NUMBER: _ClassVar[int]
            SUB_ITEM_FIELD_NUMBER: _ClassVar[int]
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            FOOTER_HTML_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENT_FAMILY_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_INSTRUMENT_INAPPLICABLE_REASON_FIELD_NUMBER: _ClassVar[int]
            SELECTED_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
            SUMMARY_FIELD_NUMBER: _ClassVar[int]
            FOOTNOTE_HTML_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
            PURCHASE_COOKIE_FIELD_NUMBER: _ClassVar[int]
            DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
            form_of_payment: str
            encoded_adjusted_cart: str
            instrument_id: str
            item: _containers.RepeatedCompositeFieldContainer[LineItem]
            sub_item: _containers.RepeatedCompositeFieldContainer[LineItem]
            total: LineItem
            footer_html: _containers.RepeatedScalarFieldContainer[str]
            instrument_family: int
            deprecated_instrument_inapplicable_reason: _containers.RepeatedScalarFieldContainer[int]
            selected_instrument: bool
            summary: LineItem
            footnote_html: _containers.RepeatedScalarFieldContainer[str]
            instrument: Instrument
            purchase_cookie: str
            disabled_reason: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, form_of_payment: _Optional[str] = ..., encoded_adjusted_cart: _Optional[str] = ..., instrument_id: _Optional[str] = ..., item: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., sub_item: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., total: _Optional[_Union[LineItem, _Mapping]] = ..., footer_html: _Optional[_Iterable[str]] = ..., instrument_family: _Optional[int] = ..., deprecated_instrument_inapplicable_reason: _Optional[_Iterable[int]] = ..., selected_instrument: _Optional[bool] = ..., summary: _Optional[_Union[LineItem, _Mapping]] = ..., footnote_html: _Optional[_Iterable[str]] = ..., instrument: _Optional[_Union[Instrument, _Mapping]] = ..., purchase_cookie: _Optional[str] = ..., disabled_reason: _Optional[_Iterable[str]] = ...) -> None: ...
        ITEM_FIELD_NUMBER: _ClassVar[int]
        SUB_ITEM_FIELD_NUMBER: _ClassVar[int]
        CHECKOUTOPTION_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
        ADD_INSTRUMENT_URL_FIELD_NUMBER: _ClassVar[int]
        FOOTER_HTML_FIELD_NUMBER: _ClassVar[int]
        ELIGIBLE_INSTRUMENT_FAMILY_FIELD_NUMBER: _ClassVar[int]
        FOOTNOTE_HTML_FIELD_NUMBER: _ClassVar[int]
        ELIGIBLE_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        item: LineItem
        sub_item: _containers.RepeatedCompositeFieldContainer[LineItem]
        checkoutoption: _containers.RepeatedCompositeFieldContainer[BuyResponse.CheckoutInfo.CheckoutOption]
        deprecated_checkout_url: str
        add_instrument_url: str
        footer_html: _containers.RepeatedScalarFieldContainer[str]
        eligible_instrument_family: _containers.RepeatedScalarFieldContainer[int]
        footnote_html: _containers.RepeatedScalarFieldContainer[str]
        eligible_instrument: _containers.RepeatedCompositeFieldContainer[Instrument]
        def __init__(self, item: _Optional[_Union[LineItem, _Mapping]] = ..., sub_item: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., checkoutoption: _Optional[_Iterable[_Union[BuyResponse.CheckoutInfo.CheckoutOption, _Mapping]]] = ..., deprecated_checkout_url: _Optional[str] = ..., add_instrument_url: _Optional[str] = ..., footer_html: _Optional[_Iterable[str]] = ..., eligible_instrument_family: _Optional[_Iterable[int]] = ..., footnote_html: _Optional[_Iterable[str]] = ..., eligible_instrument: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ...) -> None: ...
    PURCHASE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTINFO_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_VIA_URL_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    BASE_CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    TOS_CHECKBOX_HTML_FIELD_NUMBER: _ClassVar[int]
    IAB_PERMISSION_ERROR_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    ADD_INSTRUMENT_PROMPT_HTML_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ERROR_TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ERROR_MESSAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DELIVERY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    purchase_response: PurchaseNotificationResponse
    checkoutinfo: BuyResponse.CheckoutInfo
    continue_via_url: str
    purchase_status_url: str
    checkout_service_id: str
    checkout_token_required: bool
    base_checkout_url: str
    tos_checkbox_html: _containers.RepeatedScalarFieldContainer[str]
    iab_permission_error: int
    purchase_status_response: PurchaseStatusResponse
    purchase_cookie: str
    challenge: Challenge
    add_instrument_prompt_html: str
    confirm_button_text: str
    permission_error_title_text: str
    permission_error_message_text: str
    server_logs_cookie: bytes
    encoded_delivery_token: str
    unknown_token: str
    def __init__(self, purchase_response: _Optional[_Union[PurchaseNotificationResponse, _Mapping]] = ..., checkoutinfo: _Optional[_Union[BuyResponse.CheckoutInfo, _Mapping]] = ..., continue_via_url: _Optional[str] = ..., purchase_status_url: _Optional[str] = ..., checkout_service_id: _Optional[str] = ..., checkout_token_required: _Optional[bool] = ..., base_checkout_url: _Optional[str] = ..., tos_checkbox_html: _Optional[_Iterable[str]] = ..., iab_permission_error: _Optional[int] = ..., purchase_status_response: _Optional[_Union[PurchaseStatusResponse, _Mapping]] = ..., purchase_cookie: _Optional[str] = ..., challenge: _Optional[_Union[Challenge, _Mapping]] = ..., add_instrument_prompt_html: _Optional[str] = ..., confirm_button_text: _Optional[str] = ..., permission_error_title_text: _Optional[str] = ..., permission_error_message_text: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ..., encoded_delivery_token: _Optional[str] = ..., unknown_token: _Optional[str] = ...) -> None: ...

class LineItem(_message.Message):
    __slots__ = ("name", "description", "offer", "amount")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    offer: Offer
    amount: Money
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., offer: _Optional[_Union[Offer, _Mapping]] = ..., amount: _Optional[_Union[Money, _Mapping]] = ...) -> None: ...

class Money(_message.Message):
    __slots__ = ("micros", "currency_code", "formatted_amount")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    micros: int
    currency_code: str
    formatted_amount: str
    def __init__(self, micros: _Optional[int] = ..., currency_code: _Optional[str] = ..., formatted_amount: _Optional[str] = ...) -> None: ...

class PurchaseNotificationResponse(_message.Message):
    __slots__ = ("status", "debug_info", "localized_error_message", "purchase_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    debug_info: DebugInfo
    localized_error_message: str
    purchase_id: str
    def __init__(self, status: _Optional[int] = ..., debug_info: _Optional[_Union[DebugInfo, _Mapping]] = ..., localized_error_message: _Optional[str] = ..., purchase_id: _Optional[str] = ...) -> None: ...

class PurchaseStatusResponse(_message.Message):
    __slots__ = ("status", "status_msg", "status_title", "brief_message", "info_url", "library_update", "rejected_instrument", "app_delivery_data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_TITLE_FIELD_NUMBER: _ClassVar[int]
    BRIEF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INFO_URL_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    REJECTED_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    APP_DELIVERY_DATA_FIELD_NUMBER: _ClassVar[int]
    status: int
    status_msg: str
    status_title: str
    brief_message: str
    info_url: str
    library_update: LibraryUpdate
    rejected_instrument: Instrument
    app_delivery_data: AndroidAppDeliveryData
    def __init__(self, status: _Optional[int] = ..., status_msg: _Optional[str] = ..., status_title: _Optional[str] = ..., brief_message: _Optional[str] = ..., info_url: _Optional[str] = ..., library_update: _Optional[_Union[LibraryUpdate, _Mapping]] = ..., rejected_instrument: _Optional[_Union[Instrument, _Mapping]] = ..., app_delivery_data: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ...) -> None: ...

class PurchaseHistoryDetails(_message.Message):
    __slots__ = ("purchase_timestamp_millis", "purchase_details_html", "offer", "purchase_status", "title_byline_html", "client_refund_context", "purchase_details_image")
    PURCHASE_TIMESTAMP_MILLIS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DETAILS_HTML_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_BYLINE_HTML_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REFUND_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DETAILS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    purchase_timestamp_millis: int
    purchase_details_html: str
    offer: Offer
    purchase_status: str
    title_byline_html: str
    client_refund_context: bytes
    purchase_details_image: Image
    def __init__(self, purchase_timestamp_millis: _Optional[int] = ..., purchase_details_html: _Optional[str] = ..., offer: _Optional[_Union[Offer, _Mapping]] = ..., purchase_status: _Optional[str] = ..., title_byline_html: _Optional[str] = ..., client_refund_context: _Optional[bytes] = ..., purchase_details_image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class BillingProfileResponse(_message.Message):
    __slots__ = ("result", "billing_profile", "user_message_html")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    BILLING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_HTML_FIELD_NUMBER: _ClassVar[int]
    result: int
    billing_profile: BillingProfile
    user_message_html: str
    def __init__(self, result: _Optional[int] = ..., billing_profile: _Optional[_Union[BillingProfile, _Mapping]] = ..., user_message_html: _Optional[str] = ...) -> None: ...

class CheckInstrumentResponse(_message.Message):
    __slots__ = ("user_has_valid_instrument", "checkout_token_required", "instrument", "eligible_instrument")
    USER_HAS_VALID_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    user_has_valid_instrument: bool
    checkout_token_required: bool
    instrument: _containers.RepeatedCompositeFieldContainer[Instrument]
    eligible_instrument: _containers.RepeatedCompositeFieldContainer[Instrument]
    def __init__(self, user_has_valid_instrument: _Optional[bool] = ..., checkout_token_required: _Optional[bool] = ..., instrument: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ..., eligible_instrument: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ...) -> None: ...

class InstrumentSetupInfoResponse(_message.Message):
    __slots__ = ("setup_info", "checkout_token_required")
    SETUP_INFO_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    setup_info: _containers.RepeatedCompositeFieldContainer[InstrumentSetupInfo]
    checkout_token_required: bool
    def __init__(self, setup_info: _Optional[_Iterable[_Union[InstrumentSetupInfo, _Mapping]]] = ..., checkout_token_required: _Optional[bool] = ...) -> None: ...

class RedeemGiftCardRequest(_message.Message):
    __slots__ = ("gift_card_pin", "address", "accepted_legal_document_id", "checkout_token")
    GIFT_CARD_PIN_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_LEGAL_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gift_card_pin: str
    address: Address
    accepted_legal_document_id: _containers.RepeatedScalarFieldContainer[str]
    checkout_token: str
    def __init__(self, gift_card_pin: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., accepted_legal_document_id: _Optional[_Iterable[str]] = ..., checkout_token: _Optional[str] = ...) -> None: ...

class RedeemGiftCardResponse(_message.Message):
    __slots__ = ("result", "user_message_html", "balance_html", "address_challenge", "checkout_token_required")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_HTML_FIELD_NUMBER: _ClassVar[int]
    BALANCE_HTML_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    result: int
    user_message_html: str
    balance_html: str
    address_challenge: AddressChallenge
    checkout_token_required: bool
    def __init__(self, result: _Optional[int] = ..., user_message_html: _Optional[str] = ..., balance_html: _Optional[str] = ..., address_challenge: _Optional[_Union[AddressChallenge, _Mapping]] = ..., checkout_token_required: _Optional[bool] = ...) -> None: ...

class UpdateInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "checkout_token")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instrument: Instrument
    checkout_token: str
    def __init__(self, instrument: _Optional[_Union[Instrument, _Mapping]] = ..., checkout_token: _Optional[str] = ...) -> None: ...

class UpdateInstrumentResponse(_message.Message):
    __slots__ = ("result", "instrument_id", "user_message_html", "error_input_field", "checkout_token_required", "redeemed_offer")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_HTML_FIELD_NUMBER: _ClassVar[int]
    ERROR_INPUT_FIELD_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    REDEEMED_OFFER_FIELD_NUMBER: _ClassVar[int]
    result: int
    instrument_id: str
    user_message_html: str
    error_input_field: _containers.RepeatedCompositeFieldContainer[InputValidationError]
    checkout_token_required: bool
    redeemed_offer: RedeemedPromoOffer
    def __init__(self, result: _Optional[int] = ..., instrument_id: _Optional[str] = ..., user_message_html: _Optional[str] = ..., error_input_field: _Optional[_Iterable[_Union[InputValidationError, _Mapping]]] = ..., checkout_token_required: _Optional[bool] = ..., redeemed_offer: _Optional[_Union[RedeemedPromoOffer, _Mapping]] = ...) -> None: ...

class InitiateAssociationResponse(_message.Message):
    __slots__ = ("user_token",)
    USER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_token: str
    def __init__(self, user_token: _Optional[str] = ...) -> None: ...

class VerifyAssociationResponse(_message.Message):
    __slots__ = ("status", "billing_address", "carrier_tos", "carrier_error_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CARRIER_TOS_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    billing_address: Address
    carrier_tos: CarrierTos
    carrier_error_message: str
    def __init__(self, status: _Optional[int] = ..., billing_address: _Optional[_Union[Address, _Mapping]] = ..., carrier_tos: _Optional[_Union[CarrierTos, _Mapping]] = ..., carrier_error_message: _Optional[str] = ...) -> None: ...

class AddressChallenge(_message.Message):
    __slots__ = ("response_address_param", "response_checkboxes_param", "title", "description_html", "checkbox", "address", "error_input_field", "error_html", "required_field", "supported_country")
    RESPONSE_ADDRESS_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CHECKBOXES_PARAM_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_INPUT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ERROR_HTML_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    response_address_param: str
    response_checkboxes_param: str
    title: str
    description_html: str
    checkbox: _containers.RepeatedCompositeFieldContainer[FormCheckbox]
    address: Address
    error_input_field: _containers.RepeatedCompositeFieldContainer[InputValidationError]
    error_html: str
    required_field: _containers.RepeatedScalarFieldContainer[int]
    supported_country: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(self, response_address_param: _Optional[str] = ..., response_checkboxes_param: _Optional[str] = ..., title: _Optional[str] = ..., description_html: _Optional[str] = ..., checkbox: _Optional[_Iterable[_Union[FormCheckbox, _Mapping]]] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., error_input_field: _Optional[_Iterable[_Union[InputValidationError, _Mapping]]] = ..., error_html: _Optional[str] = ..., required_field: _Optional[_Iterable[int]] = ..., supported_country: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...) -> None: ...

class AuthenticationChallenge(_message.Message):
    __slots__ = ("authentication_type", "response_authentication_type_param", "response_retry_count_param", "pin_header_text", "pin_description_text_html", "gaia_header_text", "gaia_description_text_html", "gaia_footer_text_html", "gaia_opt_out_checkbox", "gaia_opt_out_description_text_html")
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_AUTHENTICATION_TYPE_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_RETRY_COUNT_PARAM_FIELD_NUMBER: _ClassVar[int]
    PIN_HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    PIN_DESCRIPTION_TEXT_HTML_FIELD_NUMBER: _ClassVar[int]
    GAIA_HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    GAIA_DESCRIPTION_TEXT_HTML_FIELD_NUMBER: _ClassVar[int]
    GAIA_FOOTER_TEXT_HTML_FIELD_NUMBER: _ClassVar[int]
    GAIA_OPT_OUT_CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    GAIA_OPT_OUT_DESCRIPTION_TEXT_HTML_FIELD_NUMBER: _ClassVar[int]
    authentication_type: int
    response_authentication_type_param: str
    response_retry_count_param: str
    pin_header_text: str
    pin_description_text_html: str
    gaia_header_text: str
    gaia_description_text_html: str
    gaia_footer_text_html: str
    gaia_opt_out_checkbox: FormCheckbox
    gaia_opt_out_description_text_html: str
    def __init__(self, authentication_type: _Optional[int] = ..., response_authentication_type_param: _Optional[str] = ..., response_retry_count_param: _Optional[str] = ..., pin_header_text: _Optional[str] = ..., pin_description_text_html: _Optional[str] = ..., gaia_header_text: _Optional[str] = ..., gaia_description_text_html: _Optional[str] = ..., gaia_footer_text_html: _Optional[str] = ..., gaia_opt_out_checkbox: _Optional[_Union[FormCheckbox, _Mapping]] = ..., gaia_opt_out_description_text_html: _Optional[str] = ...) -> None: ...

class Challenge(_message.Message):
    __slots__ = ("address_challenge", "authentication_challenge", "web_view_challenge")
    ADDRESS_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    WEB_VIEW_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    address_challenge: AddressChallenge
    authentication_challenge: AuthenticationChallenge
    web_view_challenge: WebViewChallenge
    def __init__(self, address_challenge: _Optional[_Union[AddressChallenge, _Mapping]] = ..., authentication_challenge: _Optional[_Union[AuthenticationChallenge, _Mapping]] = ..., web_view_challenge: _Optional[_Union[WebViewChallenge, _Mapping]] = ...) -> None: ...

class Country(_message.Message):
    __slots__ = ("region_code", "display_name")
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    region_code: str
    display_name: str
    def __init__(self, region_code: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class FormCheckbox(_message.Message):
    __slots__ = ("description", "checked", "required", "id")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    checked: bool
    required: bool
    id: str
    def __init__(self, description: _Optional[str] = ..., checked: _Optional[bool] = ..., required: _Optional[bool] = ..., id: _Optional[str] = ...) -> None: ...

class InputValidationError(_message.Message):
    __slots__ = ("input_field", "error_message")
    INPUT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    input_field: int
    error_message: str
    def __init__(self, input_field: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class WebViewChallenge(_message.Message):
    __slots__ = ("start_url", "target_url_regexp", "cancel_button_display_label", "response_target_url_param", "cancel_url_regexp", "title")
    START_URL_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_REGEXP_FIELD_NUMBER: _ClassVar[int]
    CANCEL_BUTTON_DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TARGET_URL_PARAM_FIELD_NUMBER: _ClassVar[int]
    CANCEL_URL_REGEXP_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    start_url: str
    target_url_regexp: str
    cancel_button_display_label: str
    response_target_url_param: str
    cancel_url_regexp: str
    title: str
    def __init__(self, start_url: _Optional[str] = ..., target_url_regexp: _Optional[str] = ..., cancel_button_display_label: _Optional[str] = ..., response_target_url_param: _Optional[str] = ..., cancel_url_regexp: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class AddCreditCardPromoOffer(_message.Message):
    __slots__ = ("header_text", "description_html", "image", "introductory_text_html", "offer_title", "no_action_description", "terms_and_conditions_html")
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    INTRODUCTORY_TEXT_HTML_FIELD_NUMBER: _ClassVar[int]
    OFFER_TITLE_FIELD_NUMBER: _ClassVar[int]
    NO_ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TERMS_AND_CONDITIONS_HTML_FIELD_NUMBER: _ClassVar[int]
    header_text: str
    description_html: str
    image: Image
    introductory_text_html: str
    offer_title: str
    no_action_description: str
    terms_and_conditions_html: str
    def __init__(self, header_text: _Optional[str] = ..., description_html: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., introductory_text_html: _Optional[str] = ..., offer_title: _Optional[str] = ..., no_action_description: _Optional[str] = ..., terms_and_conditions_html: _Optional[str] = ...) -> None: ...

class AvailablePromoOffer(_message.Message):
    __slots__ = ("add_credit_card_offer",)
    ADD_CREDIT_CARD_OFFER_FIELD_NUMBER: _ClassVar[int]
    add_credit_card_offer: AddCreditCardPromoOffer
    def __init__(self, add_credit_card_offer: _Optional[_Union[AddCreditCardPromoOffer, _Mapping]] = ...) -> None: ...

class CheckPromoOfferResponse(_message.Message):
    __slots__ = ("available_offer", "redeemed_offer", "checkout_token_required")
    AVAILABLE_OFFER_FIELD_NUMBER: _ClassVar[int]
    REDEEMED_OFFER_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_TOKEN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    available_offer: _containers.RepeatedCompositeFieldContainer[AvailablePromoOffer]
    redeemed_offer: RedeemedPromoOffer
    checkout_token_required: bool
    def __init__(self, available_offer: _Optional[_Iterable[_Union[AvailablePromoOffer, _Mapping]]] = ..., redeemed_offer: _Optional[_Union[RedeemedPromoOffer, _Mapping]] = ..., checkout_token_required: _Optional[bool] = ...) -> None: ...

class RedeemedPromoOffer(_message.Message):
    __slots__ = ("header_text", "description_html", "image")
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    header_text: str
    description_html: str
    image: Image
    def __init__(self, header_text: _Optional[str] = ..., description_html: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class DocId(_message.Message):
    __slots__ = ("backend_doc_id", "type", "backend")
    BACKEND_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    backend_doc_id: str
    type: int
    backend: int
    def __init__(self, backend_doc_id: _Optional[str] = ..., type: _Optional[int] = ..., backend: _Optional[int] = ...) -> None: ...

class Install(_message.Message):
    __slots__ = ("android_id", "version", "bundled", "pending", "last_updated")
    ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUNDLED_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    android_id: int
    version: int
    bundled: bool
    pending: bool
    last_updated: int
    def __init__(self, android_id: _Optional[int] = ..., version: _Optional[int] = ..., bundled: _Optional[bool] = ..., pending: _Optional[bool] = ..., last_updated: _Optional[int] = ...) -> None: ...

class GroupLicenseKey(_message.Message):
    __slots__ = ("dasher_customer_id", "doc_id", "licensed_offer_type", "type", "rental_period_days")
    DASHER_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    LICENSED_OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RENTAL_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    dasher_customer_id: int
    doc_id: DocId
    licensed_offer_type: int
    type: int
    rental_period_days: int
    def __init__(self, dasher_customer_id: _Optional[int] = ..., doc_id: _Optional[_Union[DocId, _Mapping]] = ..., licensed_offer_type: _Optional[int] = ..., type: _Optional[int] = ..., rental_period_days: _Optional[int] = ...) -> None: ...

class LicenseTerms(_message.Message):
    __slots__ = ("group_license_key",)
    GROUP_LICENSE_KEY_FIELD_NUMBER: _ClassVar[int]
    group_license_key: GroupLicenseKey
    def __init__(self, group_license_key: _Optional[_Union[GroupLicenseKey, _Mapping]] = ...) -> None: ...

class Offer(_message.Message):
    __slots__ = ("micros", "currency_code", "formatted_amount", "converted_price", "checkout_flow_required", "full_price_micros", "formatted_full_amount", "offer_type", "rental_terms", "on_sale_date", "promotion_label", "subscription_terms", "formatted_name", "formatted_description", "preorder", "on_sale_date_display_time_zone_offset_millis", "licensed_offer_type", "subscription_content_terms", "offer_id", "preorder_fulfillment_display_date", "license_terms", "sale", "voucher_terms", "offer_payment", "repeat_last_payment", "buy_button_label", "instant_purchase_enabled", "sale_end_timestamp", "sale_message")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_FLOW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    FULL_PRICE_MICROS_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_FULL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    RENTAL_TERMS_FIELD_NUMBER: _ClassVar[int]
    ON_SALE_DATE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TERMS_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PREORDER_FIELD_NUMBER: _ClassVar[int]
    ON_SALE_DATE_DISPLAY_TIME_ZONE_OFFSET_MILLIS_FIELD_NUMBER: _ClassVar[int]
    LICENSED_OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_CONTENT_TERMS_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PREORDER_FULFILLMENT_DISPLAY_DATE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TERMS_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    VOUCHER_TERMS_FIELD_NUMBER: _ClassVar[int]
    OFFER_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    REPEAT_LAST_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    BUY_BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    INSTANT_PURCHASE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SALE_END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SALE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    micros: int
    currency_code: str
    formatted_amount: str
    converted_price: _containers.RepeatedCompositeFieldContainer[Offer]
    checkout_flow_required: bool
    full_price_micros: int
    formatted_full_amount: str
    offer_type: int
    rental_terms: RentalTerms
    on_sale_date: int
    promotion_label: _containers.RepeatedScalarFieldContainer[str]
    subscription_terms: SubscriptionTerms
    formatted_name: str
    formatted_description: str
    preorder: bool
    on_sale_date_display_time_zone_offset_millis: int
    licensed_offer_type: int
    subscription_content_terms: SubscriptionContentTerms
    offer_id: str
    preorder_fulfillment_display_date: int
    license_terms: LicenseTerms
    sale: bool
    voucher_terms: VoucherTerms
    offer_payment: _containers.RepeatedCompositeFieldContainer[OfferPayment]
    repeat_last_payment: bool
    buy_button_label: str
    instant_purchase_enabled: bool
    sale_end_timestamp: int
    sale_message: str
    def __init__(self, micros: _Optional[int] = ..., currency_code: _Optional[str] = ..., formatted_amount: _Optional[str] = ..., converted_price: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., checkout_flow_required: _Optional[bool] = ..., full_price_micros: _Optional[int] = ..., formatted_full_amount: _Optional[str] = ..., offer_type: _Optional[int] = ..., rental_terms: _Optional[_Union[RentalTerms, _Mapping]] = ..., on_sale_date: _Optional[int] = ..., promotion_label: _Optional[_Iterable[str]] = ..., subscription_terms: _Optional[_Union[SubscriptionTerms, _Mapping]] = ..., formatted_name: _Optional[str] = ..., formatted_description: _Optional[str] = ..., preorder: _Optional[bool] = ..., on_sale_date_display_time_zone_offset_millis: _Optional[int] = ..., licensed_offer_type: _Optional[int] = ..., subscription_content_terms: _Optional[_Union[SubscriptionContentTerms, _Mapping]] = ..., offer_id: _Optional[str] = ..., preorder_fulfillment_display_date: _Optional[int] = ..., license_terms: _Optional[_Union[LicenseTerms, _Mapping]] = ..., sale: _Optional[bool] = ..., voucher_terms: _Optional[_Union[VoucherTerms, _Mapping]] = ..., offer_payment: _Optional[_Iterable[_Union[OfferPayment, _Mapping]]] = ..., repeat_last_payment: _Optional[bool] = ..., buy_button_label: _Optional[str] = ..., instant_purchase_enabled: _Optional[bool] = ..., sale_end_timestamp: _Optional[int] = ..., sale_message: _Optional[str] = ...) -> None: ...

class MonthAndDay(_message.Message):
    __slots__ = ("month", "day")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    month: int
    day: int
    def __init__(self, month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class OfferPaymentPeriod(_message.Message):
    __slots__ = ("duration", "start", "end")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    duration: TimePeriod
    start: MonthAndDay
    end: MonthAndDay
    def __init__(self, duration: _Optional[_Union[TimePeriod, _Mapping]] = ..., start: _Optional[_Union[MonthAndDay, _Mapping]] = ..., end: _Optional[_Union[MonthAndDay, _Mapping]] = ...) -> None: ...

class OfferPaymentOverride(_message.Message):
    __slots__ = ("micros", "start", "end")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    micros: int
    start: MonthAndDay
    end: MonthAndDay
    def __init__(self, micros: _Optional[int] = ..., start: _Optional[_Union[MonthAndDay, _Mapping]] = ..., end: _Optional[_Union[MonthAndDay, _Mapping]] = ...) -> None: ...

class OfferPayment(_message.Message):
    __slots__ = ("micros", "currency_code", "offer_payment_period", "offer_payment_override")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    OFFER_PAYMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    OFFER_PAYMENT_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    micros: int
    currency_code: str
    offer_payment_period: OfferPaymentPeriod
    offer_payment_override: _containers.RepeatedCompositeFieldContainer[OfferPaymentOverride]
    def __init__(self, micros: _Optional[int] = ..., currency_code: _Optional[str] = ..., offer_payment_period: _Optional[_Union[OfferPaymentPeriod, _Mapping]] = ..., offer_payment_override: _Optional[_Iterable[_Union[OfferPaymentOverride, _Mapping]]] = ...) -> None: ...

class VoucherTerms(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RentalTerms(_message.Message):
    __slots__ = ("deprecated_grant_period_seconds", "deprecated_activate_period_seconds", "grant_period", "activate_period")
    DEPRECATED_GRANT_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_ACTIVATE_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    GRANT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    deprecated_grant_period_seconds: int
    deprecated_activate_period_seconds: int
    grant_period: TimePeriod
    activate_period: TimePeriod
    def __init__(self, deprecated_grant_period_seconds: _Optional[int] = ..., deprecated_activate_period_seconds: _Optional[int] = ..., grant_period: _Optional[_Union[TimePeriod, _Mapping]] = ..., activate_period: _Optional[_Union[TimePeriod, _Mapping]] = ...) -> None: ...

class SignedData(_message.Message):
    __slots__ = ("signed_data", "signature")
    SIGNED_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signed_data: str
    signature: str
    def __init__(self, signed_data: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class SubscriptionContentTerms(_message.Message):
    __slots__ = ("required_subscription",)
    REQUIRED_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    required_subscription: DocId
    def __init__(self, required_subscription: _Optional[_Union[DocId, _Mapping]] = ...) -> None: ...

class GroupLicenseInfo(_message.Message):
    __slots__ = ("licensed_offer_type", "gaia_group_id")
    LICENSED_OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAIA_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    licensed_offer_type: int
    gaia_group_id: int
    def __init__(self, licensed_offer_type: _Optional[int] = ..., gaia_group_id: _Optional[int] = ...) -> None: ...

class LicensedDocumentInfo(_message.Message):
    __slots__ = ("gaia_group_id",)
    GAIA_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    gaia_group_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gaia_group_id: _Optional[_Iterable[int]] = ...) -> None: ...

class OwnershipInfo(_message.Message):
    __slots__ = ("initiation_timestamp", "valid_until_timestamp", "auto_renewing", "refund_timeout_timestamp", "post_delivery_refund_window_millis", "developer_purchase_info", "pre_ordered", "hidden", "rental_terms", "group_license_info", "licensed_document_info", "quantity", "library_expiration_timestamp")
    INITIATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEWING_FIELD_NUMBER: _ClassVar[int]
    REFUND_TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    POST_DELIVERY_REFUND_WINDOW_MILLIS_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_PURCHASE_INFO_FIELD_NUMBER: _ClassVar[int]
    PRE_ORDERED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    RENTAL_TERMS_FIELD_NUMBER: _ClassVar[int]
    GROUP_LICENSE_INFO_FIELD_NUMBER: _ClassVar[int]
    LICENSED_DOCUMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    initiation_timestamp: int
    valid_until_timestamp: int
    auto_renewing: bool
    refund_timeout_timestamp: int
    post_delivery_refund_window_millis: int
    developer_purchase_info: SignedData
    pre_ordered: bool
    hidden: bool
    rental_terms: RentalTerms
    group_license_info: GroupLicenseInfo
    licensed_document_info: LicensedDocumentInfo
    quantity: int
    library_expiration_timestamp: int
    def __init__(self, initiation_timestamp: _Optional[int] = ..., valid_until_timestamp: _Optional[int] = ..., auto_renewing: _Optional[bool] = ..., refund_timeout_timestamp: _Optional[int] = ..., post_delivery_refund_window_millis: _Optional[int] = ..., developer_purchase_info: _Optional[_Union[SignedData, _Mapping]] = ..., pre_ordered: _Optional[bool] = ..., hidden: _Optional[bool] = ..., rental_terms: _Optional[_Union[RentalTerms, _Mapping]] = ..., group_license_info: _Optional[_Union[GroupLicenseInfo, _Mapping]] = ..., licensed_document_info: _Optional[_Union[LicensedDocumentInfo, _Mapping]] = ..., quantity: _Optional[int] = ..., library_expiration_timestamp: _Optional[int] = ...) -> None: ...

class SubscriptionTerms(_message.Message):
    __slots__ = ("recurring_period", "trial_period")
    RECURRING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    TRIAL_PERIOD_FIELD_NUMBER: _ClassVar[int]
    recurring_period: TimePeriod
    trial_period: TimePeriod
    def __init__(self, recurring_period: _Optional[_Union[TimePeriod, _Mapping]] = ..., trial_period: _Optional[_Union[TimePeriod, _Mapping]] = ...) -> None: ...

class TimePeriod(_message.Message):
    __slots__ = ("unit", "count")
    UNIT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    unit: int
    count: int
    def __init__(self, unit: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class BillingAddressSpec(_message.Message):
    __slots__ = ("billing_address_type", "required_field")
    BILLING_ADDRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_FIELD_NUMBER: _ClassVar[int]
    billing_address_type: int
    required_field: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, billing_address_type: _Optional[int] = ..., required_field: _Optional[_Iterable[int]] = ...) -> None: ...

class BillingProfile(_message.Message):
    __slots__ = ("instrument", "selected_external_instrument_id", "billing_profile_option")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_EXTERNAL_INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PROFILE_OPTION_FIELD_NUMBER: _ClassVar[int]
    instrument: _containers.RepeatedCompositeFieldContainer[Instrument]
    selected_external_instrument_id: str
    billing_profile_option: _containers.RepeatedCompositeFieldContainer[BillingProfileOption]
    def __init__(self, instrument: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ..., selected_external_instrument_id: _Optional[str] = ..., billing_profile_option: _Optional[_Iterable[_Union[BillingProfileOption, _Mapping]]] = ...) -> None: ...

class BillingProfileOption(_message.Message):
    __slots__ = ("type", "display_title", "external_instrument_id", "topup_info", "carrier_billing_instrument_status")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TITLE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TOPUP_INFO_FIELD_NUMBER: _ClassVar[int]
    CARRIER_BILLING_INSTRUMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    type: int
    display_title: str
    external_instrument_id: str
    topup_info: TopupInfo
    carrier_billing_instrument_status: CarrierBillingInstrumentStatus
    def __init__(self, type: _Optional[int] = ..., display_title: _Optional[str] = ..., external_instrument_id: _Optional[str] = ..., topup_info: _Optional[_Union[TopupInfo, _Mapping]] = ..., carrier_billing_instrument_status: _Optional[_Union[CarrierBillingInstrumentStatus, _Mapping]] = ...) -> None: ...

class CarrierBillingCredentials(_message.Message):
    __slots__ = ("value", "expiration")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    value: str
    expiration: int
    def __init__(self, value: _Optional[str] = ..., expiration: _Optional[int] = ...) -> None: ...

class CarrierBillingInstrument(_message.Message):
    __slots__ = ("instrument_key", "account_type", "currency_code", "transaction_limit", "subscriber_identifier", "encrypted_subscriber_info", "credentials", "accepted_carrier_tos")
    INSTRUMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_SUBSCRIBER_INFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CARRIER_TOS_FIELD_NUMBER: _ClassVar[int]
    instrument_key: str
    account_type: str
    currency_code: str
    transaction_limit: int
    subscriber_identifier: str
    encrypted_subscriber_info: EncryptedSubscriberInfo
    credentials: CarrierBillingCredentials
    accepted_carrier_tos: CarrierTos
    def __init__(self, instrument_key: _Optional[str] = ..., account_type: _Optional[str] = ..., currency_code: _Optional[str] = ..., transaction_limit: _Optional[int] = ..., subscriber_identifier: _Optional[str] = ..., encrypted_subscriber_info: _Optional[_Union[EncryptedSubscriberInfo, _Mapping]] = ..., credentials: _Optional[_Union[CarrierBillingCredentials, _Mapping]] = ..., accepted_carrier_tos: _Optional[_Union[CarrierTos, _Mapping]] = ...) -> None: ...

class CarrierBillingInstrumentStatus(_message.Message):
    __slots__ = ("carrier_tos", "association_required", "password_required", "carrier_password_prompt", "api_version", "name", "device_association", "carrier_support_phone_number")
    CARRIER_TOS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CARRIER_PASSWORD_PROMPT_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    CARRIER_SUPPORT_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    carrier_tos: CarrierTos
    association_required: bool
    password_required: bool
    carrier_password_prompt: PasswordPrompt
    api_version: int
    name: str
    device_association: DeviceAssociation
    carrier_support_phone_number: str
    def __init__(self, carrier_tos: _Optional[_Union[CarrierTos, _Mapping]] = ..., association_required: _Optional[bool] = ..., password_required: _Optional[bool] = ..., carrier_password_prompt: _Optional[_Union[PasswordPrompt, _Mapping]] = ..., api_version: _Optional[int] = ..., name: _Optional[str] = ..., device_association: _Optional[_Union[DeviceAssociation, _Mapping]] = ..., carrier_support_phone_number: _Optional[str] = ...) -> None: ...

class CarrierTos(_message.Message):
    __slots__ = ("dcb_tos", "pii_tos", "needs_dcb_tos_acceptance", "needs_pii_tos_acceptance")
    DCB_TOS_FIELD_NUMBER: _ClassVar[int]
    PII_TOS_FIELD_NUMBER: _ClassVar[int]
    NEEDS_DCB_TOS_ACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    NEEDS_PII_TOS_ACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    dcb_tos: CarrierTosEntry
    pii_tos: CarrierTosEntry
    needs_dcb_tos_acceptance: bool
    needs_pii_tos_acceptance: bool
    def __init__(self, dcb_tos: _Optional[_Union[CarrierTosEntry, _Mapping]] = ..., pii_tos: _Optional[_Union[CarrierTosEntry, _Mapping]] = ..., needs_dcb_tos_acceptance: _Optional[bool] = ..., needs_pii_tos_acceptance: _Optional[bool] = ...) -> None: ...

class CarrierTosEntry(_message.Message):
    __slots__ = ("url", "version")
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    url: str
    version: str
    def __init__(self, url: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class CreditCardInstrument(_message.Message):
    __slots__ = ("type", "escrow_handle", "last_digits", "expiration_month", "expiration_year", "escrow_efe_param")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ESCROW_HANDLE_FIELD_NUMBER: _ClassVar[int]
    LAST_DIGITS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_YEAR_FIELD_NUMBER: _ClassVar[int]
    ESCROW_EFE_PARAM_FIELD_NUMBER: _ClassVar[int]
    type: int
    escrow_handle: str
    last_digits: str
    expiration_month: int
    expiration_year: int
    escrow_efe_param: _containers.RepeatedCompositeFieldContainer[EfeParam]
    def __init__(self, type: _Optional[int] = ..., escrow_handle: _Optional[str] = ..., last_digits: _Optional[str] = ..., expiration_month: _Optional[int] = ..., expiration_year: _Optional[int] = ..., escrow_efe_param: _Optional[_Iterable[_Union[EfeParam, _Mapping]]] = ...) -> None: ...

class DeviceAssociation(_message.Message):
    __slots__ = ("user_token_request_message", "user_token_request_address")
    USER_TOKEN_REQUEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_TOKEN_REQUEST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    user_token_request_message: str
    user_token_request_address: str
    def __init__(self, user_token_request_message: _Optional[str] = ..., user_token_request_address: _Optional[str] = ...) -> None: ...

class DisabledInfo(_message.Message):
    __slots__ = ("disabled_reason", "disabled_message_html", "error_message")
    DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_MESSAGE_HTML_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    disabled_reason: int
    disabled_message_html: str
    error_message: str
    def __init__(self, disabled_reason: _Optional[int] = ..., disabled_message_html: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class EfeParam(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    value: str
    def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class Instrument(_message.Message):
    __slots__ = ("instrument_id", "billing_address", "credit_card", "carrier_billing", "billing_address_spec", "instrument_family", "carrier_billing_status", "display_title", "topup_info_deprecated", "version", "stored_value", "disabled_info")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREDIT_CARD_FIELD_NUMBER: _ClassVar[int]
    CARRIER_BILLING_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FAMILY_FIELD_NUMBER: _ClassVar[int]
    CARRIER_BILLING_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TITLE_FIELD_NUMBER: _ClassVar[int]
    TOPUP_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STORED_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_INFO_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    billing_address: Address
    credit_card: CreditCardInstrument
    carrier_billing: CarrierBillingInstrument
    billing_address_spec: BillingAddressSpec
    instrument_family: int
    carrier_billing_status: CarrierBillingInstrumentStatus
    display_title: str
    topup_info_deprecated: TopupInfo
    version: int
    stored_value: StoredValueInstrument
    disabled_info: _containers.RepeatedCompositeFieldContainer[DisabledInfo]
    def __init__(self, instrument_id: _Optional[str] = ..., billing_address: _Optional[_Union[Address, _Mapping]] = ..., credit_card: _Optional[_Union[CreditCardInstrument, _Mapping]] = ..., carrier_billing: _Optional[_Union[CarrierBillingInstrument, _Mapping]] = ..., billing_address_spec: _Optional[_Union[BillingAddressSpec, _Mapping]] = ..., instrument_family: _Optional[int] = ..., carrier_billing_status: _Optional[_Union[CarrierBillingInstrumentStatus, _Mapping]] = ..., display_title: _Optional[str] = ..., topup_info_deprecated: _Optional[_Union[TopupInfo, _Mapping]] = ..., version: _Optional[int] = ..., stored_value: _Optional[_Union[StoredValueInstrument, _Mapping]] = ..., disabled_info: _Optional[_Iterable[_Union[DisabledInfo, _Mapping]]] = ...) -> None: ...

class InstrumentSetupInfo(_message.Message):
    __slots__ = ("instrument_family", "supported", "address_challenge", "balance", "footer_html")
    INSTRUMENT_FAMILY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    FOOTER_HTML_FIELD_NUMBER: _ClassVar[int]
    instrument_family: int
    supported: bool
    address_challenge: AddressChallenge
    balance: Money
    footer_html: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instrument_family: _Optional[int] = ..., supported: _Optional[bool] = ..., address_challenge: _Optional[_Union[AddressChallenge, _Mapping]] = ..., balance: _Optional[_Union[Money, _Mapping]] = ..., footer_html: _Optional[_Iterable[str]] = ...) -> None: ...

class PasswordPrompt(_message.Message):
    __slots__ = ("prompt", "forgot_password_url")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    FORGOT_PASSWORD_URL_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    forgot_password_url: str
    def __init__(self, prompt: _Optional[str] = ..., forgot_password_url: _Optional[str] = ...) -> None: ...

class StoredValueInstrument(_message.Message):
    __slots__ = ("type", "balance", "topup_info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TOPUP_INFO_FIELD_NUMBER: _ClassVar[int]
    type: int
    balance: Money
    topup_info: TopupInfo
    def __init__(self, type: _Optional[int] = ..., balance: _Optional[_Union[Money, _Mapping]] = ..., topup_info: _Optional[_Union[TopupInfo, _Mapping]] = ...) -> None: ...

class TopupInfo(_message.Message):
    __slots__ = ("options_container_doc_id_deprecated", "options_list_url", "subtitle", "options_container_doc_id")
    OPTIONS_CONTAINER_DOC_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_CONTAINER_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    options_container_doc_id_deprecated: str
    options_list_url: str
    subtitle: str
    options_container_doc_id: DocId
    def __init__(self, options_container_doc_id_deprecated: _Optional[str] = ..., options_list_url: _Optional[str] = ..., subtitle: _Optional[str] = ..., options_container_doc_id: _Optional[_Union[DocId, _Mapping]] = ...) -> None: ...

class ConsumePurchaseResponse(_message.Message):
    __slots__ = ("library_update", "status")
    LIBRARY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    library_update: LibraryUpdate
    status: int
    def __init__(self, library_update: _Optional[_Union[LibraryUpdate, _Mapping]] = ..., status: _Optional[int] = ...) -> None: ...

class ContainerMetadata(_message.Message):
    __slots__ = ("browse_url", "next_page_url", "relevance", "estimated_results", "analytics_cookie", "ordered", "container_view", "left_icon")
    BROWSE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ORDERED_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_VIEW_FIELD_NUMBER: _ClassVar[int]
    LEFT_ICON_FIELD_NUMBER: _ClassVar[int]
    browse_url: str
    next_page_url: str
    relevance: float
    estimated_results: int
    analytics_cookie: str
    ordered: bool
    container_view: _containers.RepeatedCompositeFieldContainer[ContainerView]
    left_icon: Image
    def __init__(self, browse_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., relevance: _Optional[float] = ..., estimated_results: _Optional[int] = ..., analytics_cookie: _Optional[str] = ..., ordered: _Optional[bool] = ..., container_view: _Optional[_Iterable[_Union[ContainerView, _Mapping]]] = ..., left_icon: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class ContainerView(_message.Message):
    __slots__ = ("selected", "title", "list_url", "server_logs_cookie")
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_URL_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    selected: bool
    title: str
    list_url: str
    server_logs_cookie: bytes
    def __init__(self, selected: _Optional[bool] = ..., title: _Optional[str] = ..., list_url: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ...) -> None: ...

class FlagContentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClientDownloadRequest(_message.Message):
    __slots__ = ("url", "digests", "length", "resources", "signature", "user_initiated", "client_asn", "file_basename", "download_type", "locale", "apk_info", "android_id", "originating_packages", "originating_signature")
    class ApkInfo(_message.Message):
        __slots__ = ("package_name", "version_code")
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
        package_name: str
        version_code: int
        def __init__(self, package_name: _Optional[str] = ..., version_code: _Optional[int] = ...) -> None: ...
    class CertificateChain(_message.Message):
        __slots__ = ("element",)
        class Element(_message.Message):
            __slots__ = ("certificate", "parsed_successfully", "subject", "issuer", "fingerprint", "expiry_time", "start_time")
            CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            PARSED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
            SUBJECT_FIELD_NUMBER: _ClassVar[int]
            ISSUER_FIELD_NUMBER: _ClassVar[int]
            FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
            EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            certificate: bytes
            parsed_successfully: bool
            subject: bytes
            issuer: bytes
            fingerprint: bytes
            expiry_time: int
            start_time: int
            def __init__(self, certificate: _Optional[bytes] = ..., parsed_successfully: _Optional[bool] = ..., subject: _Optional[bytes] = ..., issuer: _Optional[bytes] = ..., fingerprint: _Optional[bytes] = ..., expiry_time: _Optional[int] = ..., start_time: _Optional[int] = ...) -> None: ...
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        element: _containers.RepeatedCompositeFieldContainer[ClientDownloadRequest.CertificateChain.Element]
        def __init__(self, element: _Optional[_Iterable[_Union[ClientDownloadRequest.CertificateChain.Element, _Mapping]]] = ...) -> None: ...
    class Digests(_message.Message):
        __slots__ = ("sha256", "sha1", "md5")
        SHA256_FIELD_NUMBER: _ClassVar[int]
        SHA1_FIELD_NUMBER: _ClassVar[int]
        MD5_FIELD_NUMBER: _ClassVar[int]
        sha256: bytes
        sha1: bytes
        md5: bytes
        def __init__(self, sha256: _Optional[bytes] = ..., sha1: _Optional[bytes] = ..., md5: _Optional[bytes] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ("url", "type", "remote_ip", "referrer")
        URL_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        REMOTE_IP_FIELD_NUMBER: _ClassVar[int]
        REFERRER_FIELD_NUMBER: _ClassVar[int]
        url: str
        type: int
        remote_ip: bytes
        referrer: str
        def __init__(self, url: _Optional[str] = ..., type: _Optional[int] = ..., remote_ip: _Optional[bytes] = ..., referrer: _Optional[str] = ...) -> None: ...
    class SignatureInfo(_message.Message):
        __slots__ = ("certificate_chain", "trusted")
        CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
        TRUSTED_FIELD_NUMBER: _ClassVar[int]
        certificate_chain: _containers.RepeatedCompositeFieldContainer[ClientDownloadRequest.CertificateChain]
        trusted: bool
        def __init__(self, certificate_chain: _Optional[_Iterable[_Union[ClientDownloadRequest.CertificateChain, _Mapping]]] = ..., trusted: _Optional[bool] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    DIGESTS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    USER_INITIATED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ASN_FIELD_NUMBER: _ClassVar[int]
    FILE_BASENAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    APK_INFO_FIELD_NUMBER: _ClassVar[int]
    ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATING_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    ORIGINATING_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    url: str
    digests: ClientDownloadRequest.Digests
    length: int
    resources: _containers.RepeatedCompositeFieldContainer[ClientDownloadRequest.Resource]
    signature: ClientDownloadRequest.SignatureInfo
    user_initiated: bool
    client_asn: _containers.RepeatedScalarFieldContainer[str]
    file_basename: str
    download_type: int
    locale: str
    apk_info: ClientDownloadRequest.ApkInfo
    android_id: int
    originating_packages: _containers.RepeatedScalarFieldContainer[str]
    originating_signature: ClientDownloadRequest.SignatureInfo
    def __init__(self, url: _Optional[str] = ..., digests: _Optional[_Union[ClientDownloadRequest.Digests, _Mapping]] = ..., length: _Optional[int] = ..., resources: _Optional[_Iterable[_Union[ClientDownloadRequest.Resource, _Mapping]]] = ..., signature: _Optional[_Union[ClientDownloadRequest.SignatureInfo, _Mapping]] = ..., user_initiated: _Optional[bool] = ..., client_asn: _Optional[_Iterable[str]] = ..., file_basename: _Optional[str] = ..., download_type: _Optional[int] = ..., locale: _Optional[str] = ..., apk_info: _Optional[_Union[ClientDownloadRequest.ApkInfo, _Mapping]] = ..., android_id: _Optional[int] = ..., originating_packages: _Optional[_Iterable[str]] = ..., originating_signature: _Optional[_Union[ClientDownloadRequest.SignatureInfo, _Mapping]] = ...) -> None: ...

class ClientDownloadResponse(_message.Message):
    __slots__ = ("verdict", "more_info", "token")
    class MoreInfo(_message.Message):
        __slots__ = ("description", "url")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        description: str
        url: str
        def __init__(self, description: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MORE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    verdict: int
    more_info: ClientDownloadResponse.MoreInfo
    token: bytes
    def __init__(self, verdict: _Optional[int] = ..., more_info: _Optional[_Union[ClientDownloadResponse.MoreInfo, _Mapping]] = ..., token: _Optional[bytes] = ...) -> None: ...

class ClientDownloadStatsRequest(_message.Message):
    __slots__ = ("user_decision", "token")
    USER_DECISION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_decision: int
    token: bytes
    def __init__(self, user_decision: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...

class DebugInfo(_message.Message):
    __slots__ = ("message", "timing")
    class Timing(_message.Message):
        __slots__ = ("name", "time_in_ms")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TIME_IN_MS_FIELD_NUMBER: _ClassVar[int]
        name: str
        time_in_ms: float
        def __init__(self, name: _Optional[str] = ..., time_in_ms: _Optional[float] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedScalarFieldContainer[str]
    timing: _containers.RepeatedCompositeFieldContainer[DebugInfo.Timing]
    def __init__(self, message: _Optional[_Iterable[str]] = ..., timing: _Optional[_Iterable[_Union[DebugInfo.Timing, _Mapping]]] = ...) -> None: ...

class DebugSettingsResponse(_message.Message):
    __slots__ = ("play_country_override", "play_country_debug_info")
    PLAY_COUNTRY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PLAY_COUNTRY_DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    play_country_override: str
    play_country_debug_info: str
    def __init__(self, play_country_override: _Optional[str] = ..., play_country_debug_info: _Optional[str] = ...) -> None: ...

class DeliveryResponse(_message.Message):
    __slots__ = ("status", "app_delivery_data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_DELIVERY_DATA_FIELD_NUMBER: _ClassVar[int]
    status: int
    app_delivery_data: AndroidAppDeliveryData
    def __init__(self, status: _Optional[int] = ..., app_delivery_data: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ...) -> None: ...

class BulkDetailsEntry(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class BulkDetailsRequest(_message.Message):
    __slots__ = ("doc_id", "include_child_docs", "include_details", "source_package_name", "installed_version_code")
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHILD_DOCS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    doc_id: _containers.RepeatedScalarFieldContainer[str]
    include_child_docs: bool
    include_details: bool
    source_package_name: str
    installed_version_code: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, doc_id: _Optional[_Iterable[str]] = ..., include_child_docs: _Optional[bool] = ..., include_details: _Optional[bool] = ..., source_package_name: _Optional[str] = ..., installed_version_code: _Optional[_Iterable[int]] = ...) -> None: ...

class BulkDetailsResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[BulkDetailsEntry]
    def __init__(self, entry: _Optional[_Iterable[_Union[BulkDetailsEntry, _Mapping]]] = ...) -> None: ...

class DetailsResponse(_message.Message):
    __slots__ = ("analytics_cookie", "user_review", "item", "footer_html", "server_logs_cookie", "discovery_badge", "enable_reviews", "features", "details_stream_url", "user_review_url", "post_acquire_details_stream_url")
    ANALYTICS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    USER_REVIEW_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    FOOTER_HTML_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_BADGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    DETAILS_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    USER_REVIEW_URL_FIELD_NUMBER: _ClassVar[int]
    POST_ACQUIRE_DETAILS_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    analytics_cookie: str
    user_review: Review
    item: Item
    footer_html: str
    server_logs_cookie: bytes
    discovery_badge: _containers.RepeatedCompositeFieldContainer[DiscoveryBadge]
    enable_reviews: bool
    features: Features
    details_stream_url: str
    user_review_url: str
    post_acquire_details_stream_url: str
    def __init__(self, analytics_cookie: _Optional[str] = ..., user_review: _Optional[_Union[Review, _Mapping]] = ..., item: _Optional[_Union[Item, _Mapping]] = ..., footer_html: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ..., discovery_badge: _Optional[_Iterable[_Union[DiscoveryBadge, _Mapping]]] = ..., enable_reviews: _Optional[bool] = ..., features: _Optional[_Union[Features, _Mapping]] = ..., details_stream_url: _Optional[str] = ..., user_review_url: _Optional[str] = ..., post_acquire_details_stream_url: _Optional[str] = ...) -> None: ...

class DiscoveryBadge(_message.Message):
    __slots__ = ("label", "image", "background_color", "badge_container1", "server_logs_cookie", "is_plus_one", "aggregate_rating", "user_star_rating", "download_count", "download_units", "content_description", "player_badge", "family_age_range_badge", "family_category_badge")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    BADGE_CONTAINER1_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    IS_PLUS_ONE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_RATING_FIELD_NUMBER: _ClassVar[int]
    USER_STAR_RATING_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_UNITS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_BADGE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_AGE_RANGE_BADGE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_CATEGORY_BADGE_FIELD_NUMBER: _ClassVar[int]
    label: str
    image: Image
    background_color: int
    badge_container1: DiscoveryBadgeLink
    server_logs_cookie: bytes
    is_plus_one: bool
    aggregate_rating: float
    user_star_rating: int
    download_count: str
    download_units: str
    content_description: str
    player_badge: PlayerBadge
    family_age_range_badge: bytes
    family_category_badge: bytes
    def __init__(self, label: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., background_color: _Optional[int] = ..., badge_container1: _Optional[_Union[DiscoveryBadgeLink, _Mapping]] = ..., server_logs_cookie: _Optional[bytes] = ..., is_plus_one: _Optional[bool] = ..., aggregate_rating: _Optional[float] = ..., user_star_rating: _Optional[int] = ..., download_count: _Optional[str] = ..., download_units: _Optional[str] = ..., content_description: _Optional[str] = ..., player_badge: _Optional[_Union[PlayerBadge, _Mapping]] = ..., family_age_range_badge: _Optional[bytes] = ..., family_category_badge: _Optional[bytes] = ...) -> None: ...

class PlayerBadge(_message.Message):
    __slots__ = ("overlay_icon",)
    OVERLAY_ICON_FIELD_NUMBER: _ClassVar[int]
    overlay_icon: Image
    def __init__(self, overlay_icon: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class DiscoveryBadgeLink(_message.Message):
    __slots__ = ("link", "user_reviews_url", "critic_reviews_url")
    LINK_FIELD_NUMBER: _ClassVar[int]
    USER_REVIEWS_URL_FIELD_NUMBER: _ClassVar[int]
    CRITIC_REVIEWS_URL_FIELD_NUMBER: _ClassVar[int]
    link: Link
    user_reviews_url: str
    critic_reviews_url: str
    def __init__(self, link: _Optional[_Union[Link, _Mapping]] = ..., user_reviews_url: _Optional[str] = ..., critic_reviews_url: _Optional[str] = ...) -> None: ...

class Features(_message.Message):
    __slots__ = ("feature_presence", "feature_rating")
    FEATURE_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_RATING_FIELD_NUMBER: _ClassVar[int]
    feature_presence: _containers.RepeatedCompositeFieldContainer[Feature]
    feature_rating: _containers.RepeatedCompositeFieldContainer[Feature]
    def __init__(self, feature_presence: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., feature_rating: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("label", "value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DeviceConfigurationProto(_message.Message):
    __slots__ = ("touch_screen", "keyboard", "navigation", "screen_layout", "has_hard_keyboard", "has_five_way_navigation", "screen_density", "gl_es_version", "system_shared_library", "system_available_feature", "native_platform", "screen_width", "screen_height", "system_supported_locale", "gl_extension", "device_class", "max_apk_download_size_mb", "smallest_screen_width_dp", "low_ram_device", "total_memory_bytes", "max_num_of_cpu_cores", "device_feature", "unknown28", "unknown30")
    TOUCH_SCREEN_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    HAS_HARD_KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    HAS_FIVE_WAY_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_DENSITY_FIELD_NUMBER: _ClassVar[int]
    GL_ES_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SHARED_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_AVAILABLE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SCREEN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SCREEN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SUPPORTED_LOCALE_FIELD_NUMBER: _ClassVar[int]
    GL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    MAX_APK_DOWNLOAD_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    SMALLEST_SCREEN_WIDTH_DP_FIELD_NUMBER: _ClassVar[int]
    LOW_RAM_DEVICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_OF_CPU_CORES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN30_FIELD_NUMBER: _ClassVar[int]
    touch_screen: int
    keyboard: int
    navigation: int
    screen_layout: int
    has_hard_keyboard: bool
    has_five_way_navigation: bool
    screen_density: int
    gl_es_version: int
    system_shared_library: _containers.RepeatedScalarFieldContainer[str]
    system_available_feature: _containers.RepeatedScalarFieldContainer[str]
    native_platform: _containers.RepeatedScalarFieldContainer[str]
    screen_width: int
    screen_height: int
    system_supported_locale: _containers.RepeatedScalarFieldContainer[str]
    gl_extension: _containers.RepeatedScalarFieldContainer[str]
    device_class: int
    max_apk_download_size_mb: int
    smallest_screen_width_dp: int
    low_ram_device: int
    total_memory_bytes: int
    max_num_of_cpu_cores: int
    device_feature: _containers.RepeatedCompositeFieldContainer[DeviceFeature]
    unknown28: int
    unknown30: int
    def __init__(self, touch_screen: _Optional[int] = ..., keyboard: _Optional[int] = ..., navigation: _Optional[int] = ..., screen_layout: _Optional[int] = ..., has_hard_keyboard: _Optional[bool] = ..., has_five_way_navigation: _Optional[bool] = ..., screen_density: _Optional[int] = ..., gl_es_version: _Optional[int] = ..., system_shared_library: _Optional[_Iterable[str]] = ..., system_available_feature: _Optional[_Iterable[str]] = ..., native_platform: _Optional[_Iterable[str]] = ..., screen_width: _Optional[int] = ..., screen_height: _Optional[int] = ..., system_supported_locale: _Optional[_Iterable[str]] = ..., gl_extension: _Optional[_Iterable[str]] = ..., device_class: _Optional[int] = ..., max_apk_download_size_mb: _Optional[int] = ..., smallest_screen_width_dp: _Optional[int] = ..., low_ram_device: _Optional[int] = ..., total_memory_bytes: _Optional[int] = ..., max_num_of_cpu_cores: _Optional[int] = ..., device_feature: _Optional[_Iterable[_Union[DeviceFeature, _Mapping]]] = ..., unknown28: _Optional[int] = ..., unknown30: _Optional[int] = ...) -> None: ...

class DeviceFeature(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ("doc_id", "fetch_doc_id", "sample_doc_id", "title", "url", "snippet", "price_deprecated", "availability", "image", "child", "aggregate_rating", "offer", "translated_snippet", "document_variant", "category_id", "decoration", "parent", "privacy_policy_url", "consumption_url", "estimated_num_children", "subtitle")
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    FETCH_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    PRICE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_RATING_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_SNIPPET_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    DECORATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_URL_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_NUM_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    doc_id: DocId
    fetch_doc_id: DocId
    sample_doc_id: DocId
    title: str
    url: str
    snippet: _containers.RepeatedScalarFieldContainer[str]
    price_deprecated: Offer
    availability: Availability
    image: _containers.RepeatedCompositeFieldContainer[Image]
    child: _containers.RepeatedCompositeFieldContainer[Document]
    aggregate_rating: AggregateRating
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    translated_snippet: _containers.RepeatedCompositeFieldContainer[TranslatedText]
    document_variant: _containers.RepeatedCompositeFieldContainer[DocumentVariant]
    category_id: _containers.RepeatedScalarFieldContainer[str]
    decoration: _containers.RepeatedCompositeFieldContainer[Document]
    parent: _containers.RepeatedCompositeFieldContainer[Document]
    privacy_policy_url: str
    consumption_url: str
    estimated_num_children: int
    subtitle: str
    def __init__(self, doc_id: _Optional[_Union[DocId, _Mapping]] = ..., fetch_doc_id: _Optional[_Union[DocId, _Mapping]] = ..., sample_doc_id: _Optional[_Union[DocId, _Mapping]] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., snippet: _Optional[_Iterable[str]] = ..., price_deprecated: _Optional[_Union[Offer, _Mapping]] = ..., availability: _Optional[_Union[Availability, _Mapping]] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., child: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., aggregate_rating: _Optional[_Union[AggregateRating, _Mapping]] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., translated_snippet: _Optional[_Iterable[_Union[TranslatedText, _Mapping]]] = ..., document_variant: _Optional[_Iterable[_Union[DocumentVariant, _Mapping]]] = ..., category_id: _Optional[_Iterable[str]] = ..., decoration: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., parent: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., privacy_policy_url: _Optional[str] = ..., consumption_url: _Optional[str] = ..., estimated_num_children: _Optional[int] = ..., subtitle: _Optional[str] = ...) -> None: ...

class DocumentVariant(_message.Message):
    __slots__ = ("variation_type", "rule", "title", "snippet", "recent_changes", "auto_translation", "offer", "channel_id", "child", "decoration", "image", "category_id", "subtitle")
    VARIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    RECENT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    DECORATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    variation_type: int
    rule: Rule
    title: str
    snippet: _containers.RepeatedScalarFieldContainer[str]
    recent_changes: str
    auto_translation: _containers.RepeatedCompositeFieldContainer[TranslatedText]
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    channel_id: int
    child: _containers.RepeatedCompositeFieldContainer[Document]
    decoration: _containers.RepeatedCompositeFieldContainer[Document]
    image: _containers.RepeatedCompositeFieldContainer[Image]
    category_id: _containers.RepeatedScalarFieldContainer[str]
    subtitle: str
    def __init__(self, variation_type: _Optional[int] = ..., rule: _Optional[_Union[Rule, _Mapping]] = ..., title: _Optional[str] = ..., snippet: _Optional[_Iterable[str]] = ..., recent_changes: _Optional[str] = ..., auto_translation: _Optional[_Iterable[_Union[TranslatedText, _Mapping]]] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., channel_id: _Optional[int] = ..., child: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., decoration: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., category_id: _Optional[_Iterable[str]] = ..., subtitle: _Optional[str] = ...) -> None: ...

class SectionImage(_message.Message):
    __slots__ = ("image_container",)
    IMAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    image_container: _containers.RepeatedCompositeFieldContainer[ImageContainer]
    def __init__(self, image_container: _Optional[_Iterable[_Union[ImageContainer, _Mapping]]] = ...) -> None: ...

class ImageContainer(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: Image
    def __init__(self, image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("image_type", "dimension", "image_url", "alt_text_localized", "secure_url", "position_in_sequence", "supports_fife_url_options", "citation", "duration_seconds", "fill_color_rgb", "autogen", "attribution", "background_color_rgb", "palette", "device_class", "supports_fife_monogram_option", "image_url_alt")
    class Dimension(_message.Message):
        __slots__ = ("width", "height", "aspect_ratio")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        aspect_ratio: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., aspect_ratio: _Optional[int] = ...) -> None: ...
    class Citation(_message.Message):
        __slots__ = ("title_localized", "url")
        TITLE_LOCALIZED_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        title_localized: str
        url: str
        def __init__(self, title_localized: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_LOCALIZED_FIELD_NUMBER: _ClassVar[int]
    SECURE_URL_FIELD_NUMBER: _ClassVar[int]
    POSITION_IN_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FIFE_URL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CITATION_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FILL_COLOR_RGB_FIELD_NUMBER: _ClassVar[int]
    AUTOGEN_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_RGB_FIELD_NUMBER: _ClassVar[int]
    PALETTE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FIFE_MONOGRAM_OPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_ALT_FIELD_NUMBER: _ClassVar[int]
    image_type: int
    dimension: Image.Dimension
    image_url: str
    alt_text_localized: str
    secure_url: str
    position_in_sequence: int
    supports_fife_url_options: bool
    citation: Image.Citation
    duration_seconds: int
    fill_color_rgb: str
    autogen: bool
    attribution: Attribution
    background_color_rgb: str
    palette: ImagePalette
    device_class: int
    supports_fife_monogram_option: bool
    image_url_alt: str
    def __init__(self, image_type: _Optional[int] = ..., dimension: _Optional[_Union[Image.Dimension, _Mapping]] = ..., image_url: _Optional[str] = ..., alt_text_localized: _Optional[str] = ..., secure_url: _Optional[str] = ..., position_in_sequence: _Optional[int] = ..., supports_fife_url_options: _Optional[bool] = ..., citation: _Optional[_Union[Image.Citation, _Mapping]] = ..., duration_seconds: _Optional[int] = ..., fill_color_rgb: _Optional[str] = ..., autogen: _Optional[bool] = ..., attribution: _Optional[_Union[Attribution, _Mapping]] = ..., background_color_rgb: _Optional[str] = ..., palette: _Optional[_Union[ImagePalette, _Mapping]] = ..., device_class: _Optional[int] = ..., supports_fife_monogram_option: _Optional[bool] = ..., image_url_alt: _Optional[str] = ...) -> None: ...

class Attribution(_message.Message):
    __slots__ = ("source_title", "source_url", "license_title", "license_url")
    SOURCE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TITLE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_URL_FIELD_NUMBER: _ClassVar[int]
    source_title: str
    source_url: str
    license_title: str
    license_url: str
    def __init__(self, source_title: _Optional[str] = ..., source_url: _Optional[str] = ..., license_title: _Optional[str] = ..., license_url: _Optional[str] = ...) -> None: ...

class ImagePalette(_message.Message):
    __slots__ = ("light_vibrant_rgb", "vibrant_rgb", "dark_vibrant_rgb", "light_muted_rgb", "muted_rgb", "dark_muted_rgb")
    LIGHT_VIBRANT_RGB_FIELD_NUMBER: _ClassVar[int]
    VIBRANT_RGB_FIELD_NUMBER: _ClassVar[int]
    DARK_VIBRANT_RGB_FIELD_NUMBER: _ClassVar[int]
    LIGHT_MUTED_RGB_FIELD_NUMBER: _ClassVar[int]
    MUTED_RGB_FIELD_NUMBER: _ClassVar[int]
    DARK_MUTED_RGB_FIELD_NUMBER: _ClassVar[int]
    light_vibrant_rgb: str
    vibrant_rgb: str
    dark_vibrant_rgb: str
    light_muted_rgb: str
    muted_rgb: str
    dark_muted_rgb: str
    def __init__(self, light_vibrant_rgb: _Optional[str] = ..., vibrant_rgb: _Optional[str] = ..., dark_vibrant_rgb: _Optional[str] = ..., light_muted_rgb: _Optional[str] = ..., muted_rgb: _Optional[str] = ..., dark_muted_rgb: _Optional[str] = ...) -> None: ...

class TranslatedText(_message.Message):
    __slots__ = ("text", "source_locale", "target_locale")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCALE_FIELD_NUMBER: _ClassVar[int]
    text: str
    source_locale: str
    target_locale: str
    def __init__(self, text: _Optional[str] = ..., source_locale: _Optional[str] = ..., target_locale: _Optional[str] = ...) -> None: ...

class PlusOneData(_message.Message):
    __slots__ = ("set_by_user", "total", "circles_total", "circles_people")
    SET_BY_USER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CIRCLES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    CIRCLES_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    set_by_user: bool
    total: int
    circles_total: int
    circles_people: _containers.RepeatedCompositeFieldContainer[PlusPerson]
    def __init__(self, set_by_user: _Optional[bool] = ..., total: _Optional[int] = ..., circles_total: _Optional[int] = ..., circles_people: _Optional[_Iterable[_Union[PlusPerson, _Mapping]]] = ...) -> None: ...

class PlusPerson(_message.Message):
    __slots__ = ("display_name", "profile_image_url")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    profile_image_url: str
    def __init__(self, display_name: _Optional[str] = ..., profile_image_url: _Optional[str] = ...) -> None: ...

class AppDetails(_message.Message):
    __slots__ = ("developer_name", "major_version_number", "version_code", "version_string", "title", "app_category", "content_rating", "info_download_size", "permission", "developer_email", "developer_website", "info_download", "package_name", "recent_changes_html", "info_updated_on", "file", "app_type", "certificate_hash", "varies_with_device", "certificate_set", "auto_acquire_free_app_if_higher_version_available_tag", "has_instant_link", "split_id", "gamepad_required", "externally_hosted", "ever_externally_hosted", "install_notes", "install_location", "target_sdk_version", "has_preregistration_promo_code", "dependencies", "testing_program_info", "early_access_info", "editor_choice", "instant_link", "developer_address", "publisher", "category_name", "download_count", "download_label_display", "app_launch", "tag_group", "in_app_product", "download_label_abbreviated", "download_label", "compatibility", "support")
    DEVELOPER_NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
    INFO_DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_WEBSITE_FIELD_NUMBER: _ClassVar[int]
    INFO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECENT_CHANGES_HTML_FIELD_NUMBER: _ClassVar[int]
    INFO_UPDATED_ON_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_HASH_FIELD_NUMBER: _ClassVar[int]
    VARIES_WITH_DEVICE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_SET_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACQUIRE_FREE_APP_IF_HIGHER_VERSION_AVAILABLE_TAG_FIELD_NUMBER: _ClassVar[int]
    HAS_INSTANT_LINK_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    GAMEPAD_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_HOSTED_FIELD_NUMBER: _ClassVar[int]
    EVER_EXTERNALLY_HOSTED_FIELD_NUMBER: _ClassVar[int]
    INSTALL_NOTES_FIELD_NUMBER: _ClassVar[int]
    INSTALL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    HAS_PREREGISTRATION_PROMO_CODE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    TESTING_PROGRAM_INFO_FIELD_NUMBER: _ClassVar[int]
    EARLY_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    EDITOR_CHOICE_FIELD_NUMBER: _ClassVar[int]
    INSTANT_LINK_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LABEL_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    APP_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    TAG_GROUP_FIELD_NUMBER: _ClassVar[int]
    IN_APP_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LABEL_ABBREVIATED_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LABEL_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    developer_name: str
    major_version_number: int
    version_code: int
    version_string: str
    title: str
    app_category: _containers.RepeatedScalarFieldContainer[str]
    content_rating: int
    info_download_size: int
    permission: _containers.RepeatedScalarFieldContainer[str]
    developer_email: str
    developer_website: str
    info_download: str
    package_name: str
    recent_changes_html: str
    info_updated_on: str
    file: _containers.RepeatedCompositeFieldContainer[FileMetadata]
    app_type: str
    certificate_hash: _containers.RepeatedScalarFieldContainer[str]
    varies_with_device: bool
    certificate_set: _containers.RepeatedCompositeFieldContainer[CertificateSet]
    auto_acquire_free_app_if_higher_version_available_tag: _containers.RepeatedScalarFieldContainer[str]
    has_instant_link: bool
    split_id: _containers.RepeatedScalarFieldContainer[str]
    gamepad_required: bool
    externally_hosted: bool
    ever_externally_hosted: bool
    install_notes: str
    install_location: int
    target_sdk_version: int
    has_preregistration_promo_code: str
    dependencies: Dependencies
    testing_program_info: TestingProgramInfo
    early_access_info: EarlyAccessInfo
    editor_choice: EditorChoice
    instant_link: str
    developer_address: str
    publisher: Publisher
    category_name: str
    download_count: int
    download_label_display: str
    app_launch: AppLaunch
    tag_group: TagGroup
    in_app_product: str
    download_label_abbreviated: str
    download_label: str
    compatibility: Compatibility
    support: Support
    def __init__(self, developer_name: _Optional[str] = ..., major_version_number: _Optional[int] = ..., version_code: _Optional[int] = ..., version_string: _Optional[str] = ..., title: _Optional[str] = ..., app_category: _Optional[_Iterable[str]] = ..., content_rating: _Optional[int] = ..., info_download_size: _Optional[int] = ..., permission: _Optional[_Iterable[str]] = ..., developer_email: _Optional[str] = ..., developer_website: _Optional[str] = ..., info_download: _Optional[str] = ..., package_name: _Optional[str] = ..., recent_changes_html: _Optional[str] = ..., info_updated_on: _Optional[str] = ..., file: _Optional[_Iterable[_Union[FileMetadata, _Mapping]]] = ..., app_type: _Optional[str] = ..., certificate_hash: _Optional[_Iterable[str]] = ..., varies_with_device: _Optional[bool] = ..., certificate_set: _Optional[_Iterable[_Union[CertificateSet, _Mapping]]] = ..., auto_acquire_free_app_if_higher_version_available_tag: _Optional[_Iterable[str]] = ..., has_instant_link: _Optional[bool] = ..., split_id: _Optional[_Iterable[str]] = ..., gamepad_required: _Optional[bool] = ..., externally_hosted: _Optional[bool] = ..., ever_externally_hosted: _Optional[bool] = ..., install_notes: _Optional[str] = ..., install_location: _Optional[int] = ..., target_sdk_version: _Optional[int] = ..., has_preregistration_promo_code: _Optional[str] = ..., dependencies: _Optional[_Union[Dependencies, _Mapping]] = ..., testing_program_info: _Optional[_Union[TestingProgramInfo, _Mapping]] = ..., early_access_info: _Optional[_Union[EarlyAccessInfo, _Mapping]] = ..., editor_choice: _Optional[_Union[EditorChoice, _Mapping]] = ..., instant_link: _Optional[str] = ..., developer_address: _Optional[str] = ..., publisher: _Optional[_Union[Publisher, _Mapping]] = ..., category_name: _Optional[str] = ..., download_count: _Optional[int] = ..., download_label_display: _Optional[str] = ..., app_launch: _Optional[_Union[AppLaunch, _Mapping]] = ..., tag_group: _Optional[_Union[TagGroup, _Mapping]] = ..., in_app_product: _Optional[str] = ..., download_label_abbreviated: _Optional[str] = ..., download_label: _Optional[str] = ..., compatibility: _Optional[_Union[Compatibility, _Mapping]] = ..., support: _Optional[_Union[Support, _Mapping]] = ...) -> None: ...

class AppLaunch(_message.Message):
    __slots__ = ("date", "time")
    class Time(_message.Message):
        __slots__ = ("timestamp", "unknown")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        unknown: int
        def __init__(self, timestamp: _Optional[int] = ..., unknown: _Optional[int] = ...) -> None: ...
    DATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    date: str
    time: AppLaunch.Time
    def __init__(self, date: _Optional[str] = ..., time: _Optional[_Union[AppLaunch.Time, _Mapping]] = ...) -> None: ...

class TagGroup(_message.Message):
    __slots__ = ("type1", "type2", "type3", "type4", "type5", "type6")
    TYPE1_FIELD_NUMBER: _ClassVar[int]
    TYPE2_FIELD_NUMBER: _ClassVar[int]
    TYPE3_FIELD_NUMBER: _ClassVar[int]
    TYPE4_FIELD_NUMBER: _ClassVar[int]
    TYPE5_FIELD_NUMBER: _ClassVar[int]
    TYPE6_FIELD_NUMBER: _ClassVar[int]
    type1: TagType
    type2: TagType
    type3: TagType
    type4: TagType
    type5: TagType
    type6: TagType
    def __init__(self, type1: _Optional[_Union[TagType, _Mapping]] = ..., type2: _Optional[_Union[TagType, _Mapping]] = ..., type3: _Optional[_Union[TagType, _Mapping]] = ..., type4: _Optional[_Union[TagType, _Mapping]] = ..., type5: _Optional[_Union[TagType, _Mapping]] = ..., type6: _Optional[_Union[TagType, _Mapping]] = ...) -> None: ...

class TagType(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[TagEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[TagEntry, _Mapping]]] = ...) -> None: ...

class TagEntry(_message.Message):
    __slots__ = ("name", "metadata", "category")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: TagMetadata
    category: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[TagMetadata, _Mapping]] = ..., category: _Optional[str] = ...) -> None: ...

class TagMetadata(_message.Message):
    __slots__ = ("category", "search")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    category: TagData
    search: TagData
    def __init__(self, category: _Optional[_Union[TagData, _Mapping]] = ..., search: _Optional[_Union[TagData, _Mapping]] = ...) -> None: ...

class TagData(_message.Message):
    __slots__ = ("url", "label")
    URL_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    url: str
    label: str
    def __init__(self, url: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class Support(_message.Message):
    __slots__ = ("developer_name", "developer_email", "developer_address", "developer_phone_number")
    DEVELOPER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    developer_name: str
    developer_email: str
    developer_address: str
    developer_phone_number: str
    def __init__(self, developer_name: _Optional[str] = ..., developer_email: _Optional[str] = ..., developer_address: _Optional[str] = ..., developer_phone_number: _Optional[str] = ...) -> None: ...

class Compatibility(_message.Message):
    __slots__ = ("active_devices",)
    ACTIVE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    active_devices: _containers.RepeatedCompositeFieldContainer[ActiveDevice]
    def __init__(self, active_devices: _Optional[_Iterable[_Union[ActiveDevice, _Mapping]]] = ...) -> None: ...

class ActiveDevice(_message.Message):
    __slots__ = ("required_os", "name")
    REQUIRED_OS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    required_os: str
    name: str
    def __init__(self, required_os: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ModifyLibrary(_message.Message):
    __slots__ = ("id", "package_to_add", "package_to_remove")
    ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    package_to_add: str
    package_to_remove: str
    def __init__(self, id: _Optional[str] = ..., package_to_add: _Optional[str] = ..., package_to_remove: _Optional[str] = ...) -> None: ...

class Publisher(_message.Message):
    __slots__ = ("publisher_stream",)
    PUBLISHER_STREAM_FIELD_NUMBER: _ClassVar[int]
    publisher_stream: PublisherStream
    def __init__(self, publisher_stream: _Optional[_Union[PublisherStream, _Mapping]] = ...) -> None: ...

class PublisherStream(_message.Message):
    __slots__ = ("more_url", "query", "browse_url")
    MORE_URL_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    BROWSE_URL_FIELD_NUMBER: _ClassVar[int]
    more_url: str
    query: str
    browse_url: str
    def __init__(self, more_url: _Optional[str] = ..., query: _Optional[str] = ..., browse_url: _Optional[str] = ...) -> None: ...

class EditorChoice(_message.Message):
    __slots__ = ("bulletins", "description", "stream", "title", "subtitle")
    BULLETINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    bulletins: _containers.RepeatedScalarFieldContainer[str]
    description: str
    stream: SubStream
    title: str
    subtitle: str
    def __init__(self, bulletins: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., stream: _Optional[_Union[SubStream, _Mapping]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ...) -> None: ...

class CertificateSet(_message.Message):
    __slots__ = ("certificate_hash", "sha256")
    CERTIFICATE_HASH_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    certificate_hash: str
    sha256: str
    def __init__(self, certificate_hash: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...

class Dependencies(_message.Message):
    __slots__ = ("unknown", "size", "dependency", "target_sdk", "unknown2", "split_apks", "library_dependency")
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    TARGET_SDK_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    SPLIT_APKS_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    unknown: int
    size: int
    dependency: _containers.RepeatedCompositeFieldContainer[Dependency]
    target_sdk: int
    unknown2: int
    split_apks: _containers.RepeatedScalarFieldContainer[str]
    library_dependency: _containers.RepeatedCompositeFieldContainer[LibraryDependency]
    def __init__(self, unknown: _Optional[int] = ..., size: _Optional[int] = ..., dependency: _Optional[_Iterable[_Union[Dependency, _Mapping]]] = ..., target_sdk: _Optional[int] = ..., unknown2: _Optional[int] = ..., split_apks: _Optional[_Iterable[str]] = ..., library_dependency: _Optional[_Iterable[_Union[LibraryDependency, _Mapping]]] = ...) -> None: ...

class Dependency(_message.Message):
    __slots__ = ("package_name", "version", "unknown4")
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    version: int
    unknown4: int
    def __init__(self, package_name: _Optional[str] = ..., version: _Optional[int] = ..., unknown4: _Optional[int] = ...) -> None: ...

class LibraryDependency(_message.Message):
    __slots__ = ("package_name", "version_code")
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    version_code: int
    def __init__(self, package_name: _Optional[str] = ..., version_code: _Optional[int] = ...) -> None: ...

class TestingProgramInfo(_message.Message):
    __slots__ = ("subscribed", "subscribed_and_installed", "email", "display_name", "image")
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_AND_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    subscribed: bool
    subscribed_and_installed: bool
    email: str
    display_name: str
    image: Image
    def __init__(self, subscribed: _Optional[bool] = ..., subscribed_and_installed: _Optional[bool] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class EarlyAccessInfo(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class DocumentDetails(_message.Message):
    __slots__ = ("app_details", "subscription_details")
    APP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    app_details: AppDetails
    subscription_details: SubscriptionDetails
    def __init__(self, app_details: _Optional[_Union[AppDetails, _Mapping]] = ..., subscription_details: _Optional[_Union[SubscriptionDetails, _Mapping]] = ...) -> None: ...

class PatchDetails(_message.Message):
    __slots__ = ("base_version_code", "size")
    BASE_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    base_version_code: int
    size: int
    def __init__(self, base_version_code: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class FileMetadata(_message.Message):
    __slots__ = ("file_type", "version_code", "size", "split_id", "compressed_size", "patch_details")
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    PATCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    file_type: int
    version_code: int
    size: int
    split_id: str
    compressed_size: int
    patch_details: _containers.RepeatedCompositeFieldContainer[PatchDetails]
    def __init__(self, file_type: _Optional[int] = ..., version_code: _Optional[int] = ..., size: _Optional[int] = ..., split_id: _Optional[str] = ..., compressed_size: _Optional[int] = ..., patch_details: _Optional[_Iterable[_Union[PatchDetails, _Mapping]]] = ...) -> None: ...

class SubscriptionDetails(_message.Message):
    __slots__ = ("subscription_period",)
    SUBSCRIPTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    subscription_period: int
    def __init__(self, subscription_period: _Optional[int] = ...) -> None: ...

class Bucket(_message.Message):
    __slots__ = ("multi_corpus", "title", "icon_url", "full_contents_url", "relevance", "estimated_results", "analytics_cookie", "full_contents_list_url", "next_page_url", "ordered")
    MULTI_CORPUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    FULL_CONTENTS_URL_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    FULL_CONTENTS_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ORDERED_FIELD_NUMBER: _ClassVar[int]
    multi_corpus: bool
    title: str
    icon_url: str
    full_contents_url: str
    relevance: float
    estimated_results: int
    analytics_cookie: str
    full_contents_list_url: str
    next_page_url: str
    ordered: bool
    def __init__(self, multi_corpus: _Optional[bool] = ..., title: _Optional[str] = ..., icon_url: _Optional[str] = ..., full_contents_url: _Optional[str] = ..., relevance: _Optional[float] = ..., estimated_results: _Optional[int] = ..., analytics_cookie: _Optional[str] = ..., full_contents_list_url: _Optional[str] = ..., next_page_url: _Optional[str] = ..., ordered: _Optional[bool] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("bucket", "item")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    bucket: _containers.RepeatedCompositeFieldContainer[Bucket]
    item: Item
    def __init__(self, bucket: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("id", "sub_id", "type", "category_id", "title", "creator", "description_html", "offer", "availability", "image", "sub_item", "container_metadata", "details", "aggregate_rating", "annotations", "details_url", "share_url", "reviews_url", "backend_url", "purchase_details_url", "details_reusable", "subtitle", "translated_description_html", "server_logs_cookie", "app_info", "mature", "promotional_description", "available_for_preregistration", "tip", "review_snippets_url", "force_shareability", "use_wishlist_as_primary_action", "review_questions_url", "review_summary_url", "content_rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUB_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SUB_ITEM_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_METADATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_RATING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_URL_FIELD_NUMBER: _ClassVar[int]
    BACKEND_URL_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    DETAILS_REUSABLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    APP_INFO_FIELD_NUMBER: _ClassVar[int]
    MATURE_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONAL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FOR_PREREGISTRATION_FIELD_NUMBER: _ClassVar[int]
    TIP_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SNIPPETS_URL_FIELD_NUMBER: _ClassVar[int]
    FORCE_SHAREABILITY_FIELD_NUMBER: _ClassVar[int]
    USE_WISHLIST_AS_PRIMARY_ACTION_FIELD_NUMBER: _ClassVar[int]
    REVIEW_QUESTIONS_URL_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SUMMARY_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    sub_id: str
    type: int
    category_id: int
    title: str
    creator: str
    description_html: str
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    availability: Availability
    image: _containers.RepeatedCompositeFieldContainer[Image]
    sub_item: _containers.RepeatedCompositeFieldContainer[Item]
    container_metadata: ContainerMetadata
    details: DocumentDetails
    aggregate_rating: AggregateRating
    annotations: Annotations
    details_url: str
    share_url: str
    reviews_url: str
    backend_url: str
    purchase_details_url: str
    details_reusable: bool
    subtitle: str
    translated_description_html: str
    server_logs_cookie: bytes
    app_info: AppInfo
    mature: bool
    promotional_description: str
    available_for_preregistration: bool
    tip: _containers.RepeatedCompositeFieldContainer[ReviewTip]
    review_snippets_url: str
    force_shareability: bool
    use_wishlist_as_primary_action: bool
    review_questions_url: str
    review_summary_url: str
    content_rating: ContentRating
    def __init__(self, id: _Optional[str] = ..., sub_id: _Optional[str] = ..., type: _Optional[int] = ..., category_id: _Optional[int] = ..., title: _Optional[str] = ..., creator: _Optional[str] = ..., description_html: _Optional[str] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., availability: _Optional[_Union[Availability, _Mapping]] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., sub_item: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., container_metadata: _Optional[_Union[ContainerMetadata, _Mapping]] = ..., details: _Optional[_Union[DocumentDetails, _Mapping]] = ..., aggregate_rating: _Optional[_Union[AggregateRating, _Mapping]] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ..., details_url: _Optional[str] = ..., share_url: _Optional[str] = ..., reviews_url: _Optional[str] = ..., backend_url: _Optional[str] = ..., purchase_details_url: _Optional[str] = ..., details_reusable: _Optional[bool] = ..., subtitle: _Optional[str] = ..., translated_description_html: _Optional[str] = ..., server_logs_cookie: _Optional[bytes] = ..., app_info: _Optional[_Union[AppInfo, _Mapping]] = ..., mature: _Optional[bool] = ..., promotional_description: _Optional[str] = ..., available_for_preregistration: _Optional[bool] = ..., tip: _Optional[_Iterable[_Union[ReviewTip, _Mapping]]] = ..., review_snippets_url: _Optional[str] = ..., force_shareability: _Optional[bool] = ..., use_wishlist_as_primary_action: _Optional[bool] = ..., review_questions_url: _Optional[str] = ..., review_summary_url: _Optional[str] = ..., content_rating: _Optional[_Union[ContentRating, _Mapping]] = ...) -> None: ...

class ContentRating(_message.Message):
    __slots__ = ("title", "recommendation_and_description_html", "content_rating_image", "recommendation", "description")
    class ContentRatingImage(_message.Message):
        __slots__ = ("dimension", "image")
        class Dimension(_message.Message):
            __slots__ = ("width", "height")
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            width: int
            height: int
            def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
        class Image(_message.Message):
            __slots__ = ("url",)
            URL_FIELD_NUMBER: _ClassVar[int]
            url: str
            def __init__(self, url: _Optional[str] = ...) -> None: ...
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        dimension: ContentRating.ContentRatingImage.Dimension
        image: ContentRating.ContentRatingImage.Image
        def __init__(self, dimension: _Optional[_Union[ContentRating.ContentRatingImage.Dimension, _Mapping]] = ..., image: _Optional[_Union[ContentRating.ContentRatingImage.Image, _Mapping]] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_AND_DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RATING_IMAGE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    recommendation_and_description_html: str
    content_rating_image: ContentRating.ContentRatingImage
    recommendation: str
    description: str
    def __init__(self, title: _Optional[str] = ..., recommendation_and_description_html: _Optional[str] = ..., content_rating_image: _Optional[_Union[ContentRating.ContentRatingImage, _Mapping]] = ..., recommendation: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class AppInfo(_message.Message):
    __slots__ = ("title", "section")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    section: _containers.RepeatedCompositeFieldContainer[AppInfoSection]
    def __init__(self, title: _Optional[str] = ..., section: _Optional[_Iterable[_Union[AppInfoSection, _Mapping]]] = ...) -> None: ...

class AppInfoSection(_message.Message):
    __slots__ = ("label", "container")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    label: str
    container: AppInfoContainer
    def __init__(self, label: _Optional[str] = ..., container: _Optional[_Union[AppInfoContainer, _Mapping]] = ...) -> None: ...

class AppInfoContainer(_message.Message):
    __slots__ = ("image", "description")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    image: Image
    description: str
    def __init__(self, image: _Optional[_Union[Image, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class Annotations(_message.Message):
    __slots__ = ("section_related", "section_more_by", "warning", "section_body_of_work", "section_core_content", "overlay_meta_data", "badge_for_creator", "info_badge", "annotation_link", "section_cross_sell", "section_related_item_type", "promoted_doc", "offer_note", "privacy_policy_url", "suggestion_reasons", "optimal_device_class_warning", "badge_container", "section_suggest_for_rating", "section_purchase_cross_sell", "overflow_link", "attribution_html", "purchase_history_details", "badge_for_legacy_rating", "voucher_info", "section_featured_apps", "details_page_cluster", "video_annotations", "section_purchase_related_topics", "my_subscription_details", "my_reward_details", "feature_badge", "snippet", "downloads_label", "badge_for_rating", "category_info", "reasons", "top_chart_stream", "category_name", "chip", "display_badge", "live_stream_url", "promotion_stream_url", "overlay_meta_data_extra", "section_image", "category_stream")
    SECTION_RELATED_FIELD_NUMBER: _ClassVar[int]
    SECTION_MORE_BY_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    SECTION_BODY_OF_WORK_FIELD_NUMBER: _ClassVar[int]
    SECTION_CORE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_META_DATA_FIELD_NUMBER: _ClassVar[int]
    BADGE_FOR_CREATOR_FIELD_NUMBER: _ClassVar[int]
    INFO_BADGE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_LINK_FIELD_NUMBER: _ClassVar[int]
    SECTION_CROSS_SELL_FIELD_NUMBER: _ClassVar[int]
    SECTION_RELATED_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_DOC_FIELD_NUMBER: _ClassVar[int]
    OFFER_NOTE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_REASONS_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_DEVICE_CLASS_WARNING_FIELD_NUMBER: _ClassVar[int]
    BADGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    SECTION_SUGGEST_FOR_RATING_FIELD_NUMBER: _ClassVar[int]
    SECTION_PURCHASE_CROSS_SELL_FIELD_NUMBER: _ClassVar[int]
    OVERFLOW_LINK_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_HTML_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_HISTORY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BADGE_FOR_LEGACY_RATING_FIELD_NUMBER: _ClassVar[int]
    VOUCHER_INFO_FIELD_NUMBER: _ClassVar[int]
    SECTION_FEATURED_APPS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_PAGE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SECTION_PURCHASE_RELATED_TOPICS_FIELD_NUMBER: _ClassVar[int]
    MY_SUBSCRIPTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MY_REWARD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_BADGE_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADS_LABEL_FIELD_NUMBER: _ClassVar[int]
    BADGE_FOR_RATING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_INFO_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    TOP_CHART_STREAM_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHIP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BADGE_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_META_DATA_EXTRA_FIELD_NUMBER: _ClassVar[int]
    SECTION_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_STREAM_FIELD_NUMBER: _ClassVar[int]
    section_related: SectionMetaData
    section_more_by: SectionMetaData
    warning: _containers.RepeatedCompositeFieldContainer[Warning]
    section_body_of_work: SectionMetaData
    section_core_content: SectionMetaData
    overlay_meta_data: OverlayMetaData
    badge_for_creator: _containers.RepeatedCompositeFieldContainer[Badge]
    info_badge: _containers.RepeatedCompositeFieldContainer[Badge]
    annotation_link: AnnotationLink
    section_cross_sell: SectionMetaData
    section_related_item_type: SectionMetaData
    promoted_doc: _containers.RepeatedCompositeFieldContainer[PromotedDoc]
    offer_note: str
    privacy_policy_url: str
    suggestion_reasons: SuggestionReasons
    optimal_device_class_warning: Warning
    badge_container: BadgeContainer
    section_suggest_for_rating: SectionMetaData
    section_purchase_cross_sell: SectionMetaData
    overflow_link: _containers.RepeatedCompositeFieldContainer[OverflowLink]
    attribution_html: str
    purchase_history_details: PurchaseHistoryDetails
    badge_for_legacy_rating: Badge
    voucher_info: _containers.RepeatedCompositeFieldContainer[VoucherInfo]
    section_featured_apps: SectionMetaData
    details_page_cluster: _containers.RepeatedCompositeFieldContainer[SectionMetaData]
    video_annotations: VideoAnnotations
    section_purchase_related_topics: SectionMetaData
    my_subscription_details: MySubscriptionDetails
    my_reward_details: MyRewardDetails
    feature_badge: _containers.RepeatedCompositeFieldContainer[Badge]
    snippet: Snippet
    downloads_label: str
    badge_for_rating: Badge
    category_info: CategoryInfo
    reasons: EditorReason
    top_chart_stream: Stream
    category_name: str
    chip: _containers.RepeatedCompositeFieldContainer[Chip]
    display_badge: _containers.RepeatedCompositeFieldContainer[Badge]
    live_stream_url: str
    promotion_stream_url: str
    overlay_meta_data_extra: OverlayMetaData
    section_image: SectionImage
    category_stream: SubStream
    def __init__(self, section_related: _Optional[_Union[SectionMetaData, _Mapping]] = ..., section_more_by: _Optional[_Union[SectionMetaData, _Mapping]] = ..., warning: _Optional[_Iterable[_Union[Warning, _Mapping]]] = ..., section_body_of_work: _Optional[_Union[SectionMetaData, _Mapping]] = ..., section_core_content: _Optional[_Union[SectionMetaData, _Mapping]] = ..., overlay_meta_data: _Optional[_Union[OverlayMetaData, _Mapping]] = ..., badge_for_creator: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ..., info_badge: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ..., annotation_link: _Optional[_Union[AnnotationLink, _Mapping]] = ..., section_cross_sell: _Optional[_Union[SectionMetaData, _Mapping]] = ..., section_related_item_type: _Optional[_Union[SectionMetaData, _Mapping]] = ..., promoted_doc: _Optional[_Iterable[_Union[PromotedDoc, _Mapping]]] = ..., offer_note: _Optional[str] = ..., privacy_policy_url: _Optional[str] = ..., suggestion_reasons: _Optional[_Union[SuggestionReasons, _Mapping]] = ..., optimal_device_class_warning: _Optional[_Union[Warning, _Mapping]] = ..., badge_container: _Optional[_Union[BadgeContainer, _Mapping]] = ..., section_suggest_for_rating: _Optional[_Union[SectionMetaData, _Mapping]] = ..., section_purchase_cross_sell: _Optional[_Union[SectionMetaData, _Mapping]] = ..., overflow_link: _Optional[_Iterable[_Union[OverflowLink, _Mapping]]] = ..., attribution_html: _Optional[str] = ..., purchase_history_details: _Optional[_Union[PurchaseHistoryDetails, _Mapping]] = ..., badge_for_legacy_rating: _Optional[_Union[Badge, _Mapping]] = ..., voucher_info: _Optional[_Iterable[_Union[VoucherInfo, _Mapping]]] = ..., section_featured_apps: _Optional[_Union[SectionMetaData, _Mapping]] = ..., details_page_cluster: _Optional[_Iterable[_Union[SectionMetaData, _Mapping]]] = ..., video_annotations: _Optional[_Union[VideoAnnotations, _Mapping]] = ..., section_purchase_related_topics: _Optional[_Union[SectionMetaData, _Mapping]] = ..., my_subscription_details: _Optional[_Union[MySubscriptionDetails, _Mapping]] = ..., my_reward_details: _Optional[_Union[MyRewardDetails, _Mapping]] = ..., feature_badge: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ..., snippet: _Optional[_Union[Snippet, _Mapping]] = ..., downloads_label: _Optional[str] = ..., badge_for_rating: _Optional[_Union[Badge, _Mapping]] = ..., category_info: _Optional[_Union[CategoryInfo, _Mapping]] = ..., reasons: _Optional[_Union[EditorReason, _Mapping]] = ..., top_chart_stream: _Optional[_Union[Stream, _Mapping]] = ..., category_name: _Optional[str] = ..., chip: _Optional[_Iterable[_Union[Chip, _Mapping]]] = ..., display_badge: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ..., live_stream_url: _Optional[str] = ..., promotion_stream_url: _Optional[str] = ..., overlay_meta_data_extra: _Optional[_Union[OverlayMetaData, _Mapping]] = ..., section_image: _Optional[_Union[SectionImage, _Mapping]] = ..., category_stream: _Optional[_Union[SubStream, _Mapping]] = ...) -> None: ...

class EditorReason(_message.Message):
    __slots__ = ("bulletin", "description")
    BULLETIN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    bulletin: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, bulletin: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

class SectionMetaData(_message.Message):
    __slots__ = ("header", "list_url", "browse_url", "description")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LIST_URL_FIELD_NUMBER: _ClassVar[int]
    BROWSE_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    header: str
    list_url: str
    browse_url: str
    description: str
    def __init__(self, header: _Optional[str] = ..., list_url: _Optional[str] = ..., browse_url: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class OverlayMetaData(_message.Message):
    __slots__ = ("overlay_header", "overlay_title", "overlay_description")
    OVERLAY_HEADER_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_TITLE_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    overlay_header: OverlayHeader
    overlay_title: OverlayTitle
    overlay_description: OverlayDescription
    def __init__(self, overlay_header: _Optional[_Union[OverlayHeader, _Mapping]] = ..., overlay_title: _Optional[_Union[OverlayTitle, _Mapping]] = ..., overlay_description: _Optional[_Union[OverlayDescription, _Mapping]] = ...) -> None: ...

class OverlayHeader(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OverlayTitle(_message.Message):
    __slots__ = ("title", "composite_image")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    title: str
    composite_image: CompositeImage
    def __init__(self, title: _Optional[str] = ..., composite_image: _Optional[_Union[CompositeImage, _Mapping]] = ...) -> None: ...

class CompositeImage(_message.Message):
    __slots__ = ("type", "url", "type_alt", "title", "url_alt")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_ALT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_ALT_FIELD_NUMBER: _ClassVar[int]
    type: int
    url: str
    type_alt: int
    title: str
    url_alt: str
    def __init__(self, type: _Optional[int] = ..., url: _Optional[str] = ..., type_alt: _Optional[int] = ..., title: _Optional[str] = ..., url_alt: _Optional[str] = ...) -> None: ...

class OverlayDescription(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class SuggestionReasons(_message.Message):
    __slots__ = ("reason", "neutral_dismissal", "positive_dismissal")
    REASON_FIELD_NUMBER: _ClassVar[int]
    NEUTRAL_DISMISSAL_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DISMISSAL_FIELD_NUMBER: _ClassVar[int]
    reason: _containers.RepeatedCompositeFieldContainer[Reason]
    neutral_dismissal: Dismissal
    positive_dismissal: Dismissal
    def __init__(self, reason: _Optional[_Iterable[_Union[Reason, _Mapping]]] = ..., neutral_dismissal: _Optional[_Union[Dismissal, _Mapping]] = ..., positive_dismissal: _Optional[_Union[Dismissal, _Mapping]] = ...) -> None: ...

class Reason(_message.Message):
    __slots__ = ("description_html", "reason_plus_one", "reason_review", "dismissal", "reason_user_action")
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    REASON_PLUS_ONE_FIELD_NUMBER: _ClassVar[int]
    REASON_REVIEW_FIELD_NUMBER: _ClassVar[int]
    DISMISSAL_FIELD_NUMBER: _ClassVar[int]
    REASON_USER_ACTION_FIELD_NUMBER: _ClassVar[int]
    description_html: str
    reason_plus_one: ReasonPlusOne
    reason_review: ReasonReview
    dismissal: Dismissal
    reason_user_action: ReasonUserAction
    def __init__(self, description_html: _Optional[str] = ..., reason_plus_one: _Optional[_Union[ReasonPlusOne, _Mapping]] = ..., reason_review: _Optional[_Union[ReasonReview, _Mapping]] = ..., dismissal: _Optional[_Union[Dismissal, _Mapping]] = ..., reason_user_action: _Optional[_Union[ReasonUserAction, _Mapping]] = ...) -> None: ...

class ReasonPlusOne(_message.Message):
    __slots__ = ("localized_description_html", "user_profile")
    LOCALIZED_DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    localized_description_html: str
    user_profile: _containers.RepeatedCompositeFieldContainer[UserProfile]
    def __init__(self, localized_description_html: _Optional[str] = ..., user_profile: _Optional[_Iterable[_Union[UserProfile, _Mapping]]] = ...) -> None: ...

class ReasonReview(_message.Message):
    __slots__ = ("review",)
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    review: Review
    def __init__(self, review: _Optional[_Union[Review, _Mapping]] = ...) -> None: ...

class ReasonUserAction(_message.Message):
    __slots__ = ("user_profile", "localized_description_html")
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    user_profile: UserProfile
    localized_description_html: str
    def __init__(self, user_profile: _Optional[_Union[UserProfile, _Mapping]] = ..., localized_description_html: _Optional[str] = ...) -> None: ...

class Dismissal(_message.Message):
    __slots__ = ("url", "description_html")
    URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
    url: str
    description_html: str
    def __init__(self, url: _Optional[str] = ..., description_html: _Optional[str] = ...) -> None: ...

class Snippet(_message.Message):
    __slots__ = ("snippet_html",)
    SNIPPET_HTML_FIELD_NUMBER: _ClassVar[int]
    snippet_html: str
    def __init__(self, snippet_html: _Optional[str] = ...) -> None: ...

class MyRewardDetails(_message.Message):
    __slots__ = ("expiration_time_millis", "expiration_description", "button_label", "link_action")
    EXPIRATION_TIME_MILLIS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    LINK_ACTION_FIELD_NUMBER: _ClassVar[int]
    expiration_time_millis: int
    expiration_description: str
    button_label: str
    link_action: Link
    def __init__(self, expiration_time_millis: _Optional[int] = ..., expiration_description: _Optional[str] = ..., button_label: _Optional[str] = ..., link_action: _Optional[_Union[Link, _Mapping]] = ...) -> None: ...

class MySubscriptionDetails(_message.Message):
    __slots__ = ("subscription_status_html", "title", "title_by_line_html", "formatted_price", "price_by_line_html", "cancel_subscription", "payment_declined_learn_more_link", "in_trial_period", "title_by_line_icon")
    SUBSCRIPTION_STATUS_HTML_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_BY_LINE_HTML_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_BY_LINE_HTML_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DECLINED_LEARN_MORE_LINK_FIELD_NUMBER: _ClassVar[int]
    IN_TRIAL_PERIOD_FIELD_NUMBER: _ClassVar[int]
    TITLE_BY_LINE_ICON_FIELD_NUMBER: _ClassVar[int]
    subscription_status_html: str
    title: str
    title_by_line_html: str
    formatted_price: str
    price_by_line_html: str
    cancel_subscription: bool
    payment_declined_learn_more_link: Link
    in_trial_period: bool
    title_by_line_icon: Image
    def __init__(self, subscription_status_html: _Optional[str] = ..., title: _Optional[str] = ..., title_by_line_html: _Optional[str] = ..., formatted_price: _Optional[str] = ..., price_by_line_html: _Optional[str] = ..., cancel_subscription: _Optional[bool] = ..., payment_declined_learn_more_link: _Optional[_Union[Link, _Mapping]] = ..., in_trial_period: _Optional[bool] = ..., title_by_line_icon: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class VideoAnnotations(_message.Message):
    __slots__ = ("bundle", "bundle_content_list_url", "extras_content_list_url", "also_available_in_list_url", "bundle_doc_id")
    BUNDLE_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_CONTENT_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_CONTENT_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    ALSO_AVAILABLE_IN_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    bundle: bool
    bundle_content_list_url: str
    extras_content_list_url: str
    also_available_in_list_url: str
    bundle_doc_id: _containers.RepeatedCompositeFieldContainer[DocId]
    def __init__(self, bundle: _Optional[bool] = ..., bundle_content_list_url: _Optional[str] = ..., extras_content_list_url: _Optional[str] = ..., also_available_in_list_url: _Optional[str] = ..., bundle_doc_id: _Optional[_Iterable[_Union[DocId, _Mapping]]] = ...) -> None: ...

class VoucherInfo(_message.Message):
    __slots__ = ("item", "offer")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    item: Item
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ...) -> None: ...

class BadgeContainer(_message.Message):
    __slots__ = ("title", "image", "badge")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    title: str
    image: _containers.RepeatedCompositeFieldContainer[Image]
    badge: _containers.RepeatedCompositeFieldContainer[Badge]
    def __init__(self, title: _Optional[str] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., badge: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ...) -> None: ...

class OverflowLink(_message.Message):
    __slots__ = ("title", "link")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    title: str
    link: Link
    def __init__(self, title: _Optional[str] = ..., link: _Optional[_Union[Link, _Mapping]] = ...) -> None: ...

class PromotedDoc(_message.Message):
    __slots__ = ("title", "subtitle", "image", "description", "details_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    image: _containers.RepeatedCompositeFieldContainer[Image]
    description: str
    details_url: str
    def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., description: _Optional[str] = ..., details_url: _Optional[str] = ...) -> None: ...

class Warning(_message.Message):
    __slots__ = ("localized_message",)
    LOCALIZED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    localized_message: str
    def __init__(self, localized_message: _Optional[str] = ...) -> None: ...

class AnnotationLink(_message.Message):
    __slots__ = ("uri", "resolved_link", "uri_backend")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LINK_FIELD_NUMBER: _ClassVar[int]
    URI_BACKEND_FIELD_NUMBER: _ClassVar[int]
    uri: str
    resolved_link: ResolvedLink
    uri_backend: int
    def __init__(self, uri: _Optional[str] = ..., resolved_link: _Optional[_Union[ResolvedLink, _Mapping]] = ..., uri_backend: _Optional[int] = ...) -> None: ...

class Rated(_message.Message):
    __slots__ = ("label", "image", "learn_more_html_link")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LEARN_MORE_HTML_LINK_FIELD_NUMBER: _ClassVar[int]
    label: str
    image: Image
    learn_more_html_link: str
    def __init__(self, label: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., learn_more_html_link: _Optional[str] = ...) -> None: ...

class Badge(_message.Message):
    __slots__ = ("major", "image", "minor", "minor_html", "sub_badge", "link", "description", "stream")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_HTML_FIELD_NUMBER: _ClassVar[int]
    SUB_BADGE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    major: str
    image: Image
    minor: str
    minor_html: str
    sub_badge: SubBadge
    link: StreamLink
    description: str
    stream: SubStream
    def __init__(self, major: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., minor: _Optional[str] = ..., minor_html: _Optional[str] = ..., sub_badge: _Optional[_Union[SubBadge, _Mapping]] = ..., link: _Optional[_Union[StreamLink, _Mapping]] = ..., description: _Optional[str] = ..., stream: _Optional[_Union[SubStream, _Mapping]] = ...) -> None: ...

class SubBadge(_message.Message):
    __slots__ = ("image", "description", "link")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    image: Image
    description: str
    link: StreamLink
    def __init__(self, image: _Optional[_Union[Image, _Mapping]] = ..., description: _Optional[str] = ..., link: _Optional[_Union[StreamLink, _Mapping]] = ...) -> None: ...

class Stream(_message.Message):
    __slots__ = ("title", "stream", "subtitle", "browse_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    BROWSE_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    stream: SubStream
    subtitle: str
    browse_url: str
    def __init__(self, title: _Optional[str] = ..., stream: _Optional[_Union[SubStream, _Mapping]] = ..., subtitle: _Optional[str] = ..., browse_url: _Optional[str] = ...) -> None: ...

class SubStream(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: StreamLink
    def __init__(self, link: _Optional[_Union[StreamLink, _Mapping]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("uri", "resolved_link", "uri_backend")
    URI_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LINK_FIELD_NUMBER: _ClassVar[int]
    URI_BACKEND_FIELD_NUMBER: _ClassVar[int]
    uri: str
    resolved_link: ResolvedLink
    uri_backend: int
    def __init__(self, uri: _Optional[str] = ..., resolved_link: _Optional[_Union[ResolvedLink, _Mapping]] = ..., uri_backend: _Optional[int] = ...) -> None: ...

class StreamLink(_message.Message):
    __slots__ = ("url", "stream_url", "search_url", "sub_category_url", "search_query")
    URL_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_URL_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_URL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    url: str
    stream_url: str
    search_url: str
    sub_category_url: str
    search_query: str
    def __init__(self, url: _Optional[str] = ..., stream_url: _Optional[str] = ..., search_url: _Optional[str] = ..., sub_category_url: _Optional[str] = ..., search_query: _Optional[str] = ...) -> None: ...

class Chip(_message.Message):
    __slots__ = ("title", "stream")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    title: str
    stream: SubStream
    def __init__(self, title: _Optional[str] = ..., stream: _Optional[_Union[SubStream, _Mapping]] = ...) -> None: ...

class CategoryInfo(_message.Message):
    __slots__ = ("category", "app_category")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    APP_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: str
    app_category: str
    def __init__(self, category: _Optional[str] = ..., app_category: _Optional[str] = ...) -> None: ...

class EncryptedSubscriberInfo(_message.Message):
    __slots__ = ("data", "encrypted_key", "signature", "init_vector", "google_key_version", "carrier_key_version")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    INIT_VECTOR_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    CARRIER_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    data: str
    encrypted_key: str
    signature: str
    init_vector: str
    google_key_version: int
    carrier_key_version: int
    def __init__(self, data: _Optional[str] = ..., encrypted_key: _Optional[str] = ..., signature: _Optional[str] = ..., init_vector: _Optional[str] = ..., google_key_version: _Optional[int] = ..., carrier_key_version: _Optional[int] = ...) -> None: ...

class Availability(_message.Message):
    __slots__ = ("restriction", "offer_type", "rule", "perdeviceavailabilityrestriction", "available_if_owned", "install", "filter_info", "ownership_info", "availability_problem", "hidden")
    class PerDeviceAvailabilityRestriction(_message.Message):
        __slots__ = ("android_id", "device_restriction", "channel_id", "filter_info")
        ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        FILTER_INFO_FIELD_NUMBER: _ClassVar[int]
        android_id: int
        device_restriction: int
        channel_id: int
        filter_info: FilterEvaluationInfo
        def __init__(self, android_id: _Optional[int] = ..., device_restriction: _Optional[int] = ..., channel_id: _Optional[int] = ..., filter_info: _Optional[_Union[FilterEvaluationInfo, _Mapping]] = ...) -> None: ...
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    PERDEVICEAVAILABILITYRESTRICTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_IF_OWNED_FIELD_NUMBER: _ClassVar[int]
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    FILTER_INFO_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_INFO_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    restriction: int
    offer_type: int
    rule: Rule
    perdeviceavailabilityrestriction: _containers.RepeatedCompositeFieldContainer[Availability.PerDeviceAvailabilityRestriction]
    available_if_owned: bool
    install: _containers.RepeatedCompositeFieldContainer[Install]
    filter_info: FilterEvaluationInfo
    ownership_info: OwnershipInfo
    availability_problem: _containers.RepeatedCompositeFieldContainer[AvailabilityProblem]
    hidden: bool
    def __init__(self, restriction: _Optional[int] = ..., offer_type: _Optional[int] = ..., rule: _Optional[_Union[Rule, _Mapping]] = ..., perdeviceavailabilityrestriction: _Optional[_Iterable[_Union[Availability.PerDeviceAvailabilityRestriction, _Mapping]]] = ..., available_if_owned: _Optional[bool] = ..., install: _Optional[_Iterable[_Union[Install, _Mapping]]] = ..., filter_info: _Optional[_Union[FilterEvaluationInfo, _Mapping]] = ..., ownership_info: _Optional[_Union[OwnershipInfo, _Mapping]] = ..., availability_problem: _Optional[_Iterable[_Union[AvailabilityProblem, _Mapping]]] = ..., hidden: _Optional[bool] = ...) -> None: ...

class AvailabilityProblem(_message.Message):
    __slots__ = ("problem_type", "missing_value")
    PROBLEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    MISSING_VALUE_FIELD_NUMBER: _ClassVar[int]
    problem_type: int
    missing_value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, problem_type: _Optional[int] = ..., missing_value: _Optional[_Iterable[str]] = ...) -> None: ...

class FilterEvaluationInfo(_message.Message):
    __slots__ = ("rule_evaluation",)
    RULE_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    rule_evaluation: _containers.RepeatedCompositeFieldContainer[RuleEvaluation]
    def __init__(self, rule_evaluation: _Optional[_Iterable[_Union[RuleEvaluation, _Mapping]]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("negate", "operator", "key", "string_arg", "long_arg", "double_arg", "sub_rule", "response_code", "comment", "string_arg_hash", "const_arg", "availability_problem_type", "include_missing_values")
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_ARG_FIELD_NUMBER: _ClassVar[int]
    LONG_ARG_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ARG_FIELD_NUMBER: _ClassVar[int]
    SUB_RULE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    STRING_ARG_HASH_FIELD_NUMBER: _ClassVar[int]
    CONST_ARG_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_PROBLEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MISSING_VALUES_FIELD_NUMBER: _ClassVar[int]
    negate: bool
    operator: int
    key: int
    string_arg: _containers.RepeatedScalarFieldContainer[str]
    long_arg: _containers.RepeatedScalarFieldContainer[int]
    double_arg: _containers.RepeatedScalarFieldContainer[float]
    sub_rule: _containers.RepeatedCompositeFieldContainer[Rule]
    response_code: int
    comment: str
    string_arg_hash: _containers.RepeatedScalarFieldContainer[int]
    const_arg: _containers.RepeatedScalarFieldContainer[int]
    availability_problem_type: int
    include_missing_values: bool
    def __init__(self, negate: _Optional[bool] = ..., operator: _Optional[int] = ..., key: _Optional[int] = ..., string_arg: _Optional[_Iterable[str]] = ..., long_arg: _Optional[_Iterable[int]] = ..., double_arg: _Optional[_Iterable[float]] = ..., sub_rule: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., response_code: _Optional[int] = ..., comment: _Optional[str] = ..., string_arg_hash: _Optional[_Iterable[int]] = ..., const_arg: _Optional[_Iterable[int]] = ..., availability_problem_type: _Optional[int] = ..., include_missing_values: _Optional[bool] = ...) -> None: ...

class RuleEvaluation(_message.Message):
    __slots__ = ("rule", "actual_string_value", "actual_long_value", "actual_bool_value", "actual_double_value")
    RULE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_LONG_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    actual_string_value: _containers.RepeatedScalarFieldContainer[str]
    actual_long_value: _containers.RepeatedScalarFieldContainer[int]
    actual_bool_value: _containers.RepeatedScalarFieldContainer[bool]
    actual_double_value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]] = ..., actual_string_value: _Optional[_Iterable[str]] = ..., actual_long_value: _Optional[_Iterable[int]] = ..., actual_bool_value: _Optional[_Iterable[bool]] = ..., actual_double_value: _Optional[_Iterable[float]] = ...) -> None: ...

class LibraryAppDetails(_message.Message):
    __slots__ = ("certificate_hash", "refund_timeout_timestamp", "post_delivery_refund_window_millis")
    CERTIFICATE_HASH_FIELD_NUMBER: _ClassVar[int]
    REFUND_TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    POST_DELIVERY_REFUND_WINDOW_MILLIS_FIELD_NUMBER: _ClassVar[int]
    certificate_hash: str
    refund_timeout_timestamp: int
    post_delivery_refund_window_millis: int
    def __init__(self, certificate_hash: _Optional[str] = ..., refund_timeout_timestamp: _Optional[int] = ..., post_delivery_refund_window_millis: _Optional[int] = ...) -> None: ...

class LibraryInAppDetails(_message.Message):
    __slots__ = ("signed_purchase_data", "signature")
    SIGNED_PURCHASE_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signed_purchase_data: str
    signature: str
    def __init__(self, signed_purchase_data: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class LibraryMutation(_message.Message):
    __slots__ = ("doc_id", "offer_type", "document_hash", "deleted", "app_details", "subscription_details", "in_app_details")
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    APP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IN_APP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    doc_id: DocId
    offer_type: int
    document_hash: int
    deleted: bool
    app_details: LibraryAppDetails
    subscription_details: LibrarySubscriptionDetails
    in_app_details: LibraryInAppDetails
    def __init__(self, doc_id: _Optional[_Union[DocId, _Mapping]] = ..., offer_type: _Optional[int] = ..., document_hash: _Optional[int] = ..., deleted: _Optional[bool] = ..., app_details: _Optional[_Union[LibraryAppDetails, _Mapping]] = ..., subscription_details: _Optional[_Union[LibrarySubscriptionDetails, _Mapping]] = ..., in_app_details: _Optional[_Union[LibraryInAppDetails, _Mapping]] = ...) -> None: ...

class LibrarySubscriptionDetails(_message.Message):
    __slots__ = ("initiation_timestamp", "valid_until_timestamp", "auto_renewing", "trial_until_timestamp", "signed_purchase_data", "signature")
    INITIATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEWING_FIELD_NUMBER: _ClassVar[int]
    TRIAL_UNTIL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNED_PURCHASE_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    initiation_timestamp: int
    valid_until_timestamp: int
    auto_renewing: bool
    trial_until_timestamp: int
    signed_purchase_data: str
    signature: str
    def __init__(self, initiation_timestamp: _Optional[int] = ..., valid_until_timestamp: _Optional[int] = ..., auto_renewing: _Optional[bool] = ..., trial_until_timestamp: _Optional[int] = ..., signed_purchase_data: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class LibraryUpdate(_message.Message):
    __slots__ = ("status", "corpus", "server_token", "mutation", "has_more", "library_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    corpus: int
    server_token: bytes
    mutation: _containers.RepeatedCompositeFieldContainer[LibraryMutation]
    has_more: bool
    library_id: str
    def __init__(self, status: _Optional[int] = ..., corpus: _Optional[int] = ..., server_token: _Optional[bytes] = ..., mutation: _Optional[_Iterable[_Union[LibraryMutation, _Mapping]]] = ..., has_more: _Optional[bool] = ..., library_id: _Optional[str] = ...) -> None: ...

class AndroidAppNotificationData(_message.Message):
    __slots__ = ("version_code", "asset_id")
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    version_code: int
    asset_id: str
    def __init__(self, version_code: _Optional[int] = ..., asset_id: _Optional[str] = ...) -> None: ...

class InAppNotificationData(_message.Message):
    __slots__ = ("checkout_order_id", "in_app_notification_id")
    CHECKOUT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    IN_APP_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    checkout_order_id: str
    in_app_notification_id: str
    def __init__(self, checkout_order_id: _Optional[str] = ..., in_app_notification_id: _Optional[str] = ...) -> None: ...

class LibraryDirtyData(_message.Message):
    __slots__ = ("backend", "library_id")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    backend: int
    library_id: str
    def __init__(self, backend: _Optional[int] = ..., library_id: _Optional[str] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ("notification_type", "timestamp", "doc_id", "doc_title", "user_email", "app_data", "app_delivery_data", "purchase_removal_data", "user_notification_data", "in_app_notification_data", "purchase_declined_data", "notification_id", "library_update", "library_dirty_data")
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    DOC_TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    APP_DATA_FIELD_NUMBER: _ClassVar[int]
    APP_DELIVERY_DATA_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_REMOVAL_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_NOTIFICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    IN_APP_NOTIFICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_DECLINED_DATA_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_DIRTY_DATA_FIELD_NUMBER: _ClassVar[int]
    notification_type: int
    timestamp: int
    doc_id: DocId
    doc_title: str
    user_email: str
    app_data: AndroidAppNotificationData
    app_delivery_data: AndroidAppDeliveryData
    purchase_removal_data: PurchaseRemovalData
    user_notification_data: UserNotificationData
    in_app_notification_data: InAppNotificationData
    purchase_declined_data: PurchaseDeclinedData
    notification_id: str
    library_update: LibraryUpdate
    library_dirty_data: LibraryDirtyData
    def __init__(self, notification_type: _Optional[int] = ..., timestamp: _Optional[int] = ..., doc_id: _Optional[_Union[DocId, _Mapping]] = ..., doc_title: _Optional[str] = ..., user_email: _Optional[str] = ..., app_data: _Optional[_Union[AndroidAppNotificationData, _Mapping]] = ..., app_delivery_data: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ..., purchase_removal_data: _Optional[_Union[PurchaseRemovalData, _Mapping]] = ..., user_notification_data: _Optional[_Union[UserNotificationData, _Mapping]] = ..., in_app_notification_data: _Optional[_Union[InAppNotificationData, _Mapping]] = ..., purchase_declined_data: _Optional[_Union[PurchaseDeclinedData, _Mapping]] = ..., notification_id: _Optional[str] = ..., library_update: _Optional[_Union[LibraryUpdate, _Mapping]] = ..., library_dirty_data: _Optional[_Union[LibraryDirtyData, _Mapping]] = ...) -> None: ...

class PurchaseDeclinedData(_message.Message):
    __slots__ = ("reason", "show_notification")
    REASON_FIELD_NUMBER: _ClassVar[int]
    SHOW_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    reason: int
    show_notification: bool
    def __init__(self, reason: _Optional[int] = ..., show_notification: _Optional[bool] = ...) -> None: ...

class PurchaseRemovalData(_message.Message):
    __slots__ = ("malicious",)
    MALICIOUS_FIELD_NUMBER: _ClassVar[int]
    malicious: bool
    def __init__(self, malicious: _Optional[bool] = ...) -> None: ...

class UserNotificationData(_message.Message):
    __slots__ = ("notification_title", "notification_text", "ticker_text", "dialog_title", "dialog_text")
    NOTIFICATION_TITLE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TEXT_FIELD_NUMBER: _ClassVar[int]
    TICKER_TEXT_FIELD_NUMBER: _ClassVar[int]
    DIALOG_TITLE_FIELD_NUMBER: _ClassVar[int]
    DIALOG_TEXT_FIELD_NUMBER: _ClassVar[int]
    notification_title: str
    notification_text: str
    ticker_text: str
    dialog_title: str
    dialog_text: str
    def __init__(self, notification_title: _Optional[str] = ..., notification_text: _Optional[str] = ..., ticker_text: _Optional[str] = ..., dialog_title: _Optional[str] = ..., dialog_text: _Optional[str] = ...) -> None: ...

class AggregateRating(_message.Message):
    __slots__ = ("type", "star_rating", "ratings_count", "one_star_ratings", "two_star_ratings", "three_star_ratings", "four_star_ratings", "five_star_ratings", "thumbs_up_count", "thumbs_down_count", "comment_count", "bayesian_mean_rating", "tip", "rating_label", "rating_count_label_abbreviated", "rating_count_label")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STAR_RATING_FIELD_NUMBER: _ClassVar[int]
    RATINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ONE_STAR_RATINGS_FIELD_NUMBER: _ClassVar[int]
    TWO_STAR_RATINGS_FIELD_NUMBER: _ClassVar[int]
    THREE_STAR_RATINGS_FIELD_NUMBER: _ClassVar[int]
    FOUR_STAR_RATINGS_FIELD_NUMBER: _ClassVar[int]
    FIVE_STAR_RATINGS_FIELD_NUMBER: _ClassVar[int]
    THUMBS_UP_COUNT_FIELD_NUMBER: _ClassVar[int]
    THUMBS_DOWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    BAYESIAN_MEAN_RATING_FIELD_NUMBER: _ClassVar[int]
    TIP_FIELD_NUMBER: _ClassVar[int]
    RATING_LABEL_FIELD_NUMBER: _ClassVar[int]
    RATING_COUNT_LABEL_ABBREVIATED_FIELD_NUMBER: _ClassVar[int]
    RATING_COUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
    type: int
    star_rating: float
    ratings_count: int
    one_star_ratings: int
    two_star_ratings: int
    three_star_ratings: int
    four_star_ratings: int
    five_star_ratings: int
    thumbs_up_count: int
    thumbs_down_count: int
    comment_count: int
    bayesian_mean_rating: float
    tip: _containers.RepeatedCompositeFieldContainer[Tip]
    rating_label: str
    rating_count_label_abbreviated: str
    rating_count_label: str
    def __init__(self, type: _Optional[int] = ..., star_rating: _Optional[float] = ..., ratings_count: _Optional[int] = ..., one_star_ratings: _Optional[int] = ..., two_star_ratings: _Optional[int] = ..., three_star_ratings: _Optional[int] = ..., four_star_ratings: _Optional[int] = ..., five_star_ratings: _Optional[int] = ..., thumbs_up_count: _Optional[int] = ..., thumbs_down_count: _Optional[int] = ..., comment_count: _Optional[int] = ..., bayesian_mean_rating: _Optional[float] = ..., tip: _Optional[_Iterable[_Union[Tip, _Mapping]]] = ..., rating_label: _Optional[str] = ..., rating_count_label_abbreviated: _Optional[str] = ..., rating_count_label: _Optional[str] = ...) -> None: ...

class Tip(_message.Message):
    __slots__ = ("tip_id", "text", "polarity", "review_count", "language", "snippet_review_id")
    TIP_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    POLARITY_FIELD_NUMBER: _ClassVar[int]
    REVIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    tip_id: str
    text: str
    polarity: int
    review_count: int
    language: str
    snippet_review_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tip_id: _Optional[str] = ..., text: _Optional[str] = ..., polarity: _Optional[int] = ..., review_count: _Optional[int] = ..., language: _Optional[str] = ..., snippet_review_id: _Optional[_Iterable[str]] = ...) -> None: ...

class ReviewTip(_message.Message):
    __slots__ = ("tip_url", "text", "polarity", "review_count")
    TIP_URL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    POLARITY_FIELD_NUMBER: _ClassVar[int]
    REVIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    tip_url: str
    text: str
    polarity: int
    review_count: int
    def __init__(self, tip_url: _Optional[str] = ..., text: _Optional[str] = ..., polarity: _Optional[int] = ..., review_count: _Optional[int] = ...) -> None: ...

class AcceptTosResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarrierBillingConfig(_message.Message):
    __slots__ = ("id", "name", "api_version", "provisioning_url", "credentials_url", "tos_required", "per_transaction_credentials_required", "send_subscriber_id_with_carrier_billing_requests")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_URL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_URL_FIELD_NUMBER: _ClassVar[int]
    TOS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PER_TRANSACTION_CREDENTIALS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SEND_SUBSCRIBER_ID_WITH_CARRIER_BILLING_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    api_version: int
    provisioning_url: str
    credentials_url: str
    tos_required: bool
    per_transaction_credentials_required: bool
    send_subscriber_id_with_carrier_billing_requests: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., api_version: _Optional[int] = ..., provisioning_url: _Optional[str] = ..., credentials_url: _Optional[str] = ..., tos_required: _Optional[bool] = ..., per_transaction_credentials_required: _Optional[bool] = ..., send_subscriber_id_with_carrier_billing_requests: _Optional[bool] = ...) -> None: ...

class BillingConfig(_message.Message):
    __slots__ = ("carrier_billing_config", "max_iab_api_version")
    CARRIER_BILLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_IAB_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    carrier_billing_config: CarrierBillingConfig
    max_iab_api_version: int
    def __init__(self, carrier_billing_config: _Optional[_Union[CarrierBillingConfig, _Mapping]] = ..., max_iab_api_version: _Optional[int] = ...) -> None: ...

class CorpusMetadata(_message.Message):
    __slots__ = ("backend", "name", "landing_url", "library_name", "recs_widget_url", "shop_name")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANDING_URL_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_NAME_FIELD_NUMBER: _ClassVar[int]
    RECS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    SHOP_NAME_FIELD_NUMBER: _ClassVar[int]
    backend: int
    name: str
    landing_url: str
    library_name: str
    recs_widget_url: str
    shop_name: str
    def __init__(self, backend: _Optional[int] = ..., name: _Optional[str] = ..., landing_url: _Optional[str] = ..., library_name: _Optional[str] = ..., recs_widget_url: _Optional[str] = ..., shop_name: _Optional[str] = ...) -> None: ...

class Experiments(_message.Message):
    __slots__ = ("experiment_id",)
    EXPERIMENT_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, experiment_id: _Optional[_Iterable[str]] = ...) -> None: ...

class SelfUpdateConfig(_message.Message):
    __slots__ = ("latest_client_version_code",)
    LATEST_CLIENT_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    latest_client_version_code: int
    def __init__(self, latest_client_version_code: _Optional[int] = ...) -> None: ...

class TocResponse(_message.Message):
    __slots__ = ("corpus", "tos_version_deprecated", "tos_content", "home_url", "experiments", "tos_checkbox_text_marketing_emails", "tos_token", "user_settings", "icon_override_url", "self_update_config", "requires_upload_device_config", "billing_config", "recs_widget_url", "social_home_url", "age_verification_required", "g_plus_signup_enabled", "redeem_enabled", "help_url", "theme_id", "entertainment_home_url", "cookie")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    TOS_VERSION_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    TOS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    TOS_CHECKBOX_TEXT_MARKETING_EMAILS_FIELD_NUMBER: _ClassVar[int]
    TOS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ICON_OVERRIDE_URL_FIELD_NUMBER: _ClassVar[int]
    SELF_UPDATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_UPLOAD_DEVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BILLING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RECS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_HOME_URL_FIELD_NUMBER: _ClassVar[int]
    AGE_VERIFICATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    G_PLUS_SIGNUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REDEEM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HELP_URL_FIELD_NUMBER: _ClassVar[int]
    THEME_ID_FIELD_NUMBER: _ClassVar[int]
    ENTERTAINMENT_HOME_URL_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    corpus: _containers.RepeatedCompositeFieldContainer[CorpusMetadata]
    tos_version_deprecated: int
    tos_content: str
    home_url: str
    experiments: Experiments
    tos_checkbox_text_marketing_emails: str
    tos_token: str
    user_settings: UserSettings
    icon_override_url: str
    self_update_config: SelfUpdateConfig
    requires_upload_device_config: bool
    billing_config: BillingConfig
    recs_widget_url: str
    social_home_url: str
    age_verification_required: bool
    g_plus_signup_enabled: bool
    redeem_enabled: bool
    help_url: str
    theme_id: int
    entertainment_home_url: str
    cookie: str
    def __init__(self, corpus: _Optional[_Iterable[_Union[CorpusMetadata, _Mapping]]] = ..., tos_version_deprecated: _Optional[int] = ..., tos_content: _Optional[str] = ..., home_url: _Optional[str] = ..., experiments: _Optional[_Union[Experiments, _Mapping]] = ..., tos_checkbox_text_marketing_emails: _Optional[str] = ..., tos_token: _Optional[str] = ..., user_settings: _Optional[_Union[UserSettings, _Mapping]] = ..., icon_override_url: _Optional[str] = ..., self_update_config: _Optional[_Union[SelfUpdateConfig, _Mapping]] = ..., requires_upload_device_config: _Optional[bool] = ..., billing_config: _Optional[_Union[BillingConfig, _Mapping]] = ..., recs_widget_url: _Optional[str] = ..., social_home_url: _Optional[str] = ..., age_verification_required: _Optional[bool] = ..., g_plus_signup_enabled: _Optional[bool] = ..., redeem_enabled: _Optional[bool] = ..., help_url: _Optional[str] = ..., theme_id: _Optional[int] = ..., entertainment_home_url: _Optional[str] = ..., cookie: _Optional[str] = ...) -> None: ...

class UserSettings(_message.Message):
    __slots__ = ("tos_checkbox_marketing_emails_opted_in", "privacy_setting")
    TOS_CHECKBOX_MARKETING_EMAILS_OPTED_IN_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_SETTING_FIELD_NUMBER: _ClassVar[int]
    tos_checkbox_marketing_emails_opted_in: bool
    privacy_setting: PrivacySetting
    def __init__(self, tos_checkbox_marketing_emails_opted_in: _Optional[bool] = ..., privacy_setting: _Optional[_Union[PrivacySetting, _Mapping]] = ...) -> None: ...

class PrivacySetting(_message.Message):
    __slots__ = ("type", "current_status", "enabled_by_default")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    type: int
    current_status: int
    enabled_by_default: bool
    def __init__(self, type: _Optional[int] = ..., current_status: _Optional[int] = ..., enabled_by_default: _Optional[bool] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ("list_response", "details_response", "review_response", "buy_response", "search_response", "toc_response", "browse_response", "purchase_status_response", "log_response", "flag_content_response", "bulk_details_response", "delivery_response", "accept_tos_response", "check_promo_offer_response", "instrument_setup_info_response", "android_checkin_response", "upload_device_config_response", "search_suggest_response", "consume_purchase_response", "billing_profile_response", "debug_settings_response", "check_iab_promo_response", "user_activity_settings_response", "record_user_activity_response", "redeem_code_response", "self_update_response", "get_initial_instrument_flow_state_response", "create_instrument_response", "challenge_response", "back_device_choices_response", "backup_document_choices_response", "early_update_response", "preloads_response", "my_accounts_response", "content_filter_response", "experiments_response", "survey_response", "ping_response", "update_user_setting_response", "get_user_settings_response", "get_sharing_settings_response", "update_sharing_settings_response", "review_snippets_response", "document_sharing_state_response", "module_delivery_response", "testing_program_response", "review_summary_response")
    LIST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BUY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOC_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BROWSE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FLAG_CONTENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BULK_DETAILS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_TOS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_PROMO_OFFER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_SETUP_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ANDROID_CHECKIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DEVICE_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SUGGEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONSUME_PURCHASE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BILLING_PROFILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECK_IAB_PROMO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USER_ACTIVITY_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RECORD_USER_ACTIVITY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REDEEM_CODE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SELF_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_INITIAL_INSTRUMENT_FLOW_STATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATE_INSTRUMENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BACK_DEVICE_CHOICES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DOCUMENT_CHOICES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EARLY_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PRELOADS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MY_ACCOUNTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FILTER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SURVEY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_USER_SETTING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_USER_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_SHARING_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SHARING_SETTINGS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SNIPPETS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SHARING_STATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MODULE_DELIVERY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TESTING_PROGRAM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SUMMARY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    list_response: ListResponse
    details_response: DetailsResponse
    review_response: ReviewResponse
    buy_response: BuyResponse
    search_response: SearchResponse
    toc_response: TocResponse
    browse_response: BrowseResponse
    purchase_status_response: PurchaseStatusResponse
    log_response: str
    flag_content_response: str
    bulk_details_response: BulkDetailsResponse
    delivery_response: DeliveryResponse
    accept_tos_response: AcceptTosResponse
    check_promo_offer_response: CheckPromoOfferResponse
    instrument_setup_info_response: InstrumentSetupInfoResponse
    android_checkin_response: AndroidCheckinResponse
    upload_device_config_response: UploadDeviceConfigResponse
    search_suggest_response: SearchSuggestResponse
    consume_purchase_response: ConsumePurchaseResponse
    billing_profile_response: BillingProfileResponse
    debug_settings_response: DebugSettingsResponse
    check_iab_promo_response: CheckIabPromoResponse
    user_activity_settings_response: UserActivitySettingsResponse
    record_user_activity_response: RecordUserActivityResponse
    redeem_code_response: RedeemCodeResponse
    self_update_response: SelfUpdateResponse
    get_initial_instrument_flow_state_response: GetInitialInstrumentFlowStateResponse
    create_instrument_response: CreateInstrumentResponse
    challenge_response: ChallengeResponse
    back_device_choices_response: BackDeviceChoicesResponse
    backup_document_choices_response: BackupDocumentChoicesResponse
    early_update_response: EarlyUpdateResponse
    preloads_response: PreloadsResponse
    my_accounts_response: MyAccountsResponse
    content_filter_response: ContentFilterResponse
    experiments_response: ExperimentsResponse
    survey_response: SurveyResponse
    ping_response: PingResponse
    update_user_setting_response: UpdateUserSettingResponse
    get_user_settings_response: GetUserSettingsResponse
    get_sharing_settings_response: GetSharingSettingsResponse
    update_sharing_settings_response: UpdateSharingSettingsResponse
    review_snippets_response: ReviewSnippetsResponse
    document_sharing_state_response: DocumentSharingStateResponse
    module_delivery_response: ModuleDeliveryResponse
    testing_program_response: TestingProgramResponse
    review_summary_response: ReviewResponse
    def __init__(self, list_response: _Optional[_Union[ListResponse, _Mapping]] = ..., details_response: _Optional[_Union[DetailsResponse, _Mapping]] = ..., review_response: _Optional[_Union[ReviewResponse, _Mapping]] = ..., buy_response: _Optional[_Union[BuyResponse, _Mapping]] = ..., search_response: _Optional[_Union[SearchResponse, _Mapping]] = ..., toc_response: _Optional[_Union[TocResponse, _Mapping]] = ..., browse_response: _Optional[_Union[BrowseResponse, _Mapping]] = ..., purchase_status_response: _Optional[_Union[PurchaseStatusResponse, _Mapping]] = ..., log_response: _Optional[str] = ..., flag_content_response: _Optional[str] = ..., bulk_details_response: _Optional[_Union[BulkDetailsResponse, _Mapping]] = ..., delivery_response: _Optional[_Union[DeliveryResponse, _Mapping]] = ..., accept_tos_response: _Optional[_Union[AcceptTosResponse, _Mapping]] = ..., check_promo_offer_response: _Optional[_Union[CheckPromoOfferResponse, _Mapping]] = ..., instrument_setup_info_response: _Optional[_Union[InstrumentSetupInfoResponse, _Mapping]] = ..., android_checkin_response: _Optional[_Union[AndroidCheckinResponse, _Mapping]] = ..., upload_device_config_response: _Optional[_Union[UploadDeviceConfigResponse, _Mapping]] = ..., search_suggest_response: _Optional[_Union[SearchSuggestResponse, _Mapping]] = ..., consume_purchase_response: _Optional[_Union[ConsumePurchaseResponse, _Mapping]] = ..., billing_profile_response: _Optional[_Union[BillingProfileResponse, _Mapping]] = ..., debug_settings_response: _Optional[_Union[DebugSettingsResponse, _Mapping]] = ..., check_iab_promo_response: _Optional[_Union[CheckIabPromoResponse, _Mapping]] = ..., user_activity_settings_response: _Optional[_Union[UserActivitySettingsResponse, _Mapping]] = ..., record_user_activity_response: _Optional[_Union[RecordUserActivityResponse, _Mapping]] = ..., redeem_code_response: _Optional[_Union[RedeemCodeResponse, _Mapping]] = ..., self_update_response: _Optional[_Union[SelfUpdateResponse, _Mapping]] = ..., get_initial_instrument_flow_state_response: _Optional[_Union[GetInitialInstrumentFlowStateResponse, _Mapping]] = ..., create_instrument_response: _Optional[_Union[CreateInstrumentResponse, _Mapping]] = ..., challenge_response: _Optional[_Union[ChallengeResponse, _Mapping]] = ..., back_device_choices_response: _Optional[_Union[BackDeviceChoicesResponse, _Mapping]] = ..., backup_document_choices_response: _Optional[_Union[BackupDocumentChoicesResponse, _Mapping]] = ..., early_update_response: _Optional[_Union[EarlyUpdateResponse, _Mapping]] = ..., preloads_response: _Optional[_Union[PreloadsResponse, _Mapping]] = ..., my_accounts_response: _Optional[_Union[MyAccountsResponse, _Mapping]] = ..., content_filter_response: _Optional[_Union[ContentFilterResponse, _Mapping]] = ..., experiments_response: _Optional[_Union[ExperimentsResponse, _Mapping]] = ..., survey_response: _Optional[_Union[SurveyResponse, _Mapping]] = ..., ping_response: _Optional[_Union[PingResponse, _Mapping]] = ..., update_user_setting_response: _Optional[_Union[UpdateUserSettingResponse, _Mapping]] = ..., get_user_settings_response: _Optional[_Union[GetUserSettingsResponse, _Mapping]] = ..., get_sharing_settings_response: _Optional[_Union[GetSharingSettingsResponse, _Mapping]] = ..., update_sharing_settings_response: _Optional[_Union[UpdateSharingSettingsResponse, _Mapping]] = ..., review_snippets_response: _Optional[_Union[ReviewSnippetsResponse, _Mapping]] = ..., document_sharing_state_response: _Optional[_Union[DocumentSharingStateResponse, _Mapping]] = ..., module_delivery_response: _Optional[_Union[ModuleDeliveryResponse, _Mapping]] = ..., testing_program_response: _Optional[_Union[TestingProgramResponse, _Mapping]] = ..., review_summary_response: _Optional[_Union[ReviewResponse, _Mapping]] = ...) -> None: ...

class CheckIabPromoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserActivitySettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordUserActivityResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RedeemCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfUpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInitialInstrumentFlowStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateInstrumentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChallengeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackDeviceChoicesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupDocumentChoicesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EarlyUpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PreloadsResponse(_message.Message):
    __slots__ = ("config_preload", "app_preload")
    class Preload(_message.Message):
        __slots__ = ("doc_id", "version_code", "title", "icon", "delivery_token", "install_location", "size")
        DOC_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        DELIVERY_TOKEN_FIELD_NUMBER: _ClassVar[int]
        INSTALL_LOCATION_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        doc_id: DocId
        version_code: int
        title: str
        icon: Image
        delivery_token: str
        install_location: int
        size: int
        def __init__(self, doc_id: _Optional[_Union[DocId, _Mapping]] = ..., version_code: _Optional[int] = ..., title: _Optional[str] = ..., icon: _Optional[_Union[Image, _Mapping]] = ..., delivery_token: _Optional[str] = ..., install_location: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    CONFIG_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    APP_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    config_preload: PreloadsResponse.Preload
    app_preload: _containers.RepeatedCompositeFieldContainer[PreloadsResponse.Preload]
    def __init__(self, config_preload: _Optional[_Union[PreloadsResponse.Preload, _Mapping]] = ..., app_preload: _Optional[_Iterable[_Union[PreloadsResponse.Preload, _Mapping]]] = ...) -> None: ...

class MyAccountsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContentFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExperimentsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SurveyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserSettingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSharingSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSharingSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReviewSnippetsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DocumentSharingStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModuleDeliveryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PreFetch(_message.Message):
    __slots__ = ("url", "response", "etag", "ttl", "soft_ttl")
    URL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    SOFT_TTL_FIELD_NUMBER: _ClassVar[int]
    url: str
    response: ResponseWrapper
    etag: str
    ttl: int
    soft_ttl: int
    def __init__(self, url: _Optional[str] = ..., response: _Optional[_Union[ResponseWrapper, _Mapping]] = ..., etag: _Optional[str] = ..., ttl: _Optional[int] = ..., soft_ttl: _Optional[int] = ...) -> None: ...

class ServerMetadata(_message.Message):
    __slots__ = ("latency_millis",)
    LATENCY_MILLIS_FIELD_NUMBER: _ClassVar[int]
    latency_millis: int
    def __init__(self, latency_millis: _Optional[int] = ...) -> None: ...

class Targets(_message.Message):
    __slots__ = ("target_id", "signature")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    target_id: _containers.RepeatedScalarFieldContainer[int]
    signature: bytes
    def __init__(self, target_id: _Optional[_Iterable[int]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class ServerCookie(_message.Message):
    __slots__ = ("type", "token")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    type: int
    token: bytes
    def __init__(self, type: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...

class ServerCookies(_message.Message):
    __slots__ = ("server_cookie",)
    SERVER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    server_cookie: _containers.RepeatedCompositeFieldContainer[ServerCookie]
    def __init__(self, server_cookie: _Optional[_Iterable[_Union[ServerCookie, _Mapping]]] = ...) -> None: ...

class ResponseWrapper(_message.Message):
    __slots__ = ("payload", "commands", "pre_fetch", "notification", "server_metadata", "targets", "server_cookies", "server_logs_cookie")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    PRE_FETCH_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SERVER_METADATA_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SERVER_COOKIES_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    payload: Payload
    commands: ServerCommands
    pre_fetch: PreFetch
    notification: _containers.RepeatedCompositeFieldContainer[Notification]
    server_metadata: ServerMetadata
    targets: Targets
    server_cookies: ServerCookies
    server_logs_cookie: bytes
    def __init__(self, payload: _Optional[_Union[Payload, _Mapping]] = ..., commands: _Optional[_Union[ServerCommands, _Mapping]] = ..., pre_fetch: _Optional[_Union[PreFetch, _Mapping]] = ..., notification: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ..., server_metadata: _Optional[_Union[ServerMetadata, _Mapping]] = ..., targets: _Optional[_Union[Targets, _Mapping]] = ..., server_cookies: _Optional[_Union[ServerCookies, _Mapping]] = ..., server_logs_cookie: _Optional[bytes] = ...) -> None: ...

class ResponseWrapperApi(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: PayloadApi
    def __init__(self, payload: _Optional[_Union[PayloadApi, _Mapping]] = ...) -> None: ...

class PayloadApi(_message.Message):
    __slots__ = ("user_profile_response",)
    USER_PROFILE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    user_profile_response: UserProfileResponse
    def __init__(self, user_profile_response: _Optional[_Union[UserProfileResponse, _Mapping]] = ...) -> None: ...

class UserProfileResponse(_message.Message):
    __slots__ = ("user_profile",)
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    user_profile: UserProfile
    def __init__(self, user_profile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class ServerCommands(_message.Message):
    __slots__ = ("clear_cache", "display_error_message", "log_error_stacktrace")
    CLEAR_CACHE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_ERROR_STACKTRACE_FIELD_NUMBER: _ClassVar[int]
    clear_cache: bool
    display_error_message: str
    log_error_stacktrace: str
    def __init__(self, clear_cache: _Optional[bool] = ..., display_error_message: _Optional[str] = ..., log_error_stacktrace: _Optional[str] = ...) -> None: ...

class GetReviewsResponse(_message.Message):
    __slots__ = ("review", "matching_count")
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    MATCHING_COUNT_FIELD_NUMBER: _ClassVar[int]
    review: _containers.RepeatedCompositeFieldContainer[Review]
    matching_count: int
    def __init__(self, review: _Optional[_Iterable[_Union[Review, _Mapping]]] = ..., matching_count: _Optional[int] = ...) -> None: ...

class Review(_message.Message):
    __slots__ = ("author_name", "url", "source", "version", "timestamp", "star_rating", "title", "comment", "comment_id", "device_name", "reply_text", "reply_time_stamp", "author", "user_profile", "sentiment", "helpful_count", "thumbs_up_count")
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STAR_RATING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLY_TEXT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    HELPFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    THUMBS_UP_COUNT_FIELD_NUMBER: _ClassVar[int]
    author_name: str
    url: bytes
    source: str
    version: str
    timestamp: int
    star_rating: int
    title: str
    comment: str
    comment_id: str
    device_name: str
    reply_text: str
    reply_time_stamp: int
    author: ReviewAuthor
    user_profile: UserProfile
    sentiment: Image
    helpful_count: int
    thumbs_up_count: int
    def __init__(self, author_name: _Optional[str] = ..., url: _Optional[bytes] = ..., source: _Optional[str] = ..., version: _Optional[str] = ..., timestamp: _Optional[int] = ..., star_rating: _Optional[int] = ..., title: _Optional[str] = ..., comment: _Optional[str] = ..., comment_id: _Optional[str] = ..., device_name: _Optional[str] = ..., reply_text: _Optional[str] = ..., reply_time_stamp: _Optional[int] = ..., author: _Optional[_Union[ReviewAuthor, _Mapping]] = ..., user_profile: _Optional[_Union[UserProfile, _Mapping]] = ..., sentiment: _Optional[_Union[Image, _Mapping]] = ..., helpful_count: _Optional[int] = ..., thumbs_up_count: _Optional[int] = ...) -> None: ...

class CriticReviewsResponse(_message.Message):
    __slots__ = ("title", "image", "total_num_reviews", "percent_favorable", "source_text", "source", "review")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FAVORABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    title: str
    image: Image
    total_num_reviews: int
    percent_favorable: int
    source_text: str
    source: Link
    review: _containers.RepeatedCompositeFieldContainer[Review]
    def __init__(self, title: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., total_num_reviews: _Optional[int] = ..., percent_favorable: _Optional[int] = ..., source_text: _Optional[str] = ..., source: _Optional[_Union[Link, _Mapping]] = ..., review: _Optional[_Iterable[_Union[Review, _Mapping]]] = ...) -> None: ...

class ReviewAuthor(_message.Message):
    __slots__ = ("name", "avatar")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar: Image
    def __init__(self, name: _Optional[str] = ..., avatar: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class UserProfile(_message.Message):
    __slots__ = ("profile_id", "person_id", "profile_type", "person_type", "name", "image", "profile_url", "profile_description")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSON_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    person_id: str
    profile_type: int
    person_type: int
    name: str
    image: _containers.RepeatedCompositeFieldContainer[Image]
    profile_url: str
    profile_description: str
    def __init__(self, profile_id: _Optional[str] = ..., person_id: _Optional[str] = ..., profile_type: _Optional[int] = ..., person_type: _Optional[int] = ..., name: _Optional[str] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., profile_url: _Optional[str] = ..., profile_description: _Optional[str] = ...) -> None: ...

class ReviewResponse(_message.Message):
    __slots__ = ("user_reviews_response", "next_page_url", "user_review", "suggestions_list_url", "critic_reviews_response")
    USER_REVIEWS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    USER_REVIEW_FIELD_NUMBER: _ClassVar[int]
    SUGGESTIONS_LIST_URL_FIELD_NUMBER: _ClassVar[int]
    CRITIC_REVIEWS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    user_reviews_response: GetReviewsResponse
    next_page_url: str
    user_review: Review
    suggestions_list_url: str
    critic_reviews_response: CriticReviewsResponse
    def __init__(self, user_reviews_response: _Optional[_Union[GetReviewsResponse, _Mapping]] = ..., next_page_url: _Optional[str] = ..., user_review: _Optional[_Union[Review, _Mapping]] = ..., suggestions_list_url: _Optional[str] = ..., critic_reviews_response: _Optional[_Union[CriticReviewsResponse, _Mapping]] = ...) -> None: ...

class RelatedSearch(_message.Message):
    __slots__ = ("search_url", "header", "backend_id", "doc_type", "current")
    SEARCH_URL_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ID_FIELD_NUMBER: _ClassVar[int]
    DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    search_url: str
    header: str
    backend_id: int
    doc_type: int
    current: bool
    def __init__(self, search_url: _Optional[str] = ..., header: _Optional[str] = ..., backend_id: _Optional[int] = ..., doc_type: _Optional[int] = ..., current: _Optional[bool] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("original_query", "suggested_query", "aggregate_query", "bucket", "item", "related_search", "server_logs_cookie", "full_page_replaced", "contains_snow", "next_page_url")
    ORIGINAL_QUERY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_QUERY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    RELATED_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    FULL_PAGE_REPLACED_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_SNOW_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    original_query: str
    suggested_query: str
    aggregate_query: bool
    bucket: _containers.RepeatedCompositeFieldContainer[Bucket]
    item: _containers.RepeatedCompositeFieldContainer[Item]
    related_search: _containers.RepeatedCompositeFieldContainer[RelatedSearch]
    server_logs_cookie: bytes
    full_page_replaced: bool
    contains_snow: bool
    next_page_url: str
    def __init__(self, original_query: _Optional[str] = ..., suggested_query: _Optional[str] = ..., aggregate_query: _Optional[bool] = ..., bucket: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., item: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., related_search: _Optional[_Iterable[_Union[RelatedSearch, _Mapping]]] = ..., server_logs_cookie: _Optional[bytes] = ..., full_page_replaced: _Optional[bool] = ..., contains_snow: _Optional[bool] = ..., next_page_url: _Optional[str] = ...) -> None: ...

class SearchSuggestResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[SearchSuggestEntry]
    def __init__(self, entry: _Optional[_Iterable[_Union[SearchSuggestEntry, _Mapping]]] = ...) -> None: ...

class SearchSuggestEntry(_message.Message):
    __slots__ = ("type", "suggested_query", "image_container", "title", "package_name_container")
    class ImageContainer(_message.Message):
        __slots__ = ("image_url",)
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        image_url: str
        def __init__(self, image_url: _Optional[str] = ...) -> None: ...
    class PackageNameContainer(_message.Message):
        __slots__ = ("package_name",)
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        package_name: str
        def __init__(self, package_name: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    type: int
    suggested_query: str
    image_container: SearchSuggestEntry.ImageContainer
    title: str
    package_name_container: SearchSuggestEntry.PackageNameContainer
    def __init__(self, type: _Optional[int] = ..., suggested_query: _Optional[str] = ..., image_container: _Optional[_Union[SearchSuggestEntry.ImageContainer, _Mapping]] = ..., title: _Optional[str] = ..., package_name_container: _Optional[_Union[SearchSuggestEntry.PackageNameContainer, _Mapping]] = ...) -> None: ...

class TestingProgramResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: TestingProgramResult
    def __init__(self, result: _Optional[_Union[TestingProgramResult, _Mapping]] = ...) -> None: ...

class TestingProgramResult(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: TestingProgramDetails
    def __init__(self, details: _Optional[_Union[TestingProgramDetails, _Mapping]] = ...) -> None: ...

class TestingProgramDetails(_message.Message):
    __slots__ = ("subscribed", "id", "unsubscribed")
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    subscribed: bool
    id: int
    unsubscribed: bool
    def __init__(self, subscribed: _Optional[bool] = ..., id: _Optional[int] = ..., unsubscribed: _Optional[bool] = ...) -> None: ...

class LogRequest(_message.Message):
    __slots__ = ("timestamp", "download_confirmation_query")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONFIRMATION_QUERY_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    download_confirmation_query: str
    def __init__(self, timestamp: _Optional[int] = ..., download_confirmation_query: _Optional[str] = ...) -> None: ...

class TestingProgramRequest(_message.Message):
    __slots__ = ("package_name", "subscribe")
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    subscribe: bool
    def __init__(self, package_name: _Optional[str] = ..., subscribe: _Optional[bool] = ...) -> None: ...

class UploadDeviceConfigRequest(_message.Message):
    __slots__ = ("device_configuration", "manufacturer", "gcm_registration_id")
    DEVICE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    GCM_REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    device_configuration: DeviceConfigurationProto
    manufacturer: str
    gcm_registration_id: str
    def __init__(self, device_configuration: _Optional[_Union[DeviceConfigurationProto, _Mapping]] = ..., manufacturer: _Optional[str] = ..., gcm_registration_id: _Optional[str] = ...) -> None: ...

class UploadDeviceConfigResponse(_message.Message):
    __slots__ = ("upload_device_config_token",)
    UPLOAD_DEVICE_CONFIG_TOKEN_FIELD_NUMBER: _ClassVar[int]
    upload_device_config_token: str
    def __init__(self, upload_device_config_token: _Optional[str] = ...) -> None: ...

class AndroidCheckinRequest(_message.Message):
    __slots__ = ("imei", "id", "digest", "checkin", "desired_build", "locale", "logging_id", "market_checkin", "mac_addr", "meid", "account_cookie", "time_zone", "security_token", "version", "ota_cert", "serial_number", "esn", "device_configuration", "mac_addr_type", "fragment", "user_name", "user_serial_number")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    CHECKIN_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BUILD_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    LOGGING_ID_FIELD_NUMBER: _ClassVar[int]
    MARKET_CHECKIN_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDR_FIELD_NUMBER: _ClassVar[int]
    MEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OTA_CERT_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ESN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDR_TYPE_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    imei: str
    id: int
    digest: str
    checkin: AndroidCheckinProto
    desired_build: str
    locale: str
    logging_id: int
    market_checkin: str
    mac_addr: _containers.RepeatedScalarFieldContainer[str]
    meid: str
    account_cookie: _containers.RepeatedScalarFieldContainer[str]
    time_zone: str
    security_token: int
    version: int
    ota_cert: _containers.RepeatedScalarFieldContainer[str]
    serial_number: str
    esn: str
    device_configuration: DeviceConfigurationProto
    mac_addr_type: _containers.RepeatedScalarFieldContainer[str]
    fragment: int
    user_name: str
    user_serial_number: int
    def __init__(self, imei: _Optional[str] = ..., id: _Optional[int] = ..., digest: _Optional[str] = ..., checkin: _Optional[_Union[AndroidCheckinProto, _Mapping]] = ..., desired_build: _Optional[str] = ..., locale: _Optional[str] = ..., logging_id: _Optional[int] = ..., market_checkin: _Optional[str] = ..., mac_addr: _Optional[_Iterable[str]] = ..., meid: _Optional[str] = ..., account_cookie: _Optional[_Iterable[str]] = ..., time_zone: _Optional[str] = ..., security_token: _Optional[int] = ..., version: _Optional[int] = ..., ota_cert: _Optional[_Iterable[str]] = ..., serial_number: _Optional[str] = ..., esn: _Optional[str] = ..., device_configuration: _Optional[_Union[DeviceConfigurationProto, _Mapping]] = ..., mac_addr_type: _Optional[_Iterable[str]] = ..., fragment: _Optional[int] = ..., user_name: _Optional[str] = ..., user_serial_number: _Optional[int] = ...) -> None: ...

class AndroidCheckinResponse(_message.Message):
    __slots__ = ("stats_ok", "intent", "time_msec", "digest", "setting", "market_ok", "android_id", "security_token", "settings_diff", "delete_setting", "device_checkin_consistency_token")
    STATS_OK_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    TIME_MSEC_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    SETTING_FIELD_NUMBER: _ClassVar[int]
    MARKET_OK_FIELD_NUMBER: _ClassVar[int]
    ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_DIFF_FIELD_NUMBER: _ClassVar[int]
    DELETE_SETTING_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CHECKIN_CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    stats_ok: bool
    intent: _containers.RepeatedCompositeFieldContainer[AndroidIntentProto]
    time_msec: int
    digest: str
    setting: _containers.RepeatedCompositeFieldContainer[GservicesSetting]
    market_ok: bool
    android_id: int
    security_token: int
    settings_diff: bool
    delete_setting: _containers.RepeatedScalarFieldContainer[str]
    device_checkin_consistency_token: str
    def __init__(self, stats_ok: _Optional[bool] = ..., intent: _Optional[_Iterable[_Union[AndroidIntentProto, _Mapping]]] = ..., time_msec: _Optional[int] = ..., digest: _Optional[str] = ..., setting: _Optional[_Iterable[_Union[GservicesSetting, _Mapping]]] = ..., market_ok: _Optional[bool] = ..., android_id: _Optional[int] = ..., security_token: _Optional[int] = ..., settings_diff: _Optional[bool] = ..., delete_setting: _Optional[_Iterable[str]] = ..., device_checkin_consistency_token: _Optional[str] = ...) -> None: ...

class GservicesSetting(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    value: bytes
    def __init__(self, name: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class AndroidBuildProto(_message.Message):
    __slots__ = ("id", "product", "carrier", "radio", "bootloader", "client", "timestamp", "google_services", "device", "sdk_version", "model", "manufacturer", "build_product", "ota_installed")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    RADIO_FIELD_NUMBER: _ClassVar[int]
    BOOTLOADER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    BUILD_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    OTA_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    product: str
    carrier: str
    radio: str
    bootloader: str
    client: str
    timestamp: int
    google_services: int
    device: str
    sdk_version: int
    model: str
    manufacturer: str
    build_product: str
    ota_installed: bool
    def __init__(self, id: _Optional[str] = ..., product: _Optional[str] = ..., carrier: _Optional[str] = ..., radio: _Optional[str] = ..., bootloader: _Optional[str] = ..., client: _Optional[str] = ..., timestamp: _Optional[int] = ..., google_services: _Optional[int] = ..., device: _Optional[str] = ..., sdk_version: _Optional[int] = ..., model: _Optional[str] = ..., manufacturer: _Optional[str] = ..., build_product: _Optional[str] = ..., ota_installed: _Optional[bool] = ...) -> None: ...

class AndroidCheckinProto(_message.Message):
    __slots__ = ("build", "last_checkin_msec", "event", "stat", "requested_group", "cell_operator", "sim_operator", "roaming", "user_number")
    BUILD_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKIN_MSEC_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_GROUP_FIELD_NUMBER: _ClassVar[int]
    CELL_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    SIM_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    ROAMING_FIELD_NUMBER: _ClassVar[int]
    USER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    build: AndroidBuildProto
    last_checkin_msec: int
    event: _containers.RepeatedCompositeFieldContainer[AndroidEventProto]
    stat: _containers.RepeatedCompositeFieldContainer[AndroidStatisticProto]
    requested_group: _containers.RepeatedScalarFieldContainer[str]
    cell_operator: str
    sim_operator: str
    roaming: str
    user_number: int
    def __init__(self, build: _Optional[_Union[AndroidBuildProto, _Mapping]] = ..., last_checkin_msec: _Optional[int] = ..., event: _Optional[_Iterable[_Union[AndroidEventProto, _Mapping]]] = ..., stat: _Optional[_Iterable[_Union[AndroidStatisticProto, _Mapping]]] = ..., requested_group: _Optional[_Iterable[str]] = ..., cell_operator: _Optional[str] = ..., sim_operator: _Optional[str] = ..., roaming: _Optional[str] = ..., user_number: _Optional[int] = ...) -> None: ...

class AndroidEventProto(_message.Message):
    __slots__ = ("tag", "value", "time_msec")
    TAG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIME_MSEC_FIELD_NUMBER: _ClassVar[int]
    tag: str
    value: str
    time_msec: int
    def __init__(self, tag: _Optional[str] = ..., value: _Optional[str] = ..., time_msec: _Optional[int] = ...) -> None: ...

class AndroidIntentProto(_message.Message):
    __slots__ = ("action", "data_uri", "mime_type", "java_class", "extra")
    class Extra(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DATA_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    JAVA_CLASS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    action: str
    data_uri: str
    mime_type: str
    java_class: str
    extra: _containers.RepeatedCompositeFieldContainer[AndroidIntentProto.Extra]
    def __init__(self, action: _Optional[str] = ..., data_uri: _Optional[str] = ..., mime_type: _Optional[str] = ..., java_class: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[AndroidIntentProto.Extra, _Mapping]]] = ...) -> None: ...

class AndroidStatisticProto(_message.Message):
    __slots__ = ("tag", "count", "sum")
    TAG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    tag: str
    count: int
    sum: float
    def __init__(self, tag: _Optional[str] = ..., count: _Optional[int] = ..., sum: _Optional[float] = ...) -> None: ...

class ClientLibraryState(_message.Message):
    __slots__ = ("corpus", "server_token", "hash_code_sum", "library_size", "library_id")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HASH_CODE_SUM_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_SIZE_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    corpus: int
    server_token: bytes
    hash_code_sum: int
    library_size: int
    library_id: str
    def __init__(self, corpus: _Optional[int] = ..., server_token: _Optional[bytes] = ..., hash_code_sum: _Optional[int] = ..., library_size: _Optional[int] = ..., library_id: _Optional[str] = ...) -> None: ...

class AndroidDataUsageProto(_message.Message):
    __slots__ = ("version", "current_report_msec", "key_to_package_name_mapping", "payload_level_app_stat", "ip_layer_network_stat")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REPORT_MSEC_FIELD_NUMBER: _ClassVar[int]
    KEY_TO_PACKAGE_NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_LEVEL_APP_STAT_FIELD_NUMBER: _ClassVar[int]
    IP_LAYER_NETWORK_STAT_FIELD_NUMBER: _ClassVar[int]
    version: int
    current_report_msec: int
    key_to_package_name_mapping: _containers.RepeatedCompositeFieldContainer[KeyToPackageNameMapping]
    payload_level_app_stat: _containers.RepeatedCompositeFieldContainer[PayloadLevelAppStat]
    ip_layer_network_stat: _containers.RepeatedCompositeFieldContainer[IpLayerNetworkStat]
    def __init__(self, version: _Optional[int] = ..., current_report_msec: _Optional[int] = ..., key_to_package_name_mapping: _Optional[_Iterable[_Union[KeyToPackageNameMapping, _Mapping]]] = ..., payload_level_app_stat: _Optional[_Iterable[_Union[PayloadLevelAppStat, _Mapping]]] = ..., ip_layer_network_stat: _Optional[_Iterable[_Union[IpLayerNetworkStat, _Mapping]]] = ...) -> None: ...

class AndroidUsageStatsReport(_message.Message):
    __slots__ = ("android_id", "logging_id", "usage_stats")
    ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
    LOGGING_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_STATS_FIELD_NUMBER: _ClassVar[int]
    android_id: int
    logging_id: int
    usage_stats: UsageStatsExtensionProto
    def __init__(self, android_id: _Optional[int] = ..., logging_id: _Optional[int] = ..., usage_stats: _Optional[_Union[UsageStatsExtensionProto, _Mapping]] = ...) -> None: ...

class AppBucket(_message.Message):
    __slots__ = ("bucket_start_msec", "bucket_duration_msec", "stat_counters", "operation_count")
    BUCKET_START_MSEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_DURATION_MSEC_FIELD_NUMBER: _ClassVar[int]
    STAT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    bucket_start_msec: int
    bucket_duration_msec: int
    stat_counters: _containers.RepeatedCompositeFieldContainer[StatCounters]
    operation_count: int
    def __init__(self, bucket_start_msec: _Optional[int] = ..., bucket_duration_msec: _Optional[int] = ..., stat_counters: _Optional[_Iterable[_Union[StatCounters, _Mapping]]] = ..., operation_count: _Optional[int] = ...) -> None: ...

class CounterData(_message.Message):
    __slots__ = ("bytes", "packets")
    BYTES_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    bytes: int
    packets: int
    def __init__(self, bytes: _Optional[int] = ..., packets: _Optional[int] = ...) -> None: ...

class IpLayerAppStat(_message.Message):
    __slots__ = ("package_key", "application_tag", "ip_layer_app_bucket")
    PACKAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TAG_FIELD_NUMBER: _ClassVar[int]
    IP_LAYER_APP_BUCKET_FIELD_NUMBER: _ClassVar[int]
    package_key: int
    application_tag: int
    ip_layer_app_bucket: _containers.RepeatedCompositeFieldContainer[AppBucket]
    def __init__(self, package_key: _Optional[int] = ..., application_tag: _Optional[int] = ..., ip_layer_app_bucket: _Optional[_Iterable[_Union[AppBucket, _Mapping]]] = ...) -> None: ...

class IpLayerNetworkBucket(_message.Message):
    __slots__ = ("bucket_start_msec", "bucket_duration_msec", "stat_counters", "network_active_duration")
    BUCKET_START_MSEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_DURATION_MSEC_FIELD_NUMBER: _ClassVar[int]
    STAT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ACTIVE_DURATION_FIELD_NUMBER: _ClassVar[int]
    bucket_start_msec: int
    bucket_duration_msec: int
    stat_counters: _containers.RepeatedCompositeFieldContainer[StatCounters]
    network_active_duration: int
    def __init__(self, bucket_start_msec: _Optional[int] = ..., bucket_duration_msec: _Optional[int] = ..., stat_counters: _Optional[_Iterable[_Union[StatCounters, _Mapping]]] = ..., network_active_duration: _Optional[int] = ...) -> None: ...

class IpLayerNetworkStat(_message.Message):
    __slots__ = ("network_details", "type", "ip_layer_network_bucket", "ip_layer_app_stat")
    NETWORK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_LAYER_NETWORK_BUCKET_FIELD_NUMBER: _ClassVar[int]
    IP_LAYER_APP_STAT_FIELD_NUMBER: _ClassVar[int]
    network_details: str
    type: int
    ip_layer_network_bucket: _containers.RepeatedCompositeFieldContainer[IpLayerNetworkBucket]
    ip_layer_app_stat: _containers.RepeatedCompositeFieldContainer[IpLayerAppStat]
    def __init__(self, network_details: _Optional[str] = ..., type: _Optional[int] = ..., ip_layer_network_bucket: _Optional[_Iterable[_Union[IpLayerNetworkBucket, _Mapping]]] = ..., ip_layer_app_stat: _Optional[_Iterable[_Union[IpLayerAppStat, _Mapping]]] = ...) -> None: ...

class KeyToPackageNameMapping(_message.Message):
    __slots__ = ("package_key", "uid_name", "shared_package")
    PACKAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    UID_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package_key: int
    uid_name: str
    shared_package: _containers.RepeatedCompositeFieldContainer[PackageInfo]
    def __init__(self, package_key: _Optional[int] = ..., uid_name: _Optional[str] = ..., shared_package: _Optional[_Iterable[_Union[PackageInfo, _Mapping]]] = ...) -> None: ...

class PackageInfo(_message.Message):
    __slots__ = ("pkg_name", "version_code")
    PKG_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    pkg_name: str
    version_code: int
    def __init__(self, pkg_name: _Optional[str] = ..., version_code: _Optional[int] = ...) -> None: ...

class PayloadLevelAppStat(_message.Message):
    __slots__ = ("package_key", "application_tag", "payload_level_app_bucket")
    PACKAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TAG_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_LEVEL_APP_BUCKET_FIELD_NUMBER: _ClassVar[int]
    package_key: int
    application_tag: int
    payload_level_app_bucket: _containers.RepeatedCompositeFieldContainer[AppBucket]
    def __init__(self, package_key: _Optional[int] = ..., application_tag: _Optional[int] = ..., payload_level_app_bucket: _Optional[_Iterable[_Union[AppBucket, _Mapping]]] = ...) -> None: ...

class StatCounters(_message.Message):
    __slots__ = ("network_proto", "direction", "counter_data", "fg_bg")
    NETWORK_PROTO_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    COUNTER_DATA_FIELD_NUMBER: _ClassVar[int]
    FG_BG_FIELD_NUMBER: _ClassVar[int]
    network_proto: int
    direction: int
    counter_data: CounterData
    fg_bg: int
    def __init__(self, network_proto: _Optional[int] = ..., direction: _Optional[int] = ..., counter_data: _Optional[_Union[CounterData, _Mapping]] = ..., fg_bg: _Optional[int] = ...) -> None: ...

class UsageStatsExtensionProto(_message.Message):
    __slots__ = ("data_usage",)
    DATA_USAGE_FIELD_NUMBER: _ClassVar[int]
    data_usage: AndroidDataUsageProto
    def __init__(self, data_usage: _Optional[_Union[AndroidDataUsageProto, _Mapping]] = ...) -> None: ...

class ModifyLibraryRequest(_message.Message):
    __slots__ = ("library_id", "add_package_name", "remove_package_name")
    LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    library_id: str
    add_package_name: _containers.RepeatedScalarFieldContainer[str]
    remove_package_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, library_id: _Optional[str] = ..., add_package_name: _Optional[_Iterable[str]] = ..., remove_package_name: _Optional[_Iterable[str]] = ...) -> None: ...

class ServerResponse(_message.Message):
    __slots__ = ("error",)
    class Error(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ServerResponse.Error
    def __init__(self, error: _Optional[_Union[ServerResponse.Error, _Mapping]] = ...) -> None: ...
