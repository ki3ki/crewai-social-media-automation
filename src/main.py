from crew import Crew

def main():
    print("\n=== Social Media Multi-Agent System ===\n")

    crew = Crew()
    posts, analytics = crew.run()

    print("\nContent calendar saved to: outputs/content_calendar.json")
    print("Analytics report saved to: outputs/analytics_report.json\n")
    print("Done!")

if __name__ == "__main__":
    main()

