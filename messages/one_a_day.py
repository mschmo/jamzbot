from .message import FeedMessage


class OneADay(FeedMessage):
    feed_url = 'http://feeds.feedburner.com/blogspot/oneaday?format=xml'
    posted_file = 'posted/one_a_day.txt'

    def get_message(self):
        entry = self.get_feed().entries[0]
        if self.not_posted(entry.id.split('=')[-1]):
            summary = entry.summary.encode('utf-8').split('<br />', 1)[1].replace(' [&#8230;]', '...')
            message = '*- SONG OF THE DAY -*\n<{link}|{title}>\n{summary}...'.format(
                link=entry.link.encode('utf-8'),
                title=entry.title.encode('utf-8'),
                summary=summary)

            song_link = entry.get('feedburner_origenclosurelink')
            if song_link:
                message = '{message}\n:musical_note:<{song}|Listen Here>:musical_note:'.format(
                    message=message, song=song_link)

            return message