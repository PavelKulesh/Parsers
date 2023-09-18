import pytest
from mongomock import MongoClient

from src.dao.twitch_dao import TwitchStreamDAO
from src.dao.lamoda_dao import LamodaItemDAO

valid_stream_data = [
    {
        "id": "40629247607",
        "user_id": "148934000",
        "user_login": "kimdduddi",
        "user_name": "김뚜띠_",
        "game_id": "490100",
        "game_name": "Lost Ark",
        "type": "live",
        "title": "4관문 175줄",
        "viewer_count": 26687,
        "started_at": "2023-09-18T02:55:51Z",
        "language": "ko",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_kimdduddi-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "한국어"
        ],
        "is_mature": False
    },
    {
        "id": "40630765239",
        "user_id": "203654142",
        "user_login": "fantasista_jp",
        "user_name": "ファン太",
        "game_id": "32982",
        "game_name": "Grand Theft Auto V",
        "type": "live",
        "title": "ストグラ42日～憧れのyour my slender～鳩禁止",
        "viewer_count": 22959,
        "started_at": "2023-09-18T09:45:52Z",
        "language": "ja",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_fantasista_jp-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "日本語",
            "雑談"
        ],
        "is_mature": False
    },
    {
        "id": "40630535367",
        "user_id": "217871888",
        "user_login": "kanae_2434",
        "user_name": "叶ちゃんねる",
        "game_id": "32982",
        "game_name": "Grand Theft Auto V",
        "type": "live",
        "title": "【ストグラ 42日目】さいどびじねず｜無馬 かな｜※鳩禁",
        "viewer_count": 19239,
        "started_at": "2023-09-18T08:46:57Z",
        "language": "ja",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_kanae_2434-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "日本語"
        ],
        "is_mature": False
    },
    {
        "id": "40630158263",
        "user_id": "707328484",
        "user_login": "gosegugosegu",
        "user_name": "고세구___",
        "game_id": "509658",
        "game_name": "Just Chatting",
        "type": "live",
        "title": "5시) 생생고갈통",
        "viewer_count": 19083,
        "started_at": "2023-09-18T06:59:56Z",
        "language": "ko",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_gosegugosegu-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "코리안쿠소가키",
            "Vtuber",
            "이세계아이돌",
            "koreankusogaki",
            "트국가부른애",
            "갑니다",
            "KAWAII",
            "한국어"
        ],
        "is_mature": False
    },
    {
        "id": "49315260141",
        "user_id": "552120296",
        "user_login": "zackrawrr",
        "user_name": "zackrawrr",
        "game_id": "653624336",
        "game_name": "Lies of P",
        "type": "live",
        "title": "NEWS/LIES OF P 3 @StarforgeSystems @MadMushroomGG @MythicTalent",
        "viewer_count": 17894,
        "started_at": "2023-09-18T04:47:56Z",
        "language": "en",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_zackrawrr-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "English",
            "OTK",
            "otknetwork",
            "StarForgePCs",
            "WorldfofWarcraft",
            "wow",
            "bald"
        ],
        "is_mature": False
    }
]

invalid_stream_data = [
    {
        "started_at": "2023-09-18T02:55:51Z",
        "language": "ko",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_kimdduddi-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": 123,
        "is_mature": False
    },
    {
        "id": "40630765239",
        "user_id": "203654142",
        "user_login": "fantasista_jp",
        "user_name": "ファン太",
        "game_id": "32982",
        "game_name": "Grand Theft Auto V",
        "type": "live",
        "title": "ストグラ42日～憧れのyour my slender～鳩禁止",
        "viewer_count": 22959,
        "started_at": "2023-09-18T09:45:52Z",
        "language": "ja",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_fantasista_jp-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "日本語",
            "雑談"
        ],
        "is_mature": False
    },
    {
        "id": "40630535367",
        "user_id": "217871888",
        "user_login": "kanae_2434",
        "user_name": "叶ちゃんねる",
        "game_id": "32982",
        "game_name": "Grand Theft Auto V",
        "type": "live",
        "title": "【ストグラ 42日目】さいどびじねず｜無馬 かな｜※鳩禁",
        "viewer_count": 19239,
        "started_at": "2023-09-18T08:46:57Z",
        "language": "ja",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_kanae_2434-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "日本語"
        ],
        "is_mature": False
    },
    {
        "id": "40630158263",
        "user_id": "707328484",
        "user_login": "gosegugosegu",
        "user_name": "고세구___",
        "game_id": "509658",
        "game_name": "Just Chatting",
        "type": "live",
        "title": "5시) 생생고갈통",
        "viewer_count": 19083,
        "started_at": "2023-09-18T06:59:56Z",
        "language": "ko",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_gosegugosegu-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "코리안쿠소가키",
            "Vtuber",
            "이세계아이돌",
            "koreankusogaki",
            "트국가부른애",
            "갑니다",
            "KAWAII",
            "한국어"
        ],
        "is_mature": False
    },
    {
        "id": "49315260141",
        "user_id": "552120296",
        "user_login": "zackrawrr",
        "user_name": "zackrawrr",
        "game_id": "653624336",
        "game_name": "Lies of P",
        "type": "live",
        "title": "NEWS/LIES OF P 3 @StarforgeSystems @MadMushroomGG @MythicTalent",
        "viewer_count": 17894,
        "started_at": "2023-09-18T04:47:56Z",
        "language": "en",
        "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_zackrawrr-{width}x{height}.jpg",
        "tag_ids": [],
        "tags": [
            "English",
            "OTK",
            "otknetwork",
            "StarForgePCs",
            "WorldfofWarcraft",
            "wow",
            "bald"
        ],
        "is_mature": False
    }
]

response_body = """
<!DOCTYPE html>
<html>
<head>
    <title>Lamoda Products</title>
</head>
<body>
    <h1 class="d-catalog-header__title-text">Category Name</h1>
    
    <div class="x-product-card__card">
        <a href="/product/1">Product 1</a>
        <div class="x-product-card-description__brand-name">Brand 1</div>
        <div class="x-product-card-description__product-name">Product Name 1</div>
        <span class="x-product-card-description__price-WEB8507_price_no_bold">$19.99</span>
    </div>
    
    <div class="x-product-card__card">
        <a href="/product/2">Product 2</a>
        <div class="x-product-card-description__brand-name">Brand 2</div>
        <div class="x-product-card-description__product-name">Product Name 2</div>
        <span class="x-product-card-description__price-WEB8507_price_no_bold">$29.99</span>
    </div>
</body>
</html>
"""


@pytest.fixture
def database():
    return MongoClient().db


@pytest.fixture
def twitch_stream_dao(database):
    return TwitchStreamDAO(database)


@pytest.fixture
def lamoda_item_dao(database):
    return LamodaItemDAO(database)
