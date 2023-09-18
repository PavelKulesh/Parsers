from tests.conftest import twitch_stream_dao, valid_stream_data, invalid_stream_data


def test_valid_data_create_or_update(twitch_stream_dao):
    result = twitch_stream_dao.create_or_update(valid_stream_data)

    assert len(result) == len(valid_stream_data)


def test_invalid_data_create_or_update(twitch_stream_dao):
    result = twitch_stream_dao.create_or_update(invalid_stream_data)

    assert len(result) != len(invalid_stream_data)


def test_read(twitch_stream_dao):
    twitch_stream_dao.create_or_update(valid_stream_data)

    result = twitch_stream_dao.read(4)

    assert result is not None
    assert len(result) == 4
