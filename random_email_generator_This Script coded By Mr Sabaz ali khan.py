# Random Email Generator
# Coded by Mr Sabaz Ali Khan

import random
import string
import csv

def generate_random_email(num_emails):
    """Generate a specified number of random email addresses."""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    emails = []
    
    for _ in range(num_emails):
        # Generate random name (4 to 15 characters)
        name_length = random.randint(4, 15)
        name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(name_length))
        # Choose random domain
        domain = random.choice(domains)
        # Combine to form email
        email = f"{name}@{domain}"
        emails.append(email)
    
    return emails

def save_emails_to_csv(emails, filename="emails.csv"):
    """Save generated emails to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Email Address"])
        for email in emails:
            writer.writerow([email])

if __name__ == "__main__":
    # Generate 1000 random emails (adjust as needed)
    generated_emails = generate_random_email(1000)
    # Save to CSV
    save_emails_to_csv(generated_emails)
    print(f"Generated {len(generated_emails)} emails and saved to emails.csv")