
import pandas as pd

# Load existing dataset
data = pd.read_csv("learning_path_data.csv")

# All 51 Learning Paths
roadmaps = {

    "programming": {
        "C": [
            "C Programming Fundamentals",
            "Variables and Data Types",
            "Operators and Expressions",
            "Conditional Statements",
            "Loops",
            "Functions",
            "Arrays and Strings",
            "Pointers",
            "Structures",
            "Dynamic Memory Allocation",
            "File Handling",
            "Mini Project"
        ],

        "C++": [
            "C++ Fundamentals",
            "Variables and Data Types",
            "Operators and Control Flow",
            "Functions",
            "Arrays and Strings",
            "Pointers and References",
            "Object Oriented Programming",
            "Inheritance and Polymorphism",
            "STL",
            "Templates",
            "File Handling",
            "Mini Project"
        ],

        "Java": [
            "Java Fundamentals",
            "Variables and Data Types",
            "Operators and Control Flow",
            "Arrays and Strings",
            "Methods",
            "Object Oriented Programming",
            "Exception Handling",
            "Collections Framework",
            "Generics",
            "File Handling",
            "JDBC Basics",
            "Mini Project"
        ],

        "Python": [
            "Programming Fundamentals",
            "Variables and Data Types",
            "Operators",
            "Conditional Statements",
            "Loops",
            "Strings",
            "Lists and Tuples",
            "Dictionaries and Sets",
            "Functions",
            "Modules and Packages",
            "File Handling",
            "Exception Handling",
            "OOP Concepts",
            "List Comprehensions",
            "Iterators and Generators",
            "Decorators",
            "Mini Project"
        ],

        "JavaScript": [
            "JavaScript Fundamentals",
            "Variables and Data Types",
            "Operators and Control Flow",
            "Functions",
            "Arrays and Objects",
            "DOM Manipulation",
            "Event Handling",
            "Asynchronous JavaScript",
            "Fetch API",
            "ES6 Modules",
            "Error Handling",
            "Mini Project"
        ],

        "C#": [
            "C# Fundamentals",
            "Variables and Data Types",
            "Control Flow",
            "Methods",
            "Arrays and Collections",
            "Object Oriented Programming",
            "Exception Handling",
            "LINQ",
            "File Handling",
            "Async and Await",
            "Mini Project"
        ],

        "Other": [
            "Programming Fundamentals",
            "Variables and Data Types",
            "Operators",
            "Conditional Statements",
            "Loops",
            "Functions",
            "Arrays and Collections",
            "Object Oriented Programming",
            "Error Handling",
            "File Handling",
            "Debugging and Testing",
            "Mini Project"
        ]
    },

    "web": {
        "Frontend Development": [
            "HTML Fundamentals",
            "CSS Fundamentals",
            "Responsive Web Design",
            "JavaScript Fundamentals",
            "DOM Manipulation",
            "Forms and Validation",
            "Git and GitHub",
            "Working with APIs",
            "React Fundamentals",
            "React State and Props",
            "React Routing",
            "Website Deployment",
            "Frontend Project"
        ],

        "Backend Development": [
            "Backend Development Fundamentals",
            "JavaScript or Python Basics",
            "Node.js Fundamentals",
            "Express.js",
            "HTTP and REST APIs",
            "Routing and Middleware",
            "SQL and Database Basics",
            "Authentication and Authorization",
            "Input Validation and Error Handling",
            "Backend Security Fundamentals",
            "API Testing",
            "Backend Deployment",
            "Backend Project"
        ],

        "Full Stack Development": [
            "HTML Fundamentals",
            "CSS and Responsive Design",
            "JavaScript Fundamentals",
            "React Fundamentals",
            "Node.js Fundamentals",
            "Express.js",
            "REST API Development",
            "SQL Database Integration",
            "Frontend and Backend Integration",
            "Authentication",
            "Git and GitHub",
            "Full Stack Deployment",
            "Full Stack Project"
        ],

        "Other": [
            "Web Development Fundamentals",
            "HTML and CSS",
            "JavaScript Basics",
            "Responsive Design",
            "Frontend Development",
            "Backend Development Basics",
            "REST APIs",
            "Database Fundamentals",
            "Git and GitHub",
            "Authentication Basics",
            "Website Deployment",
            "Web Development Project"
        ]
    },

    "app": {
        "Android": [
            "Android Development Fundamentals",
            "Kotlin Fundamentals",
            "Android Studio Setup",
            "Activities and Lifecycle",
            "UI Design with XML or Compose",
            "Navigation and Screen Management",
            "State Management",
            "API Integration",
            "Local Storage and Room Database",
            "App Permissions",
            "Testing and Debugging",
            "Android App Project"
        ],

        "iOS": [
            "iOS Development Fundamentals",
            "Swift Fundamentals",
            "Xcode Basics",
            "SwiftUI Fundamentals",
            "Views and Layouts",
            "Navigation and State",
            "API Integration",
            "Local Data Storage",
            "App Architecture",
            "Testing and Debugging",
            "App Store Basics",
            "iOS App Project"
        ],

        "Flutter": [
            "Flutter Fundamentals",
            "Dart Programming",
            "Flutter Widgets",
            "Layouts and UI Design",
            "Navigation and Routing",
            "State Management",
            "API Integration",
            "Local Storage",
            "Firebase Basics",
            "Testing and Debugging",
            "App Deployment",
            "Flutter Project"
        ],

        "React Native": [
            "React Native Fundamentals",
            "JavaScript Fundamentals",
            "Components and Props",
            "Styling and Layouts",
            "Navigation",
            "State Management",
            "API Integration",
            "Device Features",
            "Local Storage",
            "Testing and Debugging",
            "App Deployment",
            "React Native Project"
        ],

        "Other": [
            "Mobile App Development Fundamentals",
            "Mobile UI Design",
            "Components and Layouts",
            "Navigation",
            "State Management",
            "API Integration",
            "Local Database",
            "Authentication",
            "Testing and Debugging",
            "App Deployment",
            "Mobile App Project"
        ]
    },

    "dsa": {
        "C++": [
            "C++ Fundamentals for DSA",
            "Time and Space Complexity",
            "Arrays",
            "Strings",
            "Searching and Sorting",
            "Hashing",
            "Linked Lists",
            "Stacks and Queues",
            "Recursion and Backtracking",
            "Trees and Binary Search Trees",
            "Graphs",
            "Greedy Algorithms",
            "Dynamic Programming",
            "Problem Solving Practice"
        ],

        "Java": [
            "Java Fundamentals for DSA",
            "Time and Space Complexity",
            "Arrays and Strings",
            "Searching and Sorting",
            "HashMap and HashSet",
            "Linked Lists",
            "Stacks and Queues",
            "Recursion and Backtracking",
            "Trees and Binary Search Trees",
            "Graphs",
            "Greedy Algorithms",
            "Dynamic Programming",
            "Problem Solving Practice"
        ],

        "Python": [
            "Python Fundamentals for DSA",
            "Time and Space Complexity",
            "Lists and Strings",
            "Searching and Sorting",
            "Dictionaries and Sets",
            "Linked Lists",
            "Stacks and Queues",
            "Recursion and Backtracking",
            "Trees and Binary Search Trees",
            "Graphs",
            "Greedy Algorithms",
            "Dynamic Programming",
            "Problem Solving Practice"
        ],

        "Other": [
            "DSA Fundamentals",
            "Time and Space Complexity",
            "Arrays and Strings",
            "Searching and Sorting",
            "Hashing",
            "Linked Lists",
            "Stacks and Queues",
            "Recursion",
            "Trees",
            "Graphs",
            "Greedy Algorithms",
            "Dynamic Programming",
            "Problem Solving Practice"
        ]
    },

    "aiml": {
        "AI": [
            "Introduction to Artificial Intelligence",
            "Python for AI",
            "Mathematics for AI",
            "Problem Solving and Search",
            "Knowledge Representation",
            "Machine Learning Fundamentals",
            "Neural Network Basics",
            "Natural Language Processing Basics",
            "Computer Vision Basics",
            "Large Language Model Fundamentals",
            "AI API Integration",
            "AI Project"
        ],

        "ML": [
            "Python for Machine Learning",
            "NumPy and Pandas",
            "Data Cleaning",
            "Data Visualization",
            "Statistics for Machine Learning",
            "Supervised Learning",
            "Unsupervised Learning",
            "Feature Engineering",
            "Model Training",
            "Model Evaluation",
            "Scikit-learn",
            "Model Deployment",
            "Machine Learning Project"
        ],

        "Deep Learning": [
            "Python Fundamentals",
            "NumPy Fundamentals",
            "Machine Learning Basics",
            "Neural Network Fundamentals",
            "Activation Functions and Backpropagation",
            "TensorFlow or PyTorch",
            "Convolutional Neural Networks",
            "Sequence Models",
            "Transformer Fundamentals",
            "Model Training and Evaluation",
            "Deep Learning Project"
        ],

        "Generative AI": [
            "Python Fundamentals",
            "Machine Learning Basics",
            "Neural Network Fundamentals",
            "Large Language Models",
            "Transformer Architecture",
            "Prompt Engineering",
            "Embeddings",
            "Vector Databases",
            "Retrieval Augmented Generation",
            "Working with AI APIs",
            "AI Evaluation and Responsible Use",
            "Generative AI Project"
        ]
    },

    "data": {
        "Data Science": [
            "Python Fundamentals",
            "NumPy",
            "Pandas",
            "Data Cleaning",
            "SQL Fundamentals",
            "Statistics and Probability",
            "Data Visualization",
            "Exploratory Data Analysis",
            "Machine Learning Fundamentals",
            "Model Evaluation",
            "Data Science Project"
        ],

        "Data Analytics": [
            "Excel Fundamentals",
            "Advanced Excel",
            "SQL Fundamentals",
            "Data Cleaning",
            "Descriptive Statistics",
            "Data Analysis Techniques",
            "Power BI or Tableau",
            "Dashboard Development",
            "Python for Data Analysis",
            "Business Metrics",
            "Data Analytics Project"
        ],

        "Data Visualization": [
            "Data Visualization Fundamentals",
            "Charts and Graphs",
            "Excel Visualization",
            "Python for Visualization",
            "Matplotlib Basics",
            "Interactive Visualizations",
            "Power BI Fundamentals",
            "Tableau Fundamentals",
            "Dashboard Design",
            "Data Storytelling",
            "Visualization Project"
        ],

        "Other": [
            "Data Fundamentals",
            "Excel Basics",
            "SQL Fundamentals",
            "Python Basics",
            "Data Cleaning",
            "Statistics Basics",
            "Data Analysis",
            "Data Visualization",
            "Exploratory Data Analysis",
            "Dashboard Development",
            "Data Project"
        ]
    },

    "design": {
        "UI Design": [
            "UI Design Fundamentals",
            "Design Principles",
            "Typography",
            "Color Theory",
            "Spacing and Layout",
            "Figma Fundamentals",
            "Wireframing",
            "UI Components",
            "Responsive UI Design",
            "Prototyping",
            "Design Systems",
            "UI Portfolio Project"
        ],

        "UX Design": [
            "UX Design Fundamentals",
            "User Research",
            "User Personas",
            "User Journey Mapping",
            "Information Architecture",
            "User Flows",
            "Wireframing",
            "Prototyping",
            "Usability Testing",
            "Accessibility Fundamentals",
            "UX Case Study"
        ],

        "Logo Design": [
            "Logo Design Fundamentals",
            "Brand Identity Basics",
            "Design Research",
            "Typography",
            "Shapes and Composition",
            "Color Theory",
            "Vector Design",
            "Illustrator or Inkscape",
            "Logo Variations",
            "Brand Guidelines",
            "Logo Design Project"
        ],

        "Graphic Design Tools": [
            "Graphic Design Fundamentals",
            "Canva Basics",
            "Photoshop Basics",
            "Illustrator Basics",
            "Typography",
            "Color Theory",
            "Layout and Composition",
            "Image Editing",
            "Social Media Design",
            "Exporting Design Files",
            "Graphic Design Portfolio"
        ],

        "Other": [
            "Graphic Design Fundamentals",
            "Design Principles",
            "Typography",
            "Color Theory",
            "Layout and Composition",
            "Canva or Figma",
            "Image Editing",
            "Basic Prototyping",
            "Design Portfolio",
            "Practical Design Project"
        ]
    },

    "project": {
        "Web Projects": [
            "Web Project Planning",
            "HTML Fundamentals",
            "CSS and Responsive Design",
            "JavaScript Fundamentals",
            "Git and GitHub",
            "Frontend Development",
            "API Integration",
            "Backend Fundamentals",
            "Database Integration",
            "Authentication",
            "Testing and Debugging",
            "Web Project Deployment"
        ],

        "App Projects": [
            "App Project Planning",
            "Mobile Development Basics",
            "UI Design",
            "Navigation and Routing",
            "State Management",
            "API Integration",
            "Local Storage",
            "Authentication",
            "Testing and Debugging",
            "App Deployment",
            "Mobile App Project"
        ],

        "Python Projects": [
            "Python Fundamentals",
            "Functions and Modules",
            "File Handling",
            "Exception Handling",
            "Working with APIs",
            "Database Integration",
            "GUI or Web Framework Basics",
            "Project Structure",
            "Testing and Debugging",
            "Project Deployment",
            "Python Project"
        ],

        "AI/ML Projects": [
            "Python Fundamentals",
            "NumPy and Pandas",
            "Data Collection",
            "Data Cleaning",
            "Data Visualization",
            "Machine Learning Fundamentals",
            "Model Training",
            "Model Evaluation",
            "Application Integration",
            "Model Deployment",
            "AI/ML Project"
        ],

        "Other": [
            "Project Idea Selection",
            "Requirement Analysis",
            "Project Planning",
            "Technology Stack Selection",
            "UI Design",
            "Core Functionality Development",
            "Database and Storage",
            "Git and GitHub",
            "Testing and Debugging",
            "Project Deployment",
            "Documentation",
            "Final Project"
        ]
    },

    "cloud": {
        "AWS": [
            "Cloud Computing Fundamentals",
            "Introduction to AWS",
            "AWS Global Infrastructure",
            "AWS IAM",
            "Amazon EC2",
            "Amazon S3",
            "Amazon VPC",
            "AWS Database Services",
            "AWS Lambda",
            "Cloud Monitoring",
            "AWS Security Fundamentals",
            "AWS Deployment Project"
        ],

        "Microsoft Azure": [
            "Cloud Computing Fundamentals",
            "Introduction to Microsoft Azure",
            "Azure Global Infrastructure",
            "Azure Identity and Access",
            "Azure Virtual Machines",
            "Azure Storage",
            "Azure Virtual Network",
            "Azure Database Services",
            "Azure Functions",
            "Azure Monitoring",
            "Azure Security Fundamentals",
            "Azure Deployment Project"
        ],

        "Google Cloud": [
            "Cloud Computing Fundamentals",
            "Introduction to Google Cloud",
            "Google Cloud Infrastructure",
            "Identity and Access Management",
            "Compute Engine",
            "Cloud Storage",
            "Virtual Private Cloud",
            "Cloud SQL",
            "Cloud Functions",
            "Cloud Monitoring",
            "Cloud Security Fundamentals",
            "Google Cloud Project"
        ],

        "Other": [
            "Cloud Computing Fundamentals",
            "Cloud Service Models",
            "Cloud Deployment Models",
            "Virtualization Basics",
            "Cloud Compute Services",
            "Cloud Storage",
            "Cloud Networking",
            "Cloud Databases",
            "Identity and Access Management",
            "Cloud Security",
            "Monitoring and Deployment",
            "Cloud Project"
        ]
    },

    "cyber": {
        "Ethical Hacking": [
            "Cybersecurity Fundamentals",
            "Ethics and Legal Responsibilities",
            "Networking Fundamentals",
            "Linux Fundamentals",
            "Operating System Security",
            "Security Assessment Concepts",
            "Vulnerability Management",
            "Web Security Fundamentals",
            "Safe Security Lab Concepts",
            "Security Reporting",
            "Risk Assessment and Remediation",
            "Cybersecurity Project"
        ],

        "Network Security": [
            "Networking Fundamentals",
            "Network Protocols",
            "Network Architecture",
            "Firewalls",
            "Access Control",
            "VPN Fundamentals",
            "Encryption and TLS",
            "IDS and IPS Concepts",
            "Network Monitoring",
            "Security Logging",
            "Secure Network Configuration",
            "Network Security Project"
        ],

        "Application Security": [
            "Application Security Fundamentals",
            "Secure Software Development",
            "OWASP Top 10 Overview",
            "Input Validation",
            "Authentication and Authorization",
            "Session Security",
            "Secure API Design",
            "Dependency Management",
            "Secure Code Review",
            "Security Testing in Safe Labs",
            "Vulnerability Remediation",
            "Application Security Project"
        ],

        "Other": [
            "Cybersecurity Fundamentals",
            "Networking Basics",
            "Operating System Basics",
            "Access Control",
            "Encryption Fundamentals",
            "Secure Coding Basics",
            "Threat Awareness",
            "Security Monitoring",
            "Security Logging",
            "Incident Response Fundamentals",
            "Risk Management",
            "Cybersecurity Project"
        ]
    },

    "devops": {
        "Docker": [
            "Linux and Command Line Basics",
            "Git and GitHub",
            "Containerization Fundamentals",
            "Docker Architecture",
            "Docker Images and Containers",
            "Dockerfile",
            "Docker Compose",
            "Docker Volumes and Networking",
            "Container Registry",
            "Container Security Basics",
            "CI/CD Integration",
            "Docker Deployment Project"
        ],

        "Kubernetes": [
            "Linux Fundamentals",
            "Containerization Basics",
            "Kubernetes Fundamentals",
            "Kubernetes Architecture",
            "Pods",
            "Deployments",
            "Services",
            "ConfigMaps and Secrets",
            "Persistent Storage",
            "Scaling Applications",
            "Monitoring Basics",
            "Kubernetes Project"
        ],

        "CI/CD": [
            "Git and GitHub",
            "Software Development Lifecycle",
            "Build Automation",
            "Automated Testing",
            "CI/CD Fundamentals",
            "GitHub Actions",
            "Jenkins Fundamentals",
            "Pipeline Configuration",
            "Secrets and Environment Variables",
            "Deployment Strategies",
            "Pipeline Monitoring",
            "CI/CD Project"
        ],

        "Linux": [
            "Linux Fundamentals",
            "Linux Distributions",
            "File System Structure",
            "Basic Linux Commands",
            "Users and Permissions",
            "Process Management",
            "Services and Package Management",
            "Shell Scripting",
            "Networking Basics",
            "System Monitoring",
            "Linux Administration",
            "Linux Mini Project"
        ],

        "Other": [
            "DevOps Fundamentals",
            "Linux and Command Line",
            "Git and GitHub",
            "Scripting Basics",
            "CI/CD Fundamentals",
            "Containerization Basics",
            "Cloud Computing Basics",
            "Deployment Fundamentals",
            "Monitoring and Logging",
            "Automation Basics",
            "DevOps Project"
        ]
    }
}


# Convert roadmaps into dataset records
new_records = []

for goal, subgoals in roadmaps.items():

    for sub_goal, topics in subgoals.items():

        for sequence, topic in enumerate(topics, start=1):

            # Assign priority and estimated duration
            if sequence <= 6:
                priority = "High"
                estimated_days = 2
            else:
                priority = "Medium"
                estimated_days = 3

            new_records.append({
                "goal": goal,
                "sub_goal": sub_goal,
                "topic": topic,
                "sequence": sequence,
                "priority": priority,
                "estimated_days": estimated_days
            })


# Create DataFrame
new_data = pd.DataFrame(new_records)

# Identify all paths being updated
updated_pairs = set(
    zip(new_data["goal"], new_data["sub_goal"])
)

# Remove old records for these 51 paths
remaining_data = data[
    ~data.apply(
        lambda row: (row["goal"], row["sub_goal"]) in updated_pairs,
        axis=1
    )
]

# Combine old remaining data with new roadmaps
final_data = pd.concat(
    [remaining_data, new_data],
    ignore_index=True
)

# Save updated dataset
final_data.to_csv("learning_path_data.csv", index=False)


# Verification summary
print("\nLEARNING PATH DATASET UPDATED SUCCESSFULLY!")

print("\nTotal Learning Paths Updated:", len(updated_pairs))
print("Total Topics:", len(new_data))
print("Total Dataset Records:", len(final_data))

print("\nSub-goal-wise Topic Count:")

for goal, subgoals in roadmaps.items():

    for sub_goal in subgoals:

        count = len(
            new_data[
                (new_data["goal"] == goal) &
                (new_data["sub_goal"] == sub_goal)
            ]
        )

        print(f"PASS: {goal} - {sub_goal} : {count} topics")


print("\nFinal Columns:")
print(list(final_data.columns))

print("\nDataset Update Completed!")
