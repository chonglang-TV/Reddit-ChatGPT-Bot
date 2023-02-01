import praw
import asyncio
from pyGPT import PyGPT

import global_constants

async def main():
  reddit = praw.Reddit(
    client_id=global_constants.CLIENT_ID,
    client_secret=global_constants.CLIENT_SECRET,
    user_agent=global_constants.USER_AGENT,
    password=global_constants.USER_PASSWORD,
    username=global_constants.USER_NAME,
    check_for_async=False
  )

  subreddit = reddit.subreddit(global_constants.MONITOR_SUBS)

  for comment in subreddit.stream.comments(skip_existing = True):
    await process_latest_comment(comment)

async def process_latest_comment(comment):
  if comment.body.find('ai') != 0:
    return

  print('comment.body', comment.body)
  print('comment.author', comment.author)
  
  retry_count = 0
  max_retry_count = 3

  while retry_count < max_retry_count:
    try:
      chat_gpt = PyGPT(global_constants.GPT_SESSION)
      await chat_gpt.connect()
      await chat_gpt.wait_for_ready()
      answer = await chat_gpt.ask(comment.body[2:])
      print('answer:\n', answer)
      await chat_gpt.disconnect()
      await asyncio.sleep(10)
      print('--------------------------')
      break
    except Exception as e:
      retry_count = retry_count + 1
      print('retry_count', retry_count)
      print('error\n', repr(e))
      continue

  if not answer:
    return

  try:
    comment.reply(answer)
  except praw.exceptions.RedditAPIException as e:
    print('comment error\n', repr(e))


if __name__ == "__main__":
  asyncio.run(main())