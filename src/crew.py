import json
import random

from agents import (
    ContentCreatorAgent,
    HashtagResearcherAgent,
    SchedulerAgent,
    AnalyticsAgent,
)


class Crew:
    def __init__(self, topics_file="data/topics.txt"):
        self.topics = self._load_topics(topics_file)

        # Initialize agents
        self.creator = ContentCreatorAgent()
        self.hashtagger = HashtagResearcherAgent()
        self.scheduler = SchedulerAgent()
        self.analytics = AnalyticsAgent()

        # Platforms we will support
        self.platforms = ["twitter", "linkedin", "instagram"]

    # -----------------------------
    # Load topics
    # -----------------------------
    def _load_topics(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            topics = [line.strip() for line in f.readlines() if line.strip()]
        return topics

    # -----------------------------
    # Main Workflow
    # -----------------------------
    def run(self):
        print("Running Crew...")

        # Step 1 — Pick topics (random sample)
        selected_topics = random.sample(self.topics, 4)

        # Step 2 — Create 12 posts (4 per platform)
        posts = []
        for topic in selected_topics:
            for platform in self.platforms:
                post_text = self.creator.generate_post(topic, platform)
                hashtags = self.hashtagger.generate_hashtags(topic)

                posts.append({
                    "topic": topic,
                    "platform": platform,
                    "content": post_text,
                    "hashtags": hashtags
                })

        # Step 3 — Generate schedule for these 12 posts
        schedule = self.scheduler.create_month_schedule(num_posts=len(posts))

        # Attach schedule to each post
        for i, post in enumerate(posts):
            post["scheduled_time"] = schedule[i]

        # Step 4 — Save content calendar
        self.save_calendar(posts)

        # Step 5 — Generate analytics
        analytics = self.analytics.simulate_engagement(posts)
        self.analytics.save_report(analytics)

        print("Crew finished. Calendar + analytics generated.")
        return posts, analytics

    # -----------------------------
    # Save Content Calendar
    # -----------------------------
    def save_calendar(self, posts, filename="outputs/content_calendar.json"):
        with open(filename, "w") as f:
            json.dump(posts, f, indent=4)
