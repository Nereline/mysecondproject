import helpers.feed_helper as feed_helper


class TestFeed:
    @staticmethod
    def test_get_feed_v3(session):
        resp = feed_helper.Feed.get_feed_v3(session.session)
        assert resp['Success'] is True, f"Запрос не успешен. " \
                                        f"Фактический результа выполнения запроса {resp['Success']}"
        assert resp['Result'] is not None, "Нет событий в ленте"
