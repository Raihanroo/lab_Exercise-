# Lab 1: The Smart Survey Onboarding Engine
# Learning Objectives
# input() capturing and Type Casting (int)

# Conditionals (if-elif-else) and Logic Operators (and, or)

# String Interpolation (f-strings)

# Scenario
# You are building an entry portal for an automated processing system. The script must interview a human user, gather their basic profile info, and evaluate their clearance tier based on strict age rules.

# Task Instructions
# Prompt the user for their name, age, and whether they are a developer (yes/no).

# Cast the captured input data into its mathematically appropriate type.

# Apply the following tier logic rules:

# If they are under 18, assign them to "Tier 3: Guest" access.

# If they are 18 or older and they are a developer, assign them to "Tier 1: Admin Infrastructure Access".

# If they are 18 or older but not a developer, assign them to "Tier 2: Standard Executive Access".

# Output a personalized configuration summary string using an F-String.
# --- STARTER CODE ---
# 1. TODO: Capture inputs from user (Name, Age, Developer Status)


# 2. TODO: Evaluate conditional logic to determine the clearance tier


# 3. TODO: Print out the final profile card using an f-string


# # 1. Capture inputs from user (Name, Age, Developer Status)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# is_developer_input = input("Are you a developer? (yes): ").strip().lower()

# # Convert developer response to a boolean flag
# is_developer = is_developer_input == "yes"

# # 2. Evaluate conditional logic to determine the clearance tier
# if age < 18:
#     clearance_tier = "Tier 3: Guest"
# elif age >= 18 and is_developer:
#     clearance_tier = "Tier 1: Admin Infrastructure Access"
# else:
#     clearance_tier = "Tier 2: Standard Executive Access"

# # 3. Print out the final profile card using an f-string
# print(f"\n--- USER PROFILE CARD ---")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Developer Status: {'Yes' if is_developer else 'No'}")
# print(f"Assigned Clearance: {clearance_tier}")


# Lab 2: The Multi-Cluster IP Audit Tool
# Learning Objectives
# Lists (list) and Dictionaries (dict)

# Sequential Loops (for loop)

# Arithmetic Operations (Counting & Percentages)

# Scenario
# Your cloud infrastructure just generated a raw audit log of all active internal application routes. You need to parse this map to tally how many endpoints exist and evaluate system capacity variables.

# Task Instructions
# Use the provided cluster_config nested dictionary structure.

# Write a function named calculate_capacity that uses a loop to extract the item values from the active_nodes list.

# Calculate the percentage of cluster utilization:

# Utilization 
# =
# (
# Active Nodes
# Total Max Slots
# )
# ×
# 100

# Print a clean summary report using string interpolation.


# 1. Provided cluster_config nested dictionary structure
# cluster_config = {
#     "cluster_a": {
#         "max_slots": 50,
#         "active_nodes": ["10.0.0.1", "10.0.0.2", "10.0.0.5", "10.0.0.12"]
#     },
#     "cluster_b": {
#         "max_slots": 20,
#         "active_nodes": ["10.0.1.10", "10.0.1.11", "10.0.1.15"]
#     },
#     "cluster_c": {
#         "max_slots": 100,
#         "active_nodes": ["10.0.2.1", "10.0.2.2", "10.0.2.3", "10.0.2.4", "10.0.2.5"]
#     }
# }


# # 2 & 3. Function to calculate capacity using a loop
# def calculate_capacity(config):
#     total_max_slots = 0
#     total_active_nodes = 0

#     # Loop through each cluster in the dictionary
#     for cluster_name, data in config.items():
#         # Accumulate max slots
#         total_max_slots += data["max_slots"]

#         # Loop through the active_nodes list to count items sequentially
#         for node_ip in data["active_nodes"]:
#             total_active_nodes += 1

#     # 4. Calculate percentage of cluster utilization
#     if total_max_slots > 0:
#         utilization = (total_active_nodes / total_max_slots) * 100
#     else:
#         utilization = 0.0

#     return total_active_nodes, total_max_slots, utilization


# # Execute audit calculation
# active_count, max_slots_count, utilization_pct = calculate_capacity(cluster_config)

# # 5. Print clean summary report
# print("--- MULTI-CLUSTER IP AUDIT REPORT ---")
# print(f"Total Active Endpoints : {active_count}")
# print(f"Total Max Capacity     : {max_slots_count}")
# print(f"Cluster Utilization    : {utilization_pct:.2f}%")



# Lab 3: The Deployment Budget Optimizer
# Learning Objectives
# Functions with Parameters and Return values

# Arithmetic operations

# Comparative conditions (> ,<=)

# Scenario
# Your financial team wants to make sure cloud spending doesn't go overboard. You need to build a function that dynamically figures out the total monthly operational cost of setting up server groups and raises flags if things get too expensive.

# Task Instructions
# Create a function called estimate_deployment_cost that accepts three inputs: instance_count, hourly_rate_per_instance, and budget_cap.

# Compute the total cost for a standard 30-day billing month (Assume 
# 30
#  days
# ×
# 24
#  hours
# =
# 720
#  hours
#  of uptime total).

# Check the calculated cost against the budget_cap:

# If the cost exceeds the cap, return an alert string: "REJECTED: Budget Exceeded by $X!"

# If it is within budget limits, return: "APPROVED: Total Estimated Cost is $X."

# Inject the final dollar numbers inside your returned values cleanly.

# 1. Create function accepting instance count, rate, and budget cap
# def estimate_deployment_cost(instance_count, hourly_rate_per_instance, budget_cap):
#     # 3. Compute total cost for a 30-day month (720 total hours)
#     total_hours = 30 * 24
#     total_cost = instance_count * hourly_rate_per_instance * total_hours

#     # 4. Check calculated cost against budget_cap
#     if total_cost > budget_cap:
#         overage = total_cost - budget_cap
#         # Return REJECTED message with dollar values formatted to 2 decimal places
#         return f"REJECTED: Budget Exceeded by ${overage:.2f}!"
#     else:
#         # Return APPROVED message
#         return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."


# # --- Example Test Cases ---

# # Case 1: Exceeds Budget
# test1 = estimate_deployment_cost(
#     instance_count=5, 
#     hourly_rate_per_instance=0.75, 
#     budget_cap=2500.00
# )
# print(test1)
# # Output: REJECTED: Budget Exceeded by $200.00!

# # Case 2: Within Budget
# test2 = estimate_deployment_cost(
#     instance_count=3, 
#     hourly_rate_per_instance=0.50, 
#     budget_cap=1200.00
# )
# print(test2)
# Output: APPROVED: Total Estimated Cost is $1080.00.


# Lab 4: The Profile Text Normalization Pipeline
# Learning Objectives
# Strings and String Methods (.strip(), .lower())

# Lists and Loops

# Appending dynamic modifications to lists

# Scenario
# A user filled out a human survey, but their input text is completely disorganized. There are erratic spaces everywhere, and the casing style is messy. You need to clean this text array before passing it downstream into production environments.

# Task Instructions
# Loop through the raw list of unformatted data inputs.

# For every item, remove any unnecessary background whitespace characters on the sides and force all lettering into complete lowercase.

# Store the cleaned results dynamically into a new list named sanitized_records.

# Output both lists to the terminal to visually verify the conversion results.

# Raw unformatted survey input data with erratic spaces and inconsistent casing
# raw_records = [
#     "   John_Doe_99   ",
#     "ADMIN_INFRASTRUCTURE",
#     "  dev_ops_Lead ",
#     "SYSTEM_ANALYSIS  ",
#     "  user_Executive  "
# ]

# # 4. Initialize empty list to store cleaned results
# sanitized_records = []

# # 1. Loop through the raw list of unformatted data inputs
# for record in raw_records:
#     # 3. Strip whitespace from both ends and convert to lowercase
#     cleaned_record = record.strip().lower()
    
#     # Append dynamic modifications to the new list
#     sanitized_records.append(cleaned_record)

# # 5. Output both lists to the terminal to visually verify the conversion results
# print("--- RAW UNFORMATTED RECORDS ---")
# print(raw_records)

# print("\n--- SANITIZED RECORDS ---")
# print(sanitized_records)


# Lab 5: System Alert Flag Evaluator
# Learning Objectives
# Complex boolean evaluations (and, not, or)

# Logical comparisons and flag validation

# Control execution states

# Scenario
# You are developing an automated error monitoring daemon. It continuously looks at a series of active machine flags to evaluate whether an urgent maintenance engineer needs to be page-alerted out of bed.

# Task Instructions
# Look at the three telemetry boolean flags provided in the scenario block below.

# Create an overriding rule condition to trigger an alert (should_alert = True) if any of the following logical evaluations are met:

# The server status is not active (is_active is False).
# The CPU utilization is critically high (cpu_percent > 90.0) and it is a critical environment (is_production is True).
# Use conditional flows to broadcast the final verdict statement cleanly.

# 1. Telemetry boolean flags and sensor readings
# is_active = True
# cpu_percent = 94.5
# is_production = True

# # 2 & 3. Complex boolean evaluation rule logic
# # Alert triggers if:
# # - Server is NOT active (not is_active)
# # OR
# # - CPU is critically high AND it is production (cpu_percent > 90.0 and is_production)
# should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# # 4. Use conditional flows to broadcast the final verdict statement cleanly
# print("--- SYSTEM TELEMETRY AUDIT ---")
# print(f"Active Status : {is_active}")
# print(f"CPU Load      : {cpu_percent}%")
# print(f"Production Env: {is_production}")
# print("-" * 30)

# if should_alert:
#     print("VERDICT: 🚨 URGENT ALERT - Paging Maintenance Engineer!")
# else:
#     print("VERDICT: ✅ SYSTEM NOMINAL - No Alert Required.")