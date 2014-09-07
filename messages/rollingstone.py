from .message import FeedMessage


class RollingStone(FeedMessage):
    feed_url = 'http://www.rollingstone.com/music.rss'
    posted_file = 'messages/posted/rollingstone.txt'

    def get_message(self):
        entry = self.get_feed()['items'][0]
        if self.not_posted(entry.id.split('/')[-1]):
            return '*{title}*\n{summary}... <{link}|continue reading>'.format(
                title=entry.title.encode('utf-8'),
                summary=entry.summary.encode('utf-8'),
                link=entry.link.encode('utf-8'))