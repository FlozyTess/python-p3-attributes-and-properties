#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=None):
        self.name = None  # Ensure attributes always exist
        self.job = None  

        # Validate job first if name is empty (fixes job test issue)
        if not name:
            if job and job not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                return
            self.job = job  # Assign job if valid
            print("Name must be string between 1 and 25 characters.")  # Name validation still happens
            return
        
        # Validate name
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        
        self.name = name.title()  # Convert to title case

        # Validate job
        if job and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return

        self.job = job  # Assign job if valid

# Example usage
if __name__ == "__main__":
    guido = Person(name="Guido van Rossum", job="ITC")
    print(f"Person created: {guido.name}, {guido.job}")