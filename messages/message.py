import os
import feedparser


class FeedMessage():
    feed_url = None
    posted_file = None

    def get_feed(self):
        return feedparser.parse(self.feed_url)

    def not_posted(self, item_id):
        file_path = '{directory}/{path}'.format(
            directory=os.path.dirname(os.path.abspath(__file__)),
            path=self.posted_file)
        with open(file_path, 'r+') as f:
            if item_id == f.read():
                return False
            f.seek(0)
            f.write(item_id)
            f.truncate()
        return True