 
import telegram
from telegram import Bot
from telegram.error import TelegramError

def send_tweet(self, chat, tweet):
    try:
        self.logger.debug("Sending tweet {} to chat {}...".format(
            tweet.tw_id, chat.chat_id
        ))

        '''
        Use a soft-hyphen to put an invisible link to the first
        image in the tweet, which will then be displayed as preview
        '''
        photo_url = ''
        if tweet.photo_url:
            photo_url = '[\xad](%s)' % tweet.photo_url

        created_dt = utc.localize(tweet.created_at)
        if chat.timezone_name is not None:
            tz = timezone(chat.timezone_name)
            created_dt = created_dt.astimezone(tz)
        created_at = created_dt.strftime('%Y-%m-%d %H:%M:%S %Z')
        self.sendMessage(
            chat_id=chat.chat_id,
            disable_web_page_preview=not photo_url,
            text="""
{link_preview}*{name}* ([@{screen_name}](https://twitter.com/{screen_name})) at {created_at}:
{text}
-- [Link to this Tweet](https://twitter.com/{screen_name}/status/{tw_id})
"""
                .format(
                link_preview=photo_url,
                text=prepare_tweet_text(tweet.text),
                name=escape_markdown(tweet.name),
                screen_name=tweet.screen_name,
                created_at=created_at,
                tw_id=tweet.tw_id,
            ),
            parse_mode=telegram.ParseMode.MARKDOWN)

    except TelegramError as e:
        self.logger.info("Couldn't send tweet {} to chat {}: {}".format(
            tweet.tw_id, chat.chat_id, e.message
        ))

        delet_this = None

        if e.message == 'Bad Request: group chat was migrated to a supergroup chat':
            delet_this = True

        if e.message == "Unauthorized":
            delet_this = True

        if delet_this:
            self.logger.info("Marking chat for deletion")
            chat.delete_soon = True
            chat.save()