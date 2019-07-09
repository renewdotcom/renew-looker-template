# Declare database
connection: "analytics_db"

# Include related views
include: "summary_sample.view"

# Define explore
explore: summary_sample {}
