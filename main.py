import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    username="YOUR_REDDIT_USERNAME",
    password="YOUR_PASSWORD",
    user_agent="script:reddit-analysis:v1.0 (by u/YOUR_USERNAME)"
)

subreddit = reddit.subreddit("all")
for post in subreddit.hot(limit=10):
    print(post.title)
