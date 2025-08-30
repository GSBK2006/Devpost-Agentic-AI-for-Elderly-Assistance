from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def send_reminder(user_id, medicine):
    print(f"Reminder for user {user_id}: Take {medicine}")

# Example: schedule a reminder at 8 AM daily
scheduler.add_job(send_reminder, 'cron', hour=8, args=[1, "Metformin"])
scheduler.start()
