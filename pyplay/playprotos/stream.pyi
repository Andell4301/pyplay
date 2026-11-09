from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamResponse(_message.Message):
    __slots__ = ("item", "tree")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[ItemResponse.Item]
    tree: StreamTree
    def __init__(self, item: _Optional[_Iterable[_Union[ItemResponse.Item, _Mapping]]] = ..., tree: _Optional[_Union[StreamTree, _Mapping]] = ...) -> None: ...

class StreamTree(_message.Message):
    __slots__ = ("page", "node")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    page: _containers.RepeatedCompositeFieldContainer[StreamPage]
    node: _containers.RepeatedCompositeFieldContainer[StreamNode]
    def __init__(self, page: _Optional[_Iterable[_Union[StreamPage, _Mapping]]] = ..., node: _Optional[_Iterable[_Union[StreamNode, _Mapping]]] = ...) -> None: ...

class StreamPage(_message.Message):
    __slots__ = ("key", "content")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    key: StreamPageKey
    content: StreamPageContent
    def __init__(self, key: _Optional[_Union[StreamPageKey, _Mapping]] = ..., content: _Optional[_Union[StreamPageContent, _Mapping]] = ...) -> None: ...

class StreamPageKey(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class StreamPageContent(_message.Message):
    __slots__ = ("children",)
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: StreamChildren
    def __init__(self, children: _Optional[_Union[StreamChildren, _Mapping]] = ...) -> None: ...

class StreamChildren(_message.Message):
    __slots__ = ("key", "next_page_token")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    key: _containers.RepeatedCompositeFieldContainer[StreamNodeKey]
    next_page_token: str
    def __init__(self, key: _Optional[_Iterable[_Union[StreamNodeKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class StreamNodeKey(_message.Message):
    __slots__ = ("url", "id")
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    id: str
    def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class StreamNode(_message.Message):
    __slots__ = ("key", "content")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    key: StreamNodeKey
    content: StreamNodeContent
    def __init__(self, key: _Optional[_Union[StreamNodeKey, _Mapping]] = ..., content: _Optional[_Union[StreamNodeContent, _Mapping]] = ...) -> None: ...

class StreamNodeContent(_message.Message):
    __slots__ = ("element", "children", "item")
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    element: StreamElement
    children: StreamChildren
    item: StreamItemRef
    def __init__(self, element: _Optional[_Union[StreamElement, _Mapping]] = ..., children: _Optional[_Union[StreamChildren, _Mapping]] = ..., item: _Optional[_Union[StreamItemRef, _Mapping]] = ...) -> None: ...

class StreamItemRef(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: StreamItemKey
    def __init__(self, key: _Optional[_Union[StreamItemKey, _Mapping]] = ...) -> None: ...

class StreamItemKey(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: StringWrapper
    def __init__(self, id: _Optional[_Union[StringWrapper, _Mapping]] = ...) -> None: ...

class StreamElement(_message.Message):
    __slots__ = ("module",)
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: StreamModule
    def __init__(self, module: _Optional[_Union[StreamModule, _Mapping]] = ...) -> None: ...

class StreamModule(_message.Message):
    __slots__ = ("cluster", "developer_header", "text")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_HEADER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    cluster: ClusterModule
    developer_header: DeveloperHeaderModule
    text: TextModule
    def __init__(self, cluster: _Optional[_Union[ClusterModule, _Mapping]] = ..., developer_header: _Optional[_Union[DeveloperHeaderModule, _Mapping]] = ..., text: _Optional[_Union[TextModule, _Mapping]] = ...) -> None: ...

class ModuleHeader(_message.Message):
    __slots__ = ("title", "subtitle", "image", "link")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    image: ItemResponse.Image.Metadata
    link: ModuleLink
    def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., link: _Optional[_Union[ModuleLink, _Mapping]] = ...) -> None: ...

class ModuleLink(_message.Message):
    __slots__ = ("browse",)
    BROWSE_FIELD_NUMBER: _ClassVar[int]
    browse: StreamBrowseLink
    def __init__(self, browse: _Optional[_Union[StreamBrowseLink, _Mapping]] = ...) -> None: ...

class StreamBrowseLink(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class ClusterModule(_message.Message):
    __slots__ = ("title", "subtitle", "link", "header")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    link: ModuleLink
    header: ModuleHeader
    def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., link: _Optional[_Union[ModuleLink, _Mapping]] = ..., header: _Optional[_Union[ModuleHeader, _Mapping]] = ...) -> None: ...

class DeveloperHeaderModule(_message.Message):
    __slots__ = ("title", "icon", "cover_image", "cover_media")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COVER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    COVER_MEDIA_FIELD_NUMBER: _ClassVar[int]
    title: str
    icon: ItemResponse.Image.Metadata
    cover_image: ItemResponse.Image.Metadata
    cover_media: CoverMedia
    def __init__(self, title: _Optional[str] = ..., icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., cover_image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., cover_media: _Optional[_Union[CoverMedia, _Mapping]] = ...) -> None: ...

class CoverMedia(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: ItemResponse.Image.Metadata
    def __init__(self, image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...

class TextModule(_message.Message):
    __slots__ = ("header", "text", "formatted_text")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_TEXT_FIELD_NUMBER: _ClassVar[int]
    header: ModuleHeader
    text: str
    formatted_text: FormattedText
    def __init__(self, header: _Optional[_Union[ModuleHeader, _Mapping]] = ..., text: _Optional[str] = ..., formatted_text: _Optional[_Union[FormattedText, _Mapping]] = ...) -> None: ...

class FormattedText(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ItemResponse(_message.Message):
    __slots__ = ("item",)
    class Image(_message.Message):
        __slots__ = ("metadata",)
        class Metadata(_message.Message):
            __slots__ = ("unknown2", "dimensions", "metadata")
            class Dimensions(_message.Message):
                __slots__ = ("height", "width")
                HEIGHT_FIELD_NUMBER: _ClassVar[int]
                WIDTH_FIELD_NUMBER: _ClassVar[int]
                height: int
                width: int
                def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...
            class MetadataEntry(_message.Message):
                __slots__ = ("url", "primary_color")
                class Color(_message.Message):
                    __slots__ = ("R", "G", "B", "A")
                    R_FIELD_NUMBER: _ClassVar[int]
                    G_FIELD_NUMBER: _ClassVar[int]
                    B_FIELD_NUMBER: _ClassVar[int]
                    A_FIELD_NUMBER: _ClassVar[int]
                    R: int
                    G: int
                    B: int
                    A: int
                    def __init__(self, R: _Optional[int] = ..., G: _Optional[int] = ..., B: _Optional[int] = ..., A: _Optional[int] = ...) -> None: ...
                URL_FIELD_NUMBER: _ClassVar[int]
                PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
                url: str
                primary_color: ItemResponse.Image.Metadata.MetadataEntry.Color
                def __init__(self, url: _Optional[str] = ..., primary_color: _Optional[_Union[ItemResponse.Image.Metadata.MetadataEntry.Color, _Mapping]] = ...) -> None: ...
            UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
            DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
            METADATA_FIELD_NUMBER: _ClassVar[int]
            unknown2: int
            dimensions: ItemResponse.Image.Metadata.Dimensions
            metadata: ItemResponse.Image.Metadata.MetadataEntry
            def __init__(self, unknown2: _Optional[int] = ..., dimensions: _Optional[_Union[ItemResponse.Image.Metadata.Dimensions, _Mapping]] = ..., metadata: _Optional[_Union[ItemResponse.Image.Metadata.MetadataEntry, _Mapping]] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        metadata: _containers.RepeatedCompositeFieldContainer[ItemResponse.Image.Metadata]
        def __init__(self, metadata: _Optional[_Iterable[_Union[ItemResponse.Image.Metadata, _Mapping]]] = ...) -> None: ...
    class DeveloperInfo(_message.Message):
        __slots__ = ("email", "website", "metadata")
        class Metadata(_message.Message):
            __slots__ = ("name", "support_email", "address", "phone")
            NAME_FIELD_NUMBER: _ClassVar[int]
            SUPPORT_EMAIL_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PHONE_FIELD_NUMBER: _ClassVar[int]
            name: str
            support_email: str
            address: str
            phone: str
            def __init__(self, name: _Optional[str] = ..., support_email: _Optional[str] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        email: str
        website: str
        metadata: ItemResponse.DeveloperInfo.Metadata
        def __init__(self, email: _Optional[str] = ..., website: _Optional[str] = ..., metadata: _Optional[_Union[ItemResponse.DeveloperInfo.Metadata, _Mapping]] = ...) -> None: ...
    class SubItem(_message.Message):
        __slots__ = ("type", "name", "package_name", "action")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        type: str
        name: str
        package_name: str
        action: str
        def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., package_name: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...
    class CertificateWrapper(_message.Message):
        __slots__ = ("certificate_set",)
        class CertificateSet(_message.Message):
            __slots__ = ("sha1", "sha256")
            SHA1_FIELD_NUMBER: _ClassVar[int]
            SHA256_FIELD_NUMBER: _ClassVar[int]
            sha1: str
            sha256: str
            def __init__(self, sha1: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...
        CERTIFICATE_SET_FIELD_NUMBER: _ClassVar[int]
        certificate_set: _containers.RepeatedCompositeFieldContainer[ItemResponse.CertificateWrapper.CertificateSet]
        def __init__(self, certificate_set: _Optional[_Iterable[_Union[ItemResponse.CertificateWrapper.CertificateSet, _Mapping]]] = ...) -> None: ...
    class ContentRating(_message.Message):
        __slots__ = ("title", "recommendation_and_description_html", "image", "image_alt", "recommendation", "description")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_AND_DESCRIPTION_HTML_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ALT_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        recommendation_and_description_html: str
        image: ItemResponse.Image.Metadata
        image_alt: ItemResponse.Image.Metadata
        recommendation: str
        description: str
        def __init__(self, title: _Optional[str] = ..., recommendation_and_description_html: _Optional[str] = ..., image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., image_alt: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., recommendation: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class Price(_message.Message):
        __slots__ = ("offer_wrapper",)
        class OfferWrapper(_message.Message):
            __slots__ = ("offer",)
            class Offer(_message.Message):
                __slots__ = ("offer_type", "amount", "buy_button", "checkout_required", "note")
                class OfferType(_message.Message):
                    __slots__ = ("type",)
                    TYPE_FIELD_NUMBER: _ClassVar[int]
                    type: int
                    def __init__(self, type: _Optional[int] = ...) -> None: ...
                class Amount(_message.Message):
                    __slots__ = ("money", "unknown3")
                    class Money(_message.Message):
                        __slots__ = ("micros", "formatted_amount")
                        MICROS_FIELD_NUMBER: _ClassVar[int]
                        FORMATTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
                        micros: int
                        formatted_amount: str
                        def __init__(self, micros: _Optional[int] = ..., formatted_amount: _Optional[str] = ...) -> None: ...
                    MONEY_FIELD_NUMBER: _ClassVar[int]
                    UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
                    money: ItemResponse.Price.OfferWrapper.Offer.Amount.Money
                    unknown3: int
                    def __init__(self, money: _Optional[_Union[ItemResponse.Price.OfferWrapper.Offer.Amount.Money, _Mapping]] = ..., unknown3: _Optional[int] = ...) -> None: ...
                class BuyButton(_message.Message):
                    __slots__ = ("label",)
                    LABEL_FIELD_NUMBER: _ClassVar[int]
                    label: str
                    def __init__(self, label: _Optional[str] = ...) -> None: ...
                class Note(_message.Message):
                    __slots__ = ("text",)
                    TEXT_FIELD_NUMBER: _ClassVar[int]
                    text: str
                    def __init__(self, text: _Optional[str] = ...) -> None: ...
                OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
                AMOUNT_FIELD_NUMBER: _ClassVar[int]
                BUY_BUTTON_FIELD_NUMBER: _ClassVar[int]
                CHECKOUT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
                NOTE_FIELD_NUMBER: _ClassVar[int]
                offer_type: ItemResponse.Price.OfferWrapper.Offer.OfferType
                amount: ItemResponse.Price.OfferWrapper.Offer.Amount
                buy_button: ItemResponse.Price.OfferWrapper.Offer.BuyButton
                checkout_required: bool
                note: ItemResponse.Price.OfferWrapper.Offer.Note
                def __init__(self, offer_type: _Optional[_Union[ItemResponse.Price.OfferWrapper.Offer.OfferType, _Mapping]] = ..., amount: _Optional[_Union[ItemResponse.Price.OfferWrapper.Offer.Amount, _Mapping]] = ..., buy_button: _Optional[_Union[ItemResponse.Price.OfferWrapper.Offer.BuyButton, _Mapping]] = ..., checkout_required: _Optional[bool] = ..., note: _Optional[_Union[ItemResponse.Price.OfferWrapper.Offer.Note, _Mapping]] = ...) -> None: ...
            OFFER_FIELD_NUMBER: _ClassVar[int]
            offer: _containers.RepeatedCompositeFieldContainer[ItemResponse.Price.OfferWrapper.Offer]
            def __init__(self, offer: _Optional[_Iterable[_Union[ItemResponse.Price.OfferWrapper.Offer, _Mapping]]] = ...) -> None: ...
        OFFER_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        offer_wrapper: ItemResponse.Price.OfferWrapper
        def __init__(self, offer_wrapper: _Optional[_Union[ItemResponse.Price.OfferWrapper, _Mapping]] = ...) -> None: ...
    class Rating(_message.Message):
        __slots__ = ("star_rating", "rating_count", "rating_one_star", "rating_two_star", "rating_three_star", "rating_four_star", "rating_five_star", "rating_label", "rating_count_label_abbreviated", "rating_count_label")
        STAR_RATING_FIELD_NUMBER: _ClassVar[int]
        RATING_COUNT_FIELD_NUMBER: _ClassVar[int]
        RATING_ONE_STAR_FIELD_NUMBER: _ClassVar[int]
        RATING_TWO_STAR_FIELD_NUMBER: _ClassVar[int]
        RATING_THREE_STAR_FIELD_NUMBER: _ClassVar[int]
        RATING_FOUR_STAR_FIELD_NUMBER: _ClassVar[int]
        RATING_FIVE_STAR_FIELD_NUMBER: _ClassVar[int]
        RATING_LABEL_FIELD_NUMBER: _ClassVar[int]
        RATING_COUNT_LABEL_ABBREVIATED_FIELD_NUMBER: _ClassVar[int]
        RATING_COUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
        star_rating: float
        rating_count: int
        rating_one_star: int
        rating_two_star: int
        rating_three_star: int
        rating_four_star: int
        rating_five_star: int
        rating_label: str
        rating_count_label_abbreviated: str
        rating_count_label: str
        def __init__(self, star_rating: _Optional[float] = ..., rating_count: _Optional[int] = ..., rating_one_star: _Optional[int] = ..., rating_two_star: _Optional[int] = ..., rating_three_star: _Optional[int] = ..., rating_four_star: _Optional[int] = ..., rating_five_star: _Optional[int] = ..., rating_label: _Optional[str] = ..., rating_count_label_abbreviated: _Optional[str] = ..., rating_count_label: _Optional[str] = ...) -> None: ...
    class Share(_message.Message):
        __slots__ = ("target",)
        class Target(_message.Message):
            __slots__ = ("play_store",)
            PLAY_STORE_FIELD_NUMBER: _ClassVar[int]
            play_store: UrlWrapper
            def __init__(self, play_store: _Optional[_Union[UrlWrapper, _Mapping]] = ...) -> None: ...
        TARGET_FIELD_NUMBER: _ClassVar[int]
        target: ItemResponse.Share.Target
        def __init__(self, target: _Optional[_Union[ItemResponse.Share.Target, _Mapping]] = ...) -> None: ...
    class PrivacyPolicy(_message.Message):
        __slots__ = ("target",)
        class Target(_message.Message):
            __slots__ = ("policy",)
            POLICY_FIELD_NUMBER: _ClassVar[int]
            policy: UrlWrapper
            def __init__(self, policy: _Optional[_Union[UrlWrapper, _Mapping]] = ...) -> None: ...
        TARGET_FIELD_NUMBER: _ClassVar[int]
        target: ItemResponse.PrivacyPolicy.Target
        def __init__(self, target: _Optional[_Union[ItemResponse.PrivacyPolicy.Target, _Mapping]] = ...) -> None: ...
    class FamilyBadge(_message.Message):
        __slots__ = ("age_label", "age_label_long", "description", "image", "state", "links")
        class Category(_message.Message):
            __slots__ = ("browse",)
            BROWSE_FIELD_NUMBER: _ClassVar[int]
            browse: UrlWrapper
            def __init__(self, browse: _Optional[_Union[UrlWrapper, _Mapping]] = ...) -> None: ...
        class Link(_message.Message):
            __slots__ = ("age_bucket", "category")
            AGE_BUCKET_FIELD_NUMBER: _ClassVar[int]
            CATEGORY_FIELD_NUMBER: _ClassVar[int]
            age_bucket: int
            category: ItemResponse.FamilyBadge.Category
            def __init__(self, age_bucket: _Optional[int] = ..., category: _Optional[_Union[ItemResponse.FamilyBadge.Category, _Mapping]] = ...) -> None: ...
        AGE_LABEL_FIELD_NUMBER: _ClassVar[int]
        AGE_LABEL_LONG_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        age_label: str
        age_label_long: str
        description: str
        image: ItemResponse.Image.Metadata
        state: int
        links: _containers.RepeatedCompositeFieldContainer[ItemResponse.FamilyBadge.Link]
        def __init__(self, age_label: _Optional[str] = ..., age_label_long: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., state: _Optional[int] = ..., links: _Optional[_Iterable[_Union[ItemResponse.FamilyBadge.Link, _Mapping]]] = ...) -> None: ...
    class DataSafetySummary(_message.Message):
        __slots__ = ("rows",)
        class Row(_message.Message):
            __slots__ = ("title", "subtitle", "icon")
            class Html(_message.Message):
                __slots__ = ("html",)
                HTML_FIELD_NUMBER: _ClassVar[int]
                html: str
                def __init__(self, html: _Optional[str] = ...) -> None: ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            ICON_FIELD_NUMBER: _ClassVar[int]
            title: str
            subtitle: ItemResponse.DataSafetySummary.Row.Html
            icon: ItemResponse.Image.Metadata
            def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[_Union[ItemResponse.DataSafetySummary.Row.Html, _Mapping]] = ..., icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
        ROWS_FIELD_NUMBER: _ClassVar[int]
        rows: _containers.RepeatedCompositeFieldContainer[ItemResponse.DataSafetySummary.Row]
        def __init__(self, rows: _Optional[_Iterable[_Union[ItemResponse.DataSafetySummary.Row, _Mapping]]] = ...) -> None: ...
    class DataSafety(_message.Message):
        __slots__ = ("learn_more", "sections", "security")
        class Html(_message.Message):
            __slots__ = ("html",)
            HTML_FIELD_NUMBER: _ClassVar[int]
            html: str
            def __init__(self, html: _Optional[str] = ...) -> None: ...
        class LearnMore(_message.Message):
            __slots__ = ("url",)
            URL_FIELD_NUMBER: _ClassVar[int]
            url: UrlWrapper
            def __init__(self, url: _Optional[_Union[UrlWrapper, _Mapping]] = ...) -> None: ...
        class Entry(_message.Message):
            __slots__ = ("header", "data")
            class Header(_message.Message):
                __slots__ = ("name", "summary", "icon")
                class Summary(_message.Message):
                    __slots__ = ("text",)
                    TEXT_FIELD_NUMBER: _ClassVar[int]
                    text: str
                    def __init__(self, text: _Optional[str] = ...) -> None: ...
                NAME_FIELD_NUMBER: _ClassVar[int]
                SUMMARY_FIELD_NUMBER: _ClassVar[int]
                ICON_FIELD_NUMBER: _ClassVar[int]
                name: str
                summary: ItemResponse.DataSafety.Entry.Header.Summary
                icon: ItemResponse.Image.Metadata
                def __init__(self, name: _Optional[str] = ..., summary: _Optional[_Union[ItemResponse.DataSafety.Entry.Header.Summary, _Mapping]] = ..., icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
            class DataPoint(_message.Message):
                __slots__ = ("name", "optional", "purposes")
                NAME_FIELD_NUMBER: _ClassVar[int]
                OPTIONAL_FIELD_NUMBER: _ClassVar[int]
                PURPOSES_FIELD_NUMBER: _ClassVar[int]
                name: str
                optional: int
                purposes: str
                def __init__(self, name: _Optional[str] = ..., optional: _Optional[int] = ..., purposes: _Optional[str] = ...) -> None: ...
            HEADER_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            header: ItemResponse.DataSafety.Entry.Header
            data: _containers.RepeatedCompositeFieldContainer[ItemResponse.DataSafety.Entry.DataPoint]
            def __init__(self, header: _Optional[_Union[ItemResponse.DataSafety.Entry.Header, _Mapping]] = ..., data: _Optional[_Iterable[_Union[ItemResponse.DataSafety.Entry.DataPoint, _Mapping]]] = ...) -> None: ...
        class Section(_message.Message):
            __slots__ = ("entries", "title", "subtitle", "icon", "description")
            ENTRIES_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            ICON_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            entries: _containers.RepeatedCompositeFieldContainer[ItemResponse.DataSafety.Entry]
            title: str
            subtitle: str
            icon: ItemResponse.Image.Metadata
            description: ItemResponse.DataSafety.Html
            def __init__(self, entries: _Optional[_Iterable[_Union[ItemResponse.DataSafety.Entry, _Mapping]]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., description: _Optional[_Union[ItemResponse.DataSafety.Html, _Mapping]] = ...) -> None: ...
        class Sections(_message.Message):
            __slots__ = ("shared", "collected")
            SHARED_FIELD_NUMBER: _ClassVar[int]
            COLLECTED_FIELD_NUMBER: _ClassVar[int]
            shared: ItemResponse.DataSafety.Section
            collected: ItemResponse.DataSafety.Section
            def __init__(self, shared: _Optional[_Union[ItemResponse.DataSafety.Section, _Mapping]] = ..., collected: _Optional[_Union[ItemResponse.DataSafety.Section, _Mapping]] = ...) -> None: ...
        class Security(_message.Message):
            __slots__ = ("icon", "title", "practices")
            class Practice(_message.Message):
                __slots__ = ("title", "description", "icon")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                ICON_FIELD_NUMBER: _ClassVar[int]
                title: str
                description: ItemResponse.DataSafety.Html
                icon: ItemResponse.Image.Metadata
                def __init__(self, title: _Optional[str] = ..., description: _Optional[_Union[ItemResponse.DataSafety.Html, _Mapping]] = ..., icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
            ICON_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            PRACTICES_FIELD_NUMBER: _ClassVar[int]
            icon: ItemResponse.Image.Metadata
            title: str
            practices: _containers.RepeatedCompositeFieldContainer[ItemResponse.DataSafety.Security.Practice]
            def __init__(self, icon: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., title: _Optional[str] = ..., practices: _Optional[_Iterable[_Union[ItemResponse.DataSafety.Security.Practice, _Mapping]]] = ...) -> None: ...
        LEARN_MORE_FIELD_NUMBER: _ClassVar[int]
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_FIELD_NUMBER: _ClassVar[int]
        learn_more: ItemResponse.DataSafety.LearnMore
        sections: ItemResponse.DataSafety.Sections
        security: ItemResponse.DataSafety.Security
        def __init__(self, learn_more: _Optional[_Union[ItemResponse.DataSafety.LearnMore, _Mapping]] = ..., sections: _Optional[_Union[ItemResponse.DataSafety.Sections, _Mapping]] = ..., security: _Optional[_Union[ItemResponse.DataSafety.Security, _Mapping]] = ...) -> None: ...
    class FeaturedReviews(_message.Message):
        __slots__ = ("reviews",)
        class Review(_message.Message):
            __slots__ = ("star_rating", "comment", "timestamp", "review_url", "author", "reply")
            class Author(_message.Message):
                __slots__ = ("avatar", "name")
                AVATAR_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                avatar: ItemResponse.Image.Metadata
                name: str
                def __init__(self, avatar: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
            class Reply(_message.Message):
                __slots__ = ("text", "timestamp")
                TEXT_FIELD_NUMBER: _ClassVar[int]
                TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
                text: str
                timestamp: Timestamp
                def __init__(self, text: _Optional[str] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...
            STAR_RATING_FIELD_NUMBER: _ClassVar[int]
            COMMENT_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            REVIEW_URL_FIELD_NUMBER: _ClassVar[int]
            AUTHOR_FIELD_NUMBER: _ClassVar[int]
            REPLY_FIELD_NUMBER: _ClassVar[int]
            star_rating: int
            comment: str
            timestamp: Timestamp
            review_url: str
            author: ItemResponse.FeaturedReviews.Review.Author
            reply: ItemResponse.FeaturedReviews.Review.Reply
            def __init__(self, star_rating: _Optional[int] = ..., comment: _Optional[str] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ..., review_url: _Optional[str] = ..., author: _Optional[_Union[ItemResponse.FeaturedReviews.Review.Author, _Mapping]] = ..., reply: _Optional[_Union[ItemResponse.FeaturedReviews.Review.Reply, _Mapping]] = ...) -> None: ...
        REVIEWS_FIELD_NUMBER: _ClassVar[int]
        reviews: _containers.RepeatedCompositeFieldContainer[ItemResponse.FeaturedReviews.Review]
        def __init__(self, reviews: _Optional[_Iterable[_Union[ItemResponse.FeaturedReviews.Review, _Mapping]]] = ...) -> None: ...
    class ReviewTips(_message.Message):
        __slots__ = ("tips",)
        class Tip(_message.Message):
            __slots__ = ("id", "text", "polarity", "review_count_label")
            class Id(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: str
                def __init__(self, id: _Optional[str] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            POLARITY_FIELD_NUMBER: _ClassVar[int]
            REVIEW_COUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
            id: ItemResponse.ReviewTips.Tip.Id
            text: str
            polarity: int
            review_count_label: str
            def __init__(self, id: _Optional[_Union[ItemResponse.ReviewTips.Tip.Id, _Mapping]] = ..., text: _Optional[str] = ..., polarity: _Optional[int] = ..., review_count_label: _Optional[str] = ...) -> None: ...
        TIPS_FIELD_NUMBER: _ClassVar[int]
        tips: _containers.RepeatedCompositeFieldContainer[ItemResponse.ReviewTips.Tip]
        def __init__(self, tips: _Optional[_Iterable[_Union[ItemResponse.ReviewTips.Tip, _Mapping]]] = ...) -> None: ...
    class AppFeatures(_message.Message):
        __slots__ = ("groups",)
        class Feature(_message.Message):
            __slots__ = ("title", "description")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            title: str
            description: str
            def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
        class Group(_message.Message):
            __slots__ = ("query", "features")
            QUERY_FIELD_NUMBER: _ClassVar[int]
            FEATURES_FIELD_NUMBER: _ClassVar[int]
            query: str
            features: _containers.RepeatedCompositeFieldContainer[ItemResponse.AppFeatures.Feature]
            def __init__(self, query: _Optional[str] = ..., features: _Optional[_Iterable[_Union[ItemResponse.AppFeatures.Feature, _Mapping]]] = ...) -> None: ...
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[ItemResponse.AppFeatures.Group]
        def __init__(self, groups: _Optional[_Iterable[_Union[ItemResponse.AppFeatures.Group, _Mapping]]] = ...) -> None: ...
    class OtherFormFactors(_message.Message):
        __slots__ = ("surfaces",)
        class Surface(_message.Message):
            __slots__ = ("type", "target")
            class Browse(_message.Message):
                __slots__ = ("url",)
                URL_FIELD_NUMBER: _ClassVar[int]
                url: UrlWrapper
                def __init__(self, url: _Optional[_Union[UrlWrapper, _Mapping]] = ...) -> None: ...
            class Target(_message.Message):
                __slots__ = ("browse", "name", "icon")
                BROWSE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                ICON_FIELD_NUMBER: _ClassVar[int]
                browse: ItemResponse.OtherFormFactors.Surface.Browse
                name: str
                icon: ItemResponse.Image
                def __init__(self, browse: _Optional[_Union[ItemResponse.OtherFormFactors.Surface.Browse, _Mapping]] = ..., name: _Optional[str] = ..., icon: _Optional[_Union[ItemResponse.Image, _Mapping]] = ...) -> None: ...
            TYPE_FIELD_NUMBER: _ClassVar[int]
            TARGET_FIELD_NUMBER: _ClassVar[int]
            type: int
            target: ItemResponse.OtherFormFactors.Surface.Target
            def __init__(self, type: _Optional[int] = ..., target: _Optional[_Union[ItemResponse.OtherFormFactors.Surface.Target, _Mapping]] = ...) -> None: ...
        SURFACES_FIELD_NUMBER: _ClassVar[int]
        surfaces: _containers.RepeatedCompositeFieldContainer[ItemResponse.OtherFormFactors.Surface]
        def __init__(self, surfaces: _Optional[_Iterable[_Union[ItemResponse.OtherFormFactors.Surface, _Mapping]]] = ...) -> None: ...
    class Category(_message.Message):
        __slots__ = ("name", "link", "id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        link: StreamTagMetadata
        id: str
        def __init__(self, name: _Optional[str] = ..., link: _Optional[_Union[StreamTagMetadata, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
    class SignedIn(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class CommunityVideo(_message.Message):
        __slots__ = ("media", "title", "channel", "views")
        class Media(_message.Message):
            __slots__ = ("video", "thumbnail")
            class Video(_message.Message):
                __slots__ = ("url", "id", "playback")
                URL_FIELD_NUMBER: _ClassVar[int]
                ID_FIELD_NUMBER: _ClassVar[int]
                PLAYBACK_FIELD_NUMBER: _ClassVar[int]
                url: str
                id: str
                playback: bytes
                def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ..., playback: _Optional[bytes] = ...) -> None: ...
            VIDEO_FIELD_NUMBER: _ClassVar[int]
            THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
            video: ItemResponse.CommunityVideo.Media.Video
            thumbnail: ItemResponse.Image.Metadata
            def __init__(self, video: _Optional[_Union[ItemResponse.CommunityVideo.Media.Video, _Mapping]] = ..., thumbnail: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        VIEWS_FIELD_NUMBER: _ClassVar[int]
        media: ItemResponse.CommunityVideo.Media
        title: str
        channel: str
        views: int
        def __init__(self, media: _Optional[_Union[ItemResponse.CommunityVideo.Media, _Mapping]] = ..., title: _Optional[str] = ..., channel: _Optional[str] = ..., views: _Optional[int] = ...) -> None: ...
    class RegionalMetadata(_message.Message):
        __slots__ = ("app_name", "icon", "rating", "description", "share", "price", "review_questions_url", "family_badge", "featured_reviews", "review_tips", "review_url", "popup_url", "details_stream_url", "post_acquire_detail_stream_url", "content_rating", "tax_declaration", "signed_in", "regional_availability", "banner_image", "category", "availability", "teacher_approval", "family_library")
        class TeacherApprovalInfo(_message.Message):
            __slots__ = ("group1", "group2", "group3", "group4", "group5", "group6", "title", "subtitle", "artwork", "notes")
            class Group(_message.Message):
                __slots__ = ("title", "values")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                VALUES_FIELD_NUMBER: _ClassVar[int]
                title: str
                values: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, title: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
            class ArtworkUrl(_message.Message):
                __slots__ = ("url",)
                URL_FIELD_NUMBER: _ClassVar[int]
                url: str
                def __init__(self, url: _Optional[str] = ...) -> None: ...
            class ApprovalArtwork(_message.Message):
                __slots__ = ("image",)
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                image: ItemResponse.RegionalMetadata.TeacherApprovalInfo.ArtworkUrl
                def __init__(self, image: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.ArtworkUrl, _Mapping]] = ...) -> None: ...
            class Note(_message.Message):
                __slots__ = ("heading", "body")
                HEADING_FIELD_NUMBER: _ClassVar[int]
                BODY_FIELD_NUMBER: _ClassVar[int]
                heading: str
                body: str
                def __init__(self, heading: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
            class Notes(_message.Message):
                __slots__ = ("title", "notes")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                NOTES_FIELD_NUMBER: _ClassVar[int]
                title: str
                notes: _containers.RepeatedCompositeFieldContainer[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Note]
                def __init__(self, title: _Optional[str] = ..., notes: _Optional[_Iterable[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Note, _Mapping]]] = ...) -> None: ...
            GROUP1_FIELD_NUMBER: _ClassVar[int]
            GROUP2_FIELD_NUMBER: _ClassVar[int]
            GROUP3_FIELD_NUMBER: _ClassVar[int]
            GROUP4_FIELD_NUMBER: _ClassVar[int]
            GROUP5_FIELD_NUMBER: _ClassVar[int]
            GROUP6_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            ARTWORK_FIELD_NUMBER: _ClassVar[int]
            NOTES_FIELD_NUMBER: _ClassVar[int]
            group1: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            group2: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            group3: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            group4: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            group5: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            group6: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group
            title: str
            subtitle: str
            artwork: ItemResponse.RegionalMetadata.TeacherApprovalInfo.ApprovalArtwork
            notes: ItemResponse.RegionalMetadata.TeacherApprovalInfo.Notes
            def __init__(self, group1: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., group2: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., group3: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., group4: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., group5: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., group6: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Group, _Mapping]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., artwork: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.ApprovalArtwork, _Mapping]] = ..., notes: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo.Notes, _Mapping]] = ...) -> None: ...
        class FamilyLibrary(_message.Message):
            __slots__ = ("html",)
            HTML_FIELD_NUMBER: _ClassVar[int]
            html: str
            def __init__(self, html: _Optional[str] = ...) -> None: ...
        class Availability(_message.Message):
            __slots__ = ("restriction",)
            RESTRICTION_FIELD_NUMBER: _ClassVar[int]
            restriction: int
            def __init__(self, restriction: _Optional[int] = ...) -> None: ...
        class RegionalAvailability(_message.Message):
            __slots__ = ("first", "second")
            FIRST_FIELD_NUMBER: _ClassVar[int]
            SECOND_FIELD_NUMBER: _ClassVar[int]
            first: int
            second: int
            def __init__(self, first: _Optional[int] = ..., second: _Optional[int] = ...) -> None: ...
        APP_NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SHARE_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        REVIEW_QUESTIONS_URL_FIELD_NUMBER: _ClassVar[int]
        FAMILY_BADGE_FIELD_NUMBER: _ClassVar[int]
        FEATURED_REVIEWS_FIELD_NUMBER: _ClassVar[int]
        REVIEW_TIPS_FIELD_NUMBER: _ClassVar[int]
        REVIEW_URL_FIELD_NUMBER: _ClassVar[int]
        POPUP_URL_FIELD_NUMBER: _ClassVar[int]
        DETAILS_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
        POST_ACQUIRE_DETAIL_STREAM_URL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
        TAX_DECLARATION_FIELD_NUMBER: _ClassVar[int]
        SIGNED_IN_FIELD_NUMBER: _ClassVar[int]
        REGIONAL_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        BANNER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        TEACHER_APPROVAL_FIELD_NUMBER: _ClassVar[int]
        FAMILY_LIBRARY_FIELD_NUMBER: _ClassVar[int]
        app_name: StringWrapper
        icon: ItemResponse.Image
        rating: ItemResponse.Rating
        description: StringWrapper
        share: ItemResponse.Share
        price: ItemResponse.Price
        review_questions_url: UrlWrapper
        family_badge: ItemResponse.FamilyBadge
        featured_reviews: ItemResponse.FeaturedReviews
        review_tips: ItemResponse.ReviewTips
        review_url: UrlWrapper
        popup_url: UrlWrapper
        details_stream_url: UrlWrapper
        post_acquire_detail_stream_url: UrlWrapper
        content_rating: ItemResponse.ContentRating
        tax_declaration: StringWrapper
        signed_in: ItemResponse.SignedIn
        regional_availability: ItemResponse.RegionalMetadata.RegionalAvailability
        banner_image: ItemResponse.Image
        category: ItemResponse.Category
        availability: ItemResponse.RegionalMetadata.Availability
        teacher_approval: ItemResponse.RegionalMetadata.TeacherApprovalInfo
        family_library: ItemResponse.RegionalMetadata.FamilyLibrary
        def __init__(self, app_name: _Optional[_Union[StringWrapper, _Mapping]] = ..., icon: _Optional[_Union[ItemResponse.Image, _Mapping]] = ..., rating: _Optional[_Union[ItemResponse.Rating, _Mapping]] = ..., description: _Optional[_Union[StringWrapper, _Mapping]] = ..., share: _Optional[_Union[ItemResponse.Share, _Mapping]] = ..., price: _Optional[_Union[ItemResponse.Price, _Mapping]] = ..., review_questions_url: _Optional[_Union[UrlWrapper, _Mapping]] = ..., family_badge: _Optional[_Union[ItemResponse.FamilyBadge, _Mapping]] = ..., featured_reviews: _Optional[_Union[ItemResponse.FeaturedReviews, _Mapping]] = ..., review_tips: _Optional[_Union[ItemResponse.ReviewTips, _Mapping]] = ..., review_url: _Optional[_Union[UrlWrapper, _Mapping]] = ..., popup_url: _Optional[_Union[UrlWrapper, _Mapping]] = ..., details_stream_url: _Optional[_Union[UrlWrapper, _Mapping]] = ..., post_acquire_detail_stream_url: _Optional[_Union[UrlWrapper, _Mapping]] = ..., content_rating: _Optional[_Union[ItemResponse.ContentRating, _Mapping]] = ..., tax_declaration: _Optional[_Union[StringWrapper, _Mapping]] = ..., signed_in: _Optional[_Union[ItemResponse.SignedIn, _Mapping]] = ..., regional_availability: _Optional[_Union[ItemResponse.RegionalMetadata.RegionalAvailability, _Mapping]] = ..., banner_image: _Optional[_Union[ItemResponse.Image, _Mapping]] = ..., category: _Optional[_Union[ItemResponse.Category, _Mapping]] = ..., availability: _Optional[_Union[ItemResponse.RegionalMetadata.Availability, _Mapping]] = ..., teacher_approval: _Optional[_Union[ItemResponse.RegionalMetadata.TeacherApprovalInfo, _Mapping]] = ..., family_library: _Optional[_Union[ItemResponse.RegionalMetadata.FamilyLibrary, _Mapping]] = ...) -> None: ...
    class GenericMetadata(_message.Message):
        __slots__ = ("package_name", "version_info", "promotional_description", "data_safety_summary", "data_safety", "features", "other_form_factors", "privacy_policy", "downloads", "update_info", "images", "trailer", "developer_tag", "developer_info", "live_ops_stream", "comparable_item", "editors_choice", "permission_wrapper", "apk_metadata_wrapper", "contains_ads", "category", "in_app_purchases", "certificate_wrapper", "launch_info", "top_chart", "tag", "developer_name", "apk_metadata_wrapper_alt", "header_image_alt", "app_launch", "testing_program", "dependencies", "compatibility", "data_deletion", "signing_info", "tagline", "play_games", "signed_in", "community_videos", "signed_in_flags")
        class Trailer(_message.Message):
            __slots__ = ("video", "clip")
            class Video(_message.Message):
                __slots__ = ("source", "thumbnail")
                class Source(_message.Message):
                    __slots__ = ("watch_url", "video_id")
                    WATCH_URL_FIELD_NUMBER: _ClassVar[int]
                    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
                    watch_url: str
                    video_id: str
                    def __init__(self, watch_url: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
                source: ItemResponse.GenericMetadata.Trailer.Video.Source
                thumbnail: ItemResponse.Image.Metadata
                def __init__(self, source: _Optional[_Union[ItemResponse.GenericMetadata.Trailer.Video.Source, _Mapping]] = ..., thumbnail: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
            class Clip(_message.Message):
                __slots__ = ("source", "thumbnail")
                class Source(_message.Message):
                    __slots__ = ("url",)
                    URL_FIELD_NUMBER: _ClassVar[int]
                    url: str
                    def __init__(self, url: _Optional[str] = ...) -> None: ...
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
                source: ItemResponse.GenericMetadata.Trailer.Clip.Source
                thumbnail: ItemResponse.Image.Metadata
                def __init__(self, source: _Optional[_Union[ItemResponse.GenericMetadata.Trailer.Clip.Source, _Mapping]] = ..., thumbnail: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ...) -> None: ...
            VIDEO_FIELD_NUMBER: _ClassVar[int]
            CLIP_FIELD_NUMBER: _ClassVar[int]
            video: ItemResponse.GenericMetadata.Trailer.Video
            clip: ItemResponse.GenericMetadata.Trailer.Clip
            def __init__(self, video: _Optional[_Union[ItemResponse.GenericMetadata.Trailer.Video, _Mapping]] = ..., clip: _Optional[_Union[ItemResponse.GenericMetadata.Trailer.Clip, _Mapping]] = ...) -> None: ...
        class TestingProgram(_message.Message):
            __slots__ = ("subscription", "image", "display_name")
            class Subscription(_message.Message):
                __slots__ = ("subscribed", "subscribed_and_installed")
                SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
                SUBSCRIBED_AND_INSTALLED_FIELD_NUMBER: _ClassVar[int]
                subscribed: int
                subscribed_and_installed: int
                def __init__(self, subscribed: _Optional[int] = ..., subscribed_and_installed: _Optional[int] = ...) -> None: ...
            SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            subscription: ItemResponse.GenericMetadata.TestingProgram.Subscription
            image: ItemResponse.Image.Metadata
            display_name: str
            def __init__(self, subscription: _Optional[_Union[ItemResponse.GenericMetadata.TestingProgram.Subscription, _Mapping]] = ..., image: _Optional[_Union[ItemResponse.Image.Metadata, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...
        class Dependency(_message.Message):
            __slots__ = ("package_name", "min_version_code", "type", "is_optional", "module")
            class Module(_message.Message):
                __slots__ = ("name", "version_code", "type")
                NAME_FIELD_NUMBER: _ClassVar[int]
                VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                name: str
                version_code: int
                type: int
                def __init__(self, name: _Optional[str] = ..., version_code: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...
            PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
            MIN_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
            MODULE_FIELD_NUMBER: _ClassVar[int]
            package_name: str
            min_version_code: int
            type: int
            is_optional: bool
            module: _containers.RepeatedCompositeFieldContainer[ItemResponse.GenericMetadata.Dependency.Module]
            def __init__(self, package_name: _Optional[str] = ..., min_version_code: _Optional[int] = ..., type: _Optional[int] = ..., is_optional: _Optional[bool] = ..., module: _Optional[_Iterable[_Union[ItemResponse.GenericMetadata.Dependency.Module, _Mapping]]] = ...) -> None: ...
        class LibraryDependency(_message.Message):
            __slots__ = ("package_name", "version_code", "type", "size", "details")
            class Details(_message.Message):
                __slots__ = ("sdk",)
                class Sdk(_message.Message):
                    __slots__ = ("size", "version_major", "unconfirmed_3")
                    SIZE_FIELD_NUMBER: _ClassVar[int]
                    VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
                    UNCONFIRMED_3_FIELD_NUMBER: _ClassVar[int]
                    size: int
                    version_major: int
                    unconfirmed_3: int
                    def __init__(self, size: _Optional[int] = ..., version_major: _Optional[int] = ..., unconfirmed_3: _Optional[int] = ...) -> None: ...
                SDK_FIELD_NUMBER: _ClassVar[int]
                sdk: ItemResponse.GenericMetadata.LibraryDependency.Details.Sdk
                def __init__(self, sdk: _Optional[_Union[ItemResponse.GenericMetadata.LibraryDependency.Details.Sdk, _Mapping]] = ...) -> None: ...
            PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
            VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            package_name: str
            version_code: int
            type: int
            size: int
            details: ItemResponse.GenericMetadata.LibraryDependency.Details
            def __init__(self, package_name: _Optional[str] = ..., version_code: _Optional[int] = ..., type: _Optional[int] = ..., size: _Optional[int] = ..., details: _Optional[_Union[ItemResponse.GenericMetadata.LibraryDependency.Details, _Mapping]] = ...) -> None: ...
        class ModuleInstall(_message.Message):
            __slots__ = ("should_stage", "enable_rollback", "is_apex")
            SHOULD_STAGE_FIELD_NUMBER: _ClassVar[int]
            ENABLE_ROLLBACK_FIELD_NUMBER: _ClassVar[int]
            IS_APEX_FIELD_NUMBER: _ClassVar[int]
            should_stage: bool
            enable_rollback: bool
            is_apex: bool
            def __init__(self, should_stage: _Optional[bool] = ..., enable_rollback: _Optional[bool] = ..., is_apex: _Optional[bool] = ...) -> None: ...
        class Unconfirmed13(_message.Message):
            __slots__ = ("flag_1", "flag_2", "value_5", "value_6")
            FLAG_1_FIELD_NUMBER: _ClassVar[int]
            FLAG_2_FIELD_NUMBER: _ClassVar[int]
            VALUE_5_FIELD_NUMBER: _ClassVar[int]
            VALUE_6_FIELD_NUMBER: _ClassVar[int]
            flag_1: bool
            flag_2: bool
            value_5: float
            value_6: int
            def __init__(self, flag_1: _Optional[bool] = ..., flag_2: _Optional[bool] = ..., value_5: _Optional[float] = ..., value_6: _Optional[int] = ...) -> None: ...
        class Archive(_message.Message):
            __slots__ = ("derived_apk_id",)
            DERIVED_APK_ID_FIELD_NUMBER: _ClassVar[int]
            derived_apk_id: int
            def __init__(self, derived_apk_id: _Optional[int] = ...) -> None: ...
        class AntiTamper(_message.Message):
            __slots__ = ("transfer_key",)
            TRANSFER_KEY_FIELD_NUMBER: _ClassVar[int]
            transfer_key: bool
            def __init__(self, transfer_key: _Optional[bool] = ...) -> None: ...
        class Dependencies(_message.Message):
            __slots__ = ("install_location", "dependency", "target_sdk", "target_sandbox_version", "android_category", "frosting_id", "installer_permissions", "library_dependency", "module_install", "unconfirmed_13", "delivery_token", "archive", "licensing_flag", "anti_tamper")
            INSTALL_LOCATION_FIELD_NUMBER: _ClassVar[int]
            DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
            TARGET_SDK_FIELD_NUMBER: _ClassVar[int]
            TARGET_SANDBOX_VERSION_FIELD_NUMBER: _ClassVar[int]
            ANDROID_CATEGORY_FIELD_NUMBER: _ClassVar[int]
            FROSTING_ID_FIELD_NUMBER: _ClassVar[int]
            INSTALLER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            LIBRARY_DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
            MODULE_INSTALL_FIELD_NUMBER: _ClassVar[int]
            UNCONFIRMED_13_FIELD_NUMBER: _ClassVar[int]
            DELIVERY_TOKEN_FIELD_NUMBER: _ClassVar[int]
            ARCHIVE_FIELD_NUMBER: _ClassVar[int]
            LICENSING_FLAG_FIELD_NUMBER: _ClassVar[int]
            ANTI_TAMPER_FIELD_NUMBER: _ClassVar[int]
            install_location: int
            dependency: _containers.RepeatedCompositeFieldContainer[ItemResponse.GenericMetadata.Dependency]
            target_sdk: int
            target_sandbox_version: int
            android_category: int
            frosting_id: int
            installer_permissions: _containers.RepeatedScalarFieldContainer[str]
            library_dependency: _containers.RepeatedCompositeFieldContainer[ItemResponse.GenericMetadata.LibraryDependency]
            module_install: ItemResponse.GenericMetadata.ModuleInstall
            unconfirmed_13: ItemResponse.GenericMetadata.Unconfirmed13
            delivery_token: str
            archive: ItemResponse.GenericMetadata.Archive
            licensing_flag: bool
            anti_tamper: ItemResponse.GenericMetadata.AntiTamper
            def __init__(self, install_location: _Optional[int] = ..., dependency: _Optional[_Iterable[_Union[ItemResponse.GenericMetadata.Dependency, _Mapping]]] = ..., target_sdk: _Optional[int] = ..., target_sandbox_version: _Optional[int] = ..., android_category: _Optional[int] = ..., frosting_id: _Optional[int] = ..., installer_permissions: _Optional[_Iterable[str]] = ..., library_dependency: _Optional[_Iterable[_Union[ItemResponse.GenericMetadata.LibraryDependency, _Mapping]]] = ..., module_install: _Optional[_Union[ItemResponse.GenericMetadata.ModuleInstall, _Mapping]] = ..., unconfirmed_13: _Optional[_Union[ItemResponse.GenericMetadata.Unconfirmed13, _Mapping]] = ..., delivery_token: _Optional[str] = ..., archive: _Optional[_Union[ItemResponse.GenericMetadata.Archive, _Mapping]] = ..., licensing_flag: _Optional[bool] = ..., anti_tamper: _Optional[_Union[ItemResponse.GenericMetadata.AntiTamper, _Mapping]] = ...) -> None: ...
        class Device(_message.Message):
            __slots__ = ("required_os", "name")
            REQUIRED_OS_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            required_os: str
            name: str
            def __init__(self, required_os: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
        class Compatibility(_message.Message):
            __slots__ = ("device",)
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            device: _containers.RepeatedCompositeFieldContainer[ItemResponse.GenericMetadata.Device]
            def __init__(self, device: _Optional[_Iterable[_Union[ItemResponse.GenericMetadata.Device, _Mapping]]] = ...) -> None: ...
        class EditorsChoice(_message.Message):
            __slots__ = ("bulletins", "award", "title", "subtitle")
            BULLETINS_FIELD_NUMBER: _ClassVar[int]
            AWARD_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            bulletins: _containers.RepeatedScalarFieldContainer[str]
            award: str
            title: str
            subtitle: str
            def __init__(self, bulletins: _Optional[_Iterable[str]] = ..., award: _Optional[str] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ...) -> None: ...
        class UpdateInfo(_message.Message):
            __slots__ = ("changelog", "last_updated")
            CHANGELOG_FIELD_NUMBER: _ClassVar[int]
            LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
            changelog: str
            last_updated: str
            def __init__(self, changelog: _Optional[str] = ..., last_updated: _Optional[str] = ...) -> None: ...
        class LaunchInfo(_message.Message):
            __slots__ = ("launch_date", "timestamp")
            LAUNCH_DATE_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            launch_date: str
            timestamp: Timestamp
            def __init__(self, launch_date: _Optional[str] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...
        class Downloads(_message.Message):
            __slots__ = ("label_long", "count_rounded", "count_exact", "label_abbreviated", "label_short")
            LABEL_LONG_FIELD_NUMBER: _ClassVar[int]
            COUNT_ROUNDED_FIELD_NUMBER: _ClassVar[int]
            COUNT_EXACT_FIELD_NUMBER: _ClassVar[int]
            LABEL_ABBREVIATED_FIELD_NUMBER: _ClassVar[int]
            LABEL_SHORT_FIELD_NUMBER: _ClassVar[int]
            label_long: str
            count_rounded: int
            count_exact: int
            label_abbreviated: str
            label_short: str
            def __init__(self, label_long: _Optional[str] = ..., count_rounded: _Optional[int] = ..., count_exact: _Optional[int] = ..., label_abbreviated: _Optional[str] = ..., label_short: _Optional[str] = ...) -> None: ...
        class InAppPurchases(_message.Message):
            __slots__ = ("price_range",)
            PRICE_RANGE_FIELD_NUMBER: _ClassVar[int]
            price_range: str
            def __init__(self, price_range: _Optional[str] = ...) -> None: ...
        class AppLaunch(_message.Message):
            __slots__ = ("name", "intent_action", "intent_activity")
            NAME_FIELD_NUMBER: _ClassVar[int]
            INTENT_ACTION_FIELD_NUMBER: _ClassVar[int]
            INTENT_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
            name: str
            intent_action: str
            intent_activity: str
            def __init__(self, name: _Optional[str] = ..., intent_action: _Optional[str] = ..., intent_activity: _Optional[str] = ...) -> None: ...
        class TopChartInfo(_message.Message):
            __slots__ = ("title", "link")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            LINK_FIELD_NUMBER: _ClassVar[int]
            title: str
            link: StreamTagMetadata
            def __init__(self, title: _Optional[str] = ..., link: _Optional[_Union[StreamTagMetadata, _Mapping]] = ...) -> None: ...
        class PermissionWrapper(_message.Message):
            __slots__ = ("permissions",)
            PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            permissions: _containers.RepeatedCompositeFieldContainer[StringWrapper]
            def __init__(self, permissions: _Optional[_Iterable[_Union[StringWrapper, _Mapping]]] = ...) -> None: ...
        class VersionInfo(_message.Message):
            __slots__ = ("version_code", "version_string", "offer_type")
            VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
            VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
            OFFER_TYPE_FIELD_NUMBER: _ClassVar[int]
            version_code: int
            version_string: str
            offer_type: int
            def __init__(self, version_code: _Optional[int] = ..., version_string: _Optional[str] = ..., offer_type: _Optional[int] = ...) -> None: ...
        class DeletionLinks(_message.Message):
            __slots__ = ("account_deletion_url", "data_deletion_url")
            ACCOUNT_DELETION_URL_FIELD_NUMBER: _ClassVar[int]
            DATA_DELETION_URL_FIELD_NUMBER: _ClassVar[int]
            account_deletion_url: str
            data_deletion_url: str
            def __init__(self, account_deletion_url: _Optional[str] = ..., data_deletion_url: _Optional[str] = ...) -> None: ...
        class DeletionUrls(_message.Message):
            __slots__ = ("links",)
            LINKS_FIELD_NUMBER: _ClassVar[int]
            links: ItemResponse.GenericMetadata.DeletionLinks
            def __init__(self, links: _Optional[_Union[ItemResponse.GenericMetadata.DeletionLinks, _Mapping]] = ...) -> None: ...
        class DataDeletion(_message.Message):
            __slots__ = ("urls",)
            URLS_FIELD_NUMBER: _ClassVar[int]
            urls: ItemResponse.GenericMetadata.DeletionUrls
            def __init__(self, urls: _Optional[_Union[ItemResponse.GenericMetadata.DeletionUrls, _Mapping]] = ...) -> None: ...
        class DataDeletionWrapper(_message.Message):
            __slots__ = ("deletion",)
            DELETION_FIELD_NUMBER: _ClassVar[int]
            deletion: ItemResponse.GenericMetadata.DataDeletion
            def __init__(self, deletion: _Optional[_Union[ItemResponse.GenericMetadata.DataDeletion, _Mapping]] = ...) -> None: ...
        class CertificateData(_message.Message):
            __slots__ = ("encoded", "public_key")
            ENCODED_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            encoded: bytes
            public_key: bytes
            def __init__(self, encoded: _Optional[bytes] = ..., public_key: _Optional[bytes] = ...) -> None: ...
        class Signer(_message.Message):
            __slots__ = ("certificate", "scheme")
            CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
            SCHEME_FIELD_NUMBER: _ClassVar[int]
            certificate: ItemResponse.GenericMetadata.CertificateData
            scheme: int
            def __init__(self, certificate: _Optional[_Union[ItemResponse.GenericMetadata.CertificateData, _Mapping]] = ..., scheme: _Optional[int] = ...) -> None: ...
        class Signers(_message.Message):
            __slots__ = ("signer",)
            SIGNER_FIELD_NUMBER: _ClassVar[int]
            signer: _containers.RepeatedCompositeFieldContainer[ItemResponse.GenericMetadata.Signer]
            def __init__(self, signer: _Optional[_Iterable[_Union[ItemResponse.GenericMetadata.Signer, _Mapping]]] = ...) -> None: ...
        class SigningInfo(_message.Message):
            __slots__ = ("signers",)
            SIGNERS_FIELD_NUMBER: _ClassVar[int]
            signers: ItemResponse.GenericMetadata.Signers
            def __init__(self, signers: _Optional[_Union[ItemResponse.GenericMetadata.Signers, _Mapping]] = ...) -> None: ...
        class ContainsAds(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PlayGames(_message.Message):
            __slots__ = ("enabled", "third")
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            THIRD_FIELD_NUMBER: _ClassVar[int]
            enabled: int
            third: int
            def __init__(self, enabled: _Optional[int] = ..., third: _Optional[int] = ...) -> None: ...
        class CommunityVideos(_message.Message):
            __slots__ = ("videos",)
            VIDEOS_FIELD_NUMBER: _ClassVar[int]
            videos: _containers.RepeatedCompositeFieldContainer[ItemResponse.CommunityVideo]
            def __init__(self, videos: _Optional[_Iterable[_Union[ItemResponse.CommunityVideo, _Mapping]]] = ...) -> None: ...
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
        PROMOTIONAL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DATA_SAFETY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        DATA_SAFETY_FIELD_NUMBER: _ClassVar[int]
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        OTHER_FORM_FACTORS_FIELD_NUMBER: _ClassVar[int]
        PRIVACY_POLICY_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        TRAILER_FIELD_NUMBER: _ClassVar[int]
        DEVELOPER_TAG_FIELD_NUMBER: _ClassVar[int]
        DEVELOPER_INFO_FIELD_NUMBER: _ClassVar[int]
        LIVE_OPS_STREAM_FIELD_NUMBER: _ClassVar[int]
        COMPARABLE_ITEM_FIELD_NUMBER: _ClassVar[int]
        EDITORS_CHOICE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        APK_METADATA_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        CONTAINS_ADS_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        IN_APP_PURCHASES_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        LAUNCH_INFO_FIELD_NUMBER: _ClassVar[int]
        TOP_CHART_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        DEVELOPER_NAME_FIELD_NUMBER: _ClassVar[int]
        APK_METADATA_WRAPPER_ALT_FIELD_NUMBER: _ClassVar[int]
        HEADER_IMAGE_ALT_FIELD_NUMBER: _ClassVar[int]
        APP_LAUNCH_FIELD_NUMBER: _ClassVar[int]
        TESTING_PROGRAM_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
        DATA_DELETION_FIELD_NUMBER: _ClassVar[int]
        SIGNING_INFO_FIELD_NUMBER: _ClassVar[int]
        TAGLINE_FIELD_NUMBER: _ClassVar[int]
        PLAY_GAMES_FIELD_NUMBER: _ClassVar[int]
        SIGNED_IN_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_VIDEOS_FIELD_NUMBER: _ClassVar[int]
        SIGNED_IN_FLAGS_FIELD_NUMBER: _ClassVar[int]
        package_name: StringWrapper
        version_info: ItemResponse.GenericMetadata.VersionInfo
        promotional_description: StringWrapper
        data_safety_summary: ItemResponse.DataSafetySummary
        data_safety: ItemResponse.DataSafety
        features: ItemResponse.AppFeatures
        other_form_factors: ItemResponse.OtherFormFactors
        privacy_policy: ItemResponse.PrivacyPolicy
        downloads: ItemResponse.GenericMetadata.Downloads
        update_info: ItemResponse.GenericMetadata.UpdateInfo
        images: ItemResponse.Image
        trailer: ItemResponse.GenericMetadata.Trailer
        developer_tag: Tag
        developer_info: ItemResponse.DeveloperInfo
        live_ops_stream: UrlWrapper
        comparable_item: ItemResponse.SubItem
        editors_choice: ItemResponse.GenericMetadata.EditorsChoice
        permission_wrapper: ItemResponse.GenericMetadata.PermissionWrapper
        apk_metadata_wrapper: ItemResponse.ApkMetadataWrapper
        contains_ads: ItemResponse.GenericMetadata.ContainsAds
        category: Tag
        in_app_purchases: ItemResponse.GenericMetadata.InAppPurchases
        certificate_wrapper: ItemResponse.CertificateWrapper
        launch_info: ItemResponse.GenericMetadata.LaunchInfo
        top_chart: ItemResponse.GenericMetadata.TopChartInfo
        tag: TagWrapper
        developer_name: StringWrapper
        apk_metadata_wrapper_alt: ItemResponse.ApkMetadataWrapper
        header_image_alt: ItemResponse.Image
        app_launch: ItemResponse.GenericMetadata.AppLaunch
        testing_program: ItemResponse.GenericMetadata.TestingProgram
        dependencies: ItemResponse.GenericMetadata.Dependencies
        compatibility: ItemResponse.GenericMetadata.Compatibility
        data_deletion: ItemResponse.GenericMetadata.DataDeletionWrapper
        signing_info: ItemResponse.GenericMetadata.SigningInfo
        tagline: StringWrapper
        play_games: ItemResponse.GenericMetadata.PlayGames
        signed_in: ItemResponse.SignedIn
        community_videos: ItemResponse.GenericMetadata.CommunityVideos
        signed_in_flags: ItemResponse.SignedIn
        def __init__(self, package_name: _Optional[_Union[StringWrapper, _Mapping]] = ..., version_info: _Optional[_Union[ItemResponse.GenericMetadata.VersionInfo, _Mapping]] = ..., promotional_description: _Optional[_Union[StringWrapper, _Mapping]] = ..., data_safety_summary: _Optional[_Union[ItemResponse.DataSafetySummary, _Mapping]] = ..., data_safety: _Optional[_Union[ItemResponse.DataSafety, _Mapping]] = ..., features: _Optional[_Union[ItemResponse.AppFeatures, _Mapping]] = ..., other_form_factors: _Optional[_Union[ItemResponse.OtherFormFactors, _Mapping]] = ..., privacy_policy: _Optional[_Union[ItemResponse.PrivacyPolicy, _Mapping]] = ..., downloads: _Optional[_Union[ItemResponse.GenericMetadata.Downloads, _Mapping]] = ..., update_info: _Optional[_Union[ItemResponse.GenericMetadata.UpdateInfo, _Mapping]] = ..., images: _Optional[_Union[ItemResponse.Image, _Mapping]] = ..., trailer: _Optional[_Union[ItemResponse.GenericMetadata.Trailer, _Mapping]] = ..., developer_tag: _Optional[_Union[Tag, _Mapping]] = ..., developer_info: _Optional[_Union[ItemResponse.DeveloperInfo, _Mapping]] = ..., live_ops_stream: _Optional[_Union[UrlWrapper, _Mapping]] = ..., comparable_item: _Optional[_Union[ItemResponse.SubItem, _Mapping]] = ..., editors_choice: _Optional[_Union[ItemResponse.GenericMetadata.EditorsChoice, _Mapping]] = ..., permission_wrapper: _Optional[_Union[ItemResponse.GenericMetadata.PermissionWrapper, _Mapping]] = ..., apk_metadata_wrapper: _Optional[_Union[ItemResponse.ApkMetadataWrapper, _Mapping]] = ..., contains_ads: _Optional[_Union[ItemResponse.GenericMetadata.ContainsAds, _Mapping]] = ..., category: _Optional[_Union[Tag, _Mapping]] = ..., in_app_purchases: _Optional[_Union[ItemResponse.GenericMetadata.InAppPurchases, _Mapping]] = ..., certificate_wrapper: _Optional[_Union[ItemResponse.CertificateWrapper, _Mapping]] = ..., launch_info: _Optional[_Union[ItemResponse.GenericMetadata.LaunchInfo, _Mapping]] = ..., top_chart: _Optional[_Union[ItemResponse.GenericMetadata.TopChartInfo, _Mapping]] = ..., tag: _Optional[_Union[TagWrapper, _Mapping]] = ..., developer_name: _Optional[_Union[StringWrapper, _Mapping]] = ..., apk_metadata_wrapper_alt: _Optional[_Union[ItemResponse.ApkMetadataWrapper, _Mapping]] = ..., header_image_alt: _Optional[_Union[ItemResponse.Image, _Mapping]] = ..., app_launch: _Optional[_Union[ItemResponse.GenericMetadata.AppLaunch, _Mapping]] = ..., testing_program: _Optional[_Union[ItemResponse.GenericMetadata.TestingProgram, _Mapping]] = ..., dependencies: _Optional[_Union[ItemResponse.GenericMetadata.Dependencies, _Mapping]] = ..., compatibility: _Optional[_Union[ItemResponse.GenericMetadata.Compatibility, _Mapping]] = ..., data_deletion: _Optional[_Union[ItemResponse.GenericMetadata.DataDeletionWrapper, _Mapping]] = ..., signing_info: _Optional[_Union[ItemResponse.GenericMetadata.SigningInfo, _Mapping]] = ..., tagline: _Optional[_Union[StringWrapper, _Mapping]] = ..., play_games: _Optional[_Union[ItemResponse.GenericMetadata.PlayGames, _Mapping]] = ..., signed_in: _Optional[_Union[ItemResponse.SignedIn, _Mapping]] = ..., community_videos: _Optional[_Union[ItemResponse.GenericMetadata.CommunityVideos, _Mapping]] = ..., signed_in_flags: _Optional[_Union[ItemResponse.SignedIn, _Mapping]] = ...) -> None: ...
    class ApkMetadataWrapper(_message.Message):
        __slots__ = ("metadata", "main_obb", "patch_obb", "total_size", "badge_logs")
        class PatchInfo(_message.Message):
            __slots__ = ("base_version_code", "size")
            BASE_VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            base_version_code: int
            size: int
            def __init__(self, base_version_code: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
        class ApkInfo(_message.Message):
            __slots__ = ("version_code", "size", "size_compressed", "patch")
            VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            SIZE_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
            PATCH_FIELD_NUMBER: _ClassVar[int]
            version_code: int
            size: int
            size_compressed: int
            patch: ItemResponse.ApkMetadataWrapper.PatchInfo
            def __init__(self, version_code: _Optional[int] = ..., size: _Optional[int] = ..., size_compressed: _Optional[int] = ..., patch: _Optional[_Union[ItemResponse.ApkMetadataWrapper.PatchInfo, _Mapping]] = ...) -> None: ...
        class SplitHotfix(_message.Message):
            __slots__ = ("sdk_split_hotfix_version",)
            SDK_SPLIT_HOTFIX_VERSION_FIELD_NUMBER: _ClassVar[int]
            sdk_split_hotfix_version: int
            def __init__(self, sdk_split_hotfix_version: _Optional[int] = ...) -> None: ...
        class SplitApk(_message.Message):
            __slots__ = ("split_name", "info", "dex_metadata", "hotfix")
            SPLIT_NAME_FIELD_NUMBER: _ClassVar[int]
            INFO_FIELD_NUMBER: _ClassVar[int]
            DEX_METADATA_FIELD_NUMBER: _ClassVar[int]
            HOTFIX_FIELD_NUMBER: _ClassVar[int]
            split_name: str
            info: ItemResponse.ApkMetadataWrapper.ApkInfo
            dex_metadata: ItemResponse.ApkMetadataWrapper.ApkInfo
            hotfix: ItemResponse.ApkMetadataWrapper.SplitHotfix
            def __init__(self, split_name: _Optional[str] = ..., info: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., dex_metadata: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., hotfix: _Optional[_Union[ItemResponse.ApkMetadataWrapper.SplitHotfix, _Mapping]] = ...) -> None: ...
        class AssetPack(_message.Message):
            __slots__ = ("name", "info", "version")
            NAME_FIELD_NUMBER: _ClassVar[int]
            INFO_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            name: str
            info: ItemResponse.ApkMetadataWrapper.ApkInfo
            version: int
            def __init__(self, name: _Optional[str] = ..., info: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...
        class ApkMetadata(_message.Message):
            __slots__ = ("base_apk", "split_apks", "dex_metadata", "derived_apk_id", "internal_sharing_id", "asset_packs", "package_size")
            BASE_APK_FIELD_NUMBER: _ClassVar[int]
            SPLIT_APKS_FIELD_NUMBER: _ClassVar[int]
            DEX_METADATA_FIELD_NUMBER: _ClassVar[int]
            DERIVED_APK_ID_FIELD_NUMBER: _ClassVar[int]
            INTERNAL_SHARING_ID_FIELD_NUMBER: _ClassVar[int]
            ASSET_PACKS_FIELD_NUMBER: _ClassVar[int]
            PACKAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
            base_apk: ItemResponse.ApkMetadataWrapper.ApkInfo
            split_apks: _containers.RepeatedCompositeFieldContainer[ItemResponse.ApkMetadataWrapper.SplitApk]
            dex_metadata: ItemResponse.ApkMetadataWrapper.ApkInfo
            derived_apk_id: int
            internal_sharing_id: str
            asset_packs: _containers.RepeatedCompositeFieldContainer[ItemResponse.ApkMetadataWrapper.AssetPack]
            package_size: int
            def __init__(self, base_apk: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., split_apks: _Optional[_Iterable[_Union[ItemResponse.ApkMetadataWrapper.SplitApk, _Mapping]]] = ..., dex_metadata: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., derived_apk_id: _Optional[int] = ..., internal_sharing_id: _Optional[str] = ..., asset_packs: _Optional[_Iterable[_Union[ItemResponse.ApkMetadataWrapper.AssetPack, _Mapping]]] = ..., package_size: _Optional[int] = ...) -> None: ...
        class BadgeLogs(_message.Message):
            __slots__ = ("server_logs_cookie",)
            SERVER_LOGS_COOKIE_FIELD_NUMBER: _ClassVar[int]
            server_logs_cookie: bytes
            def __init__(self, server_logs_cookie: _Optional[bytes] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        MAIN_OBB_FIELD_NUMBER: _ClassVar[int]
        PATCH_OBB_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        BADGE_LOGS_FIELD_NUMBER: _ClassVar[int]
        metadata: ItemResponse.ApkMetadataWrapper.ApkMetadata
        main_obb: ItemResponse.ApkMetadataWrapper.ApkInfo
        patch_obb: ItemResponse.ApkMetadataWrapper.ApkInfo
        total_size: int
        badge_logs: ItemResponse.ApkMetadataWrapper.BadgeLogs
        def __init__(self, metadata: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkMetadata, _Mapping]] = ..., main_obb: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., patch_obb: _Optional[_Union[ItemResponse.ApkMetadataWrapper.ApkInfo, _Mapping]] = ..., total_size: _Optional[int] = ..., badge_logs: _Optional[_Union[ItemResponse.ApkMetadataWrapper.BadgeLogs, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("metadata",)
        class MetadataWrapper(_message.Message):
            __slots__ = ("package_name", "regional_metadata", "generic_metadata")
            PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
            REGIONAL_METADATA_FIELD_NUMBER: _ClassVar[int]
            GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
            package_name: StringWrapper
            regional_metadata: ItemResponse.RegionalMetadata
            generic_metadata: ItemResponse.GenericMetadata
            def __init__(self, package_name: _Optional[_Union[StringWrapper, _Mapping]] = ..., regional_metadata: _Optional[_Union[ItemResponse.RegionalMetadata, _Mapping]] = ..., generic_metadata: _Optional[_Union[ItemResponse.GenericMetadata, _Mapping]] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        metadata: ItemResponse.Item.MetadataWrapper
        def __init__(self, metadata: _Optional[_Union[ItemResponse.Item.MetadataWrapper, _Mapping]] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[ItemResponse.Item]
    def __init__(self, item: _Optional[_Iterable[_Union[ItemResponse.Item, _Mapping]]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ("title", "image", "subtitle", "subtitle_html", "description")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_HTML_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    image: Artwork
    subtitle: str
    subtitle_html: str
    description: str
    def __init__(self, title: _Optional[str] = ..., image: _Optional[_Union[Artwork, _Mapping]] = ..., subtitle: _Optional[str] = ..., subtitle_html: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ("primary", "secondary")
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    primary: str
    secondary: str
    def __init__(self, primary: _Optional[str] = ..., secondary: _Optional[str] = ...) -> None: ...

class Annotation(_message.Message):
    __slots__ = ("content_rating", "category")
    CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    content_rating: Label
    category: Category
    def __init__(self, content_rating: _Optional[_Union[Label, _Mapping]] = ..., category: _Optional[_Union[Category, _Mapping]] = ...) -> None: ...

class StreamTagMetadata(_message.Message):
    __slots__ = ("category_metadata", "search_metadata")
    class SearchMetadata(_message.Message):
        __slots__ = ("url", "query", "unknown3", "unknown4")
        URL_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
        url: str
        query: str
        unknown3: int
        unknown4: int
        def __init__(self, url: _Optional[str] = ..., query: _Optional[str] = ..., unknown3: _Optional[int] = ..., unknown4: _Optional[int] = ...) -> None: ...
    class CategoryMetadata(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    CATEGORY_METADATA_FIELD_NUMBER: _ClassVar[int]
    SEARCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    category_metadata: StreamTagMetadata.CategoryMetadata
    search_metadata: StreamTagMetadata.SearchMetadata
    def __init__(self, category_metadata: _Optional[_Union[StreamTagMetadata.CategoryMetadata, _Mapping]] = ..., search_metadata: _Optional[_Union[StreamTagMetadata.SearchMetadata, _Mapping]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("name", "metadata", "category_id", "genome_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    GENOME_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: StreamTagMetadata
    category_id: str
    genome_id: str
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[StreamTagMetadata, _Mapping]] = ..., category_id: _Optional[str] = ..., genome_id: _Optional[str] = ...) -> None: ...

class TagWrapper(_message.Message):
    __slots__ = ("type1", "type2", "type3", "type4", "type5", "type6", "type7")
    TYPE1_FIELD_NUMBER: _ClassVar[int]
    TYPE2_FIELD_NUMBER: _ClassVar[int]
    TYPE3_FIELD_NUMBER: _ClassVar[int]
    TYPE4_FIELD_NUMBER: _ClassVar[int]
    TYPE5_FIELD_NUMBER: _ClassVar[int]
    TYPE6_FIELD_NUMBER: _ClassVar[int]
    TYPE7_FIELD_NUMBER: _ClassVar[int]
    type1: _containers.RepeatedCompositeFieldContainer[TagList]
    type2: _containers.RepeatedCompositeFieldContainer[TagList]
    type3: _containers.RepeatedCompositeFieldContainer[TagList]
    type4: _containers.RepeatedCompositeFieldContainer[TagList]
    type5: _containers.RepeatedCompositeFieldContainer[TagList]
    type6: _containers.RepeatedCompositeFieldContainer[TagList]
    type7: _containers.RepeatedCompositeFieldContainer[TagList]
    def __init__(self, type1: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type2: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type3: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type4: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type5: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type6: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ..., type7: _Optional[_Iterable[_Union[TagList, _Mapping]]] = ...) -> None: ...

class TagList(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class ArtworkWrapper(_message.Message):
    __slots__ = ("artwork",)
    ARTWORK_FIELD_NUMBER: _ClassVar[int]
    artwork: Artwork
    def __init__(self, artwork: _Optional[_Union[Artwork, _Mapping]] = ...) -> None: ...

class Artwork(_message.Message):
    __slots__ = ("artwork_type", "dimensions", "url", "alt_text", "https_url", "sequence_position", "is_fife_url_supported", "citation", "duration_in_seconds", "fill_color_hex", "is_autogenerated", "attribution", "background_color_hex", "color_palette", "device_type", "is_fife_monogram_supported", "alternate_url")
    class Dimensions(_message.Message):
        __slots__ = ("width", "height", "aspect_ratio")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        aspect_ratio: float
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., aspect_ratio: _Optional[float] = ...) -> None: ...
    class Citation(_message.Message):
        __slots__ = ("title", "url")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        title: str
        url: str
        def __init__(self, title: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    ARTWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    HTTPS_URL_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_POSITION_FIELD_NUMBER: _ClassVar[int]
    IS_FIFE_URL_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CITATION_FIELD_NUMBER: _ClassVar[int]
    DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FILL_COLOR_HEX_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_HEX_FIELD_NUMBER: _ClassVar[int]
    COLOR_PALETTE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FIFE_MONOGRAM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_URL_FIELD_NUMBER: _ClassVar[int]
    artwork_type: int
    dimensions: Artwork.Dimensions
    url: str
    alt_text: str
    https_url: str
    sequence_position: int
    is_fife_url_supported: bool
    citation: Artwork.Citation
    duration_in_seconds: int
    fill_color_hex: str
    is_autogenerated: bool
    attribution: ArtworkAttribution
    background_color_hex: str
    color_palette: ColorPalette
    device_type: int
    is_fife_monogram_supported: bool
    alternate_url: str
    def __init__(self, artwork_type: _Optional[int] = ..., dimensions: _Optional[_Union[Artwork.Dimensions, _Mapping]] = ..., url: _Optional[str] = ..., alt_text: _Optional[str] = ..., https_url: _Optional[str] = ..., sequence_position: _Optional[int] = ..., is_fife_url_supported: _Optional[bool] = ..., citation: _Optional[_Union[Artwork.Citation, _Mapping]] = ..., duration_in_seconds: _Optional[int] = ..., fill_color_hex: _Optional[str] = ..., is_autogenerated: _Optional[bool] = ..., attribution: _Optional[_Union[ArtworkAttribution, _Mapping]] = ..., background_color_hex: _Optional[str] = ..., color_palette: _Optional[_Union[ColorPalette, _Mapping]] = ..., device_type: _Optional[int] = ..., is_fife_monogram_supported: _Optional[bool] = ..., alternate_url: _Optional[str] = ...) -> None: ...

class ArtworkAttribution(_message.Message):
    __slots__ = ("source_name", "source_url", "license_name", "license_url")
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    LICENSE_NAME_FIELD_NUMBER: _ClassVar[int]
    LICENSE_URL_FIELD_NUMBER: _ClassVar[int]
    source_name: str
    source_url: str
    license_name: str
    license_url: str
    def __init__(self, source_name: _Optional[str] = ..., source_url: _Optional[str] = ..., license_name: _Optional[str] = ..., license_url: _Optional[str] = ...) -> None: ...

class ColorPalette(_message.Message):
    __slots__ = ("light_vibrant", "vibrant", "dark_vibrant", "light_muted", "muted", "dark_muted")
    LIGHT_VIBRANT_FIELD_NUMBER: _ClassVar[int]
    VIBRANT_FIELD_NUMBER: _ClassVar[int]
    DARK_VIBRANT_FIELD_NUMBER: _ClassVar[int]
    LIGHT_MUTED_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    DARK_MUTED_FIELD_NUMBER: _ClassVar[int]
    light_vibrant: str
    vibrant: str
    dark_vibrant: str
    light_muted: str
    muted: str
    dark_muted: str
    def __init__(self, light_vibrant: _Optional[str] = ..., vibrant: _Optional[str] = ..., dark_vibrant: _Optional[str] = ..., light_muted: _Optional[str] = ..., muted: _Optional[str] = ..., dark_muted: _Optional[str] = ...) -> None: ...

class StringWrapper(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class UrlWrapper(_message.Message):
    __slots__ = ("url", "id")
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    id: str
    def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class TimestampWrapper(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: Timestamp
    def __init__(self, timestamp: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...

class TimestampEntry(_message.Message):
    __slots__ = ("entry", "timestamp")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    entry: str
    timestamp: Timestamp
    def __init__(self, entry: _Optional[str] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...

class TimestampEntryWrapper(_message.Message):
    __slots__ = ("android_id", "entry")
    ANDROID_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    android_id: str
    entry: TimestampEntry
    def __init__(self, android_id: _Optional[str] = ..., entry: _Optional[_Union[TimestampEntry, _Mapping]] = ...) -> None: ...

class NestedTimestamp(_message.Message):
    __slots__ = ("wrapper", "timestamp")
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    wrapper: TimestampWrapper
    timestamp: Timestamp
    def __init__(self, wrapper: _Optional[_Union[TimestampWrapper, _Mapping]] = ..., timestamp: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...

class TimestampContainer(_message.Message):
    __slots__ = ("entry_wrapper", "nested_timestamp")
    ENTRY_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    NESTED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    entry_wrapper: TimestampEntryWrapper
    nested_timestamp: NestedTimestamp
    def __init__(self, entry_wrapper: _Optional[_Union[TimestampEntryWrapper, _Mapping]] = ..., nested_timestamp: _Optional[_Union[NestedTimestamp, _Mapping]] = ...) -> None: ...
