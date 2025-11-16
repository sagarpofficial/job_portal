from app import app, db, Job
import random
from datetime import datetime

# -------------------------------------------
# DATA LISTS
# -------------------------------------------
large_titles = [
    "Software Engineer", "Marketing Manager", "HR Executive", "Business Analyst",
    "Nurse", "Accountant", "Graphic Designer", "Project Manager",
    "Sales Executive", "Customer Support Specialist"
]

small_titles = [
    "Delivery Boy", "Cook", "Housekeeping Staff", "Electrician Helper",
    "Construction Worker", "Packing Assistant", "Security Guard",
    "Gardener", "Painter Helper", "Warehouse Loader"
]

locations = ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Pune", "Vizag", "Coimbatore"]
companies = ["TechCorp Solutions", "Skyline Software", "BrightFuture Pvt Ltd", "UrbanWorks", "GreenLeaf Industries"]
risk_levels = ["Low", "Medium", "High"]

# Any employer ID (from your screenshot employer ID = 4)
EMPLOYER_ID = 4


# -------------------------------------------
# CREATE LARGE JOB
# -------------------------------------------
def create_large_job():
    title = random.choice(large_titles)
    return Job(
        title=title,
        category=random.choice(["IT", "Management", "Marketing", "Healthcare", "Finance"]),
        job_type="large",
        location=random.choice(locations),
        salary=f"₹{random.randint(20000, 60000)}",
        description=f"This is a demo large job posting for {title}.",

        # Large job fields
        qualification=random.choice(["Any Degree", "Diploma", "B.Tech", "MBA"]),
        experience=random.choice(["0-1 years", "1-2 years", "2+ years"]),
        benefits=random.choice(["PF + ESI", "Travel Allowance", "Medical Insurance"]),

        company_name=random.choice(companies),
        company_address=random.choice(locations) + ", India",
        company_website="https://www.examplecompany.com",

        posted_by=EMPLOYER_ID,
        created_at=datetime.utcnow()
    )


# -------------------------------------------
# CREATE SMALL JOB
# -------------------------------------------
def create_small_job():
    title = random.choice(small_titles)
    return Job(
        title=title,
        category=random.choice(["Delivery", "Hospitality", "Labour", "Support"]),
        job_type="small",
        location=random.choice(locations),
        salary=f"₹{random.randint(8000, 20000)}",
        description=f"This is a demo small job posting for {title}.",

        # Small job fields
        salary_type=random.choice(["Daily", "Weekly", "Monthly"]),
        workplace_type=random.choice(["Field Work", "Office", "On-site"]),
        full_address=f"No. {random.randint(10,99)}, Demo Street",
        pincode=str(random.randint(500000, 699999)),
        risk_level=random.choice(risk_levels),

        tools_provided=random.choice([True, False]),
        food_provided=random.choice([True, False]),
        stay_provided=random.choice([True, False]),

        google_map_link="https://maps.app.goo.gl/example",

        posted_by=EMPLOYER_ID,
        created_at=datetime.utcnow()
    )


# -------------------------------------------
# MAIN EXECUTION
# -------------------------------------------
with app.app_context():
    print("🔄 Adding 100 demo jobs...")

    for i in range(50):
        db.session.add(create_large_job())  # 50 large jobs

    for i in range(50):
        db.session.add(create_small_job())  # 50 small jobs

    db.session.commit()

    print("✅ Successfully added 100 demo jobs!")