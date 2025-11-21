import random
import json
from datetime import datetime, timedelta


# -----------------------------
# Content Creator Agent
# -----------------------------
class ContentCreatorAgent:
    def __init__(self):
        pass

    def generate_post(self, topic, platform):
        """Generate a simple platform-specific post."""
        base = f"Here’s a quick tip about {topic}."
        
        if platform == "twitter":
            return base[:240]  # keep it short
        elif platform == "linkedin":
            return f"{base}\n\nIn today's world, continuous learning matters!"
        elif platform == "instagram":
            return f"{base} 😊\n#LearningJourney #DeveloperLife"
        else:
            return base


# -----------------------------
# Hashtag Researcher Agent
# -----------------------------
class HashtagResearcherAgent:
    def __init__(self):
        pass

    def generate_hashtags(self, topic):
        """Generate 3 simple hashtags based on the topic."""
        key = topic.split()[0].lower()  # take first word
        hashtags = [f"#{key}", f"#{key}tips", f"#{key}learning"]
        return hashtags


# -----------------------------
# Scheduler Agent
# -----------------------------
class SchedulerAgent:
    def __init__(self):
        pass

    def create_month_schedule(self, num_posts=12):
        """
        Generate a 1-month schedule with random posting times.
        Creates sparse calendar: 12 posts across the month.
        """
        today = datetime.now().date()
        schedule = []

        for i in range(num_posts):
            # random day in next 30 days
            day_offset = random.randint(1, 30)
            post_date = today + timedelta(days=day_offset)

            # random hour between 9am–6pm
            hour = random.randint(9, 18)
            scheduled_time = datetime(
                post_date.year, post_date.month, post_date.day, hour, 0
            )

            schedule.append(scheduled_time.isoformat())

        return schedule


# -----------------------------
# Analytics Agent
# -----------------------------
class AnalyticsAgent:
    def __init__(self):
        pass

    def simulate_engagement(self, posts):
        """
        Create simple dummy analytics.
        Returns: views, likes, comments for each post.
        """
        analytics = []

        for post in posts:
            analytics.append({
                "platform": post["platform"],
                "topic": post["topic"],
                "views": random.randint(100, 2000),
                "likes": random.randint(10, 400),
                "comments": random.randint(0, 50),
            })

        return analytics

    def save_report(self, analytics, filename="outputs/analytics_report.json"):
        with open(filename, "w") as f:
            json.dump(analytics, f, indent=4)
