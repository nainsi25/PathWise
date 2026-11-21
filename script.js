// ==========================================
// PATHWISE - PERSONALIZED LEARNING PATH
// ==========================================
// // ===== API URL =====

const API_URL = "https://pathwise-vwou.onrender.com";

// ==========================================
// 1. LEARNING GOAL AND SUB-GOAL DROPDOWN
// ==========================================

const goalSelect = document.getElementById("goal");

const subGoalGroup = document.getElementById("subGoalGroup");

const subGoalSelect = document.getElementById("subGoal");

const subGoalOptions = {

    web: [
        "Frontend Development",
        "Backend Development",
        "Full Stack Development",
        "Other"
    ],

    app: [
        "Android",
        "iOS",
        "Flutter",
        "React Native",
        "Other"
    ],

    programming: [
        "C",
        "C++",
        "Java",
        "Python",
        "JavaScript",
        "C#",
        "Other"
    ],

    dsa: [
        "C++",
        "Java",
        "Python",
        "Other"
    ],

    aiml: [
        "AI",
        "ML",
        "Deep Learning",
        "Generative AI"
    ],

    data: [
        "Data Science",
        "Data Analytics",
        "Data Visualization",
        "Other"
    ],

    design: [
        "UI Design",
        "UX Design",
        "Logo Design",
        "Graphic Design Tools",
        "Other"
    ],

    project: [
        "Web Projects",
        "App Projects",
        "Python Projects",
        "AI/ML Projects",
        "Other"
    ],

    cloud: [
        "AWS",
        "Microsoft Azure",
        "Google Cloud",
        "Other"
    ],

    cyber: [
        "Ethical Hacking",
        "Network Security",
        "Application Security",
        "Other"
    ],

    devops: [
        "Docker",
        "Kubernetes",
        "CI/CD",
        "Linux",
        "Other"
    ],

    gate: ["GATE CSE"],

    tcsnqt: [
        "Foundation",
        "Advanced",
        "Programming"
    ],

    nimcet: [
        "Mathematics",
        "Logical Reasoning",
        "Computer Awareness",
        "English"
    ],

    cuetpg: [
        "Computer Science",
        "Information Technology"
    ]

};


// Update Sub-goal Dropdown

goalSelect.addEventListener("change", function () {

    const selectedGoal = goalSelect.value;

    subGoalSelect.innerHTML =
        '<option value="">Select an option</option>';

    if (subGoalOptions[selectedGoal]) {

        subGoalGroup.hidden = false;

        subGoalSelect.required = true;

        subGoalOptions[selectedGoal].forEach(function (option) {

            const newOption = document.createElement("option");

            newOption.value = option;

            newOption.textContent = option;

            subGoalSelect.appendChild(newOption);

        });

    } else {

        subGoalGroup.hidden = true;

        subGoalSelect.required = false;

        subGoalSelect.value = "";

    }

});


// ==========================================
// 2. GET STARTED BUTTON
// ==========================================

function startLearning() {

    document.getElementById("learning").scrollIntoView({

        behavior: "smooth"

    });

}


// ==========================================
// 3. ML LEARNING PATH GENERATOR
// ==========================================

const learningForm = document.getElementById("learningForm");

const learningResult = document.getElementById("learningResult");


learningForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const goal = document.getElementById("goal").value;

    const subGoal = document.getElementById("subGoal").value;

    const availableDays = Number(
        document.getElementById("days").value
    );

    const dailyHours = Number(
        document.getElementById("hours").value
    );
    console.log("Selected Goal:", goal);
    console.log("Selected Sub Goal:", subGoal);
    console.log("Available Days:", availableDays);
    console.log("Daily Hours:", dailyHours);

    // Technical exam paths are not available yet

    const examGoals = [
        "gate",
        "tcsnqt",
        "nimcet",
        "cuetpg"
    ];


    if (examGoals.includes(goal)) {

        learningResult.innerHTML = `

            <h3>Exam Learning Path</h3>

            <p>
                Learning path for this exam is not available yet.
                We will add it in a future update.
            </p>

        `;

        learningResult.hidden = false;

        return;

    }


    // Show loading message

    learningResult.hidden = false;

    learningResult.innerHTML = `

        <h3>Generating Your Learning Path...</h3>

        <p>Please wait while we prepare your personalized roadmap.</p>

    `;


    try {

        // Send data to Flask ML API

        const response = await fetch(
            `${API_URL}/recommend-learning-path`,
            {

                method: "POST",
                credentials: "include",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    goal: goal,

                    sub_goal: subGoal,

                    available_days: availableDays,

                    daily_hours: dailyHours

                })

            }
        );


        const result = await response.json();


        if (!response.ok) {

            throw new Error(
                result.error || "Learning path could not be generated."
            );

        }


        // Generate Topics HTML

        const topicsHTML = result.learning_path.map(function (item) {

            return `

                <li>

                    <strong>${item.topic}</strong>

                    <p>Priority: ${item.priority}</p>

                    <p>Estimated Days: ${item.estimated_days}</p>

                </li>

            `;

        }).join("");


        // Display Learning Path

        learningResult.innerHTML = `

            <h3>Your Personalized Learning Path</h3>

            <div class="learning-summary">

                <p>
                    <strong>Goal:</strong>
                    ${result.goal}
                </p>

                <p>
                    <strong>Sub Goal:</strong>
                    ${result.sub_goal}
                </p>

                <p>
                    <strong>Available Days:</strong>
                    ${result.available_days}
                </p>

                <p>
                    <strong>Daily Study Hours:</strong>
                    ${result.daily_hours}
                </p>

                <p>
                    <strong>Total Topics:</strong>
                    ${result.total_topics}
                </p>

                <p>
                    <strong>Estimated Study Hours:</strong>
                    ${result.total_hours}
                </p>

                <p>
                    <strong>Required Days:</strong>
                    ${result.required_days}
                </p>

                <h4>Status: ${result.status}</h4>

            </div>


            <h4>Your Learning Roadmap</h4>

            <ol>

                ${topicsHTML}

            </ol>

        <button type="button" id="deleteLearningPath">
        Delete Learning Path
        </button>    

        `;


        learningResult.hidden = false;


        learningResult.scrollIntoView({

            behavior: "smooth",

            block: "start"

        });


    } catch (error) {

        learningResult.innerHTML = `

            <h3>Something went wrong!</h3>

            <p>${error.message}</p>

        `;

        console.error("Learning Path Error:", error);

    }

});

// ==========================================
// DELETE LEARNING PATH
// ==========================================

learningResult.addEventListener("click", async function(event) {

    if (event.target.id !== "deleteLearningPath") {
        return;
    }

    const confirmDelete = confirm(
        "Are you sure you want to delete your Learning Path?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/delete-learning-path`,
            {
                method: "DELETE",
                credentials: "include"
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error);
        }

        learningResult.innerHTML = "";
        learningResult.hidden = true;

        alert("Learning Path deleted successfully!");

    } catch (error) {

        console.error("Delete Learning Path Error:", error);

        alert(error.message);

    }

});

// ==========================================
// 4. DAILY PLANNER
// ==========================================

const taskForm = document.getElementById("taskForm");

const taskList = document.getElementById("taskList");


// Add New Task

taskForm.addEventListener("submit", async function (event) {

    event.preventDefault();


    const task = {

        name: document.getElementById("taskName").value,

        subject: document.getElementById("taskSubject").value,

        date: document.getElementById("taskDate").value

    };


    try {

        const response = await fetch(`${API_URL}/add-task`, {

            method: "POST",

            credentials: "include",

             headers: {
            "Content-Type": "application/json"
             },

            body: JSON.stringify(task)

        });


        if (!response.ok) {

            throw new Error("Task could not be saved.");

        }


        


        taskForm.reset();


        loadTasks();


    } catch (error) {

        alert("Error saving task. Please check the server.");

        console.error(error);

    }

});



// Load Tasks

async function loadTasks() {

    try {

        const response = await fetch(`${API_URL}/get-tasks`, {
             credentials: "include"
        });


        if (!response.ok) {

            throw new Error("Could not load tasks.");

        }


        const tasks = await response.json();


        displayTasks(tasks);


    } catch (error) {

        console.error("Error loading tasks:", error);

    }

}



// Display Tasks

function displayTasks(tasks) {

    taskList.innerHTML = "";

    if (tasks.length === 0) {
        taskList.innerHTML = "<p>No tasks added yet.</p>";
    }

    tasks.forEach(function (task) {

        const div = document.createElement("div");

        div.innerHTML = `

            <h4>${task.task_name}</h4>

            <p>Subject: ${task.subject || "Not specified"}</p>

            <p>Date: ${task.task_date}</p>

            <p>Status: ${task.is_completed ? "Completed" : "Pending"}</p>

           <button
        onclick="completeTask(${task.task_id})"
         ${task.is_completed ? "disabled" : ""}
        >
         ${task.is_completed ? "Completed ✓" : "Complete"}
        </button>
            <button onclick="deleteTask(${task.task_id})">
                Delete
            </button>

        `;

        taskList.appendChild(div);

    });

    updateProgress(tasks);
}


// Complete Task

async function completeTask(taskId) {

    try {

        const response = await fetch(

            `${API_URL}/complete-task/${taskId}`,

            {

                method: "PUT",
                 credentials: "include"


            }

        );


        if (!response.ok) {

            throw new Error("Could not complete task.");

        }


        loadTasks();


    } catch (error) {

        alert("Error updating task.");

        console.error(error);

    }

}
// Delete Task

async function deleteTask(taskId) {

    const confirmDelete = confirm("Are you sure you want to delete this task?");

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/delete-task/${taskId}`,
            {
                method: "DELETE",
                credentials: "include"
            }
        );

        if (!response.ok) {
            throw new Error("Task deletion failed");
        }

       

        loadTasks();

    } catch (error) {

        console.error("Error:", error);
        alert("Unable to delete task.");

    }
}


// ==========================================
// 5. PROGRESS TRACKING
// ==========================================

function updateProgress(tasks) {


    const total = tasks.length;


    const completed = tasks.filter(

        task => task.is_completed

    ).length;


    const pending = total - completed;


    const percentage = total === 0

        ? 0

        : Math.round((completed / total) * 100);


    document.getElementById("totalTasks").textContent = total;


    document.getElementById("completedTasks").textContent = completed;


    document.getElementById("pendingTasks").textContent = pending;


    document.getElementById("progressFill").style.width =

        percentage + "%";


    document.getElementById("progressPercentage").textContent =

        percentage + "% Completed";

}



// Load Tasks When Page Opens

loadTasks();



// ==========================================
// 6. MY GOALS
// ==========================================

const goalForm = document.getElementById("goalForm");

const goalList = document.getElementById("goalList");



// Add New Goal

goalForm.addEventListener("submit", async function (event) {

    event.preventDefault();


    const goal = {

        name: document.getElementById("goalName").value,

        type: document.getElementById("goalType").value,

        date: document.getElementById("goalDate").value

    };


    try {

        const response = await fetch(`${API_URL}/add-goal`, {
                
                credentials: "include",

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(goal)

        });


        if (!response.ok) {

            throw new Error("Goal could not be saved.");

        }


       

        goalForm.reset();


        loadGoals();


    } catch (error) {

        alert("Error saving goal. Please check the server.");

        console.error(error);

    }

});



// Load Goals

async function loadGoals() {

    try {
         const response = await fetch(`${API_URL}/get-goals`, {
                credentials: "include"
            });
        
        if (!response.ok) {

            throw new Error("Could not load goals.");

        }


        const goals = await response.json();


        displayGoals(goals);


    } catch (error) {

        console.error("Error loading goals:", error);

    }

}



// Display Goals

function displayGoals(goals) {

    goalList.innerHTML = "";


    if (goals.length === 0) {

        goalList.innerHTML =

            "<p class='no-goals'>No goals added yet.</p>";

        return;

    }


    goals.forEach(function (goal) {

        const div = document.createElement("div");

        div.className = "goal-card";


        div.innerHTML = `

            <div class="goal-card-header">

                <h3>${goal.goal_name}</h3>

                <span class="goal-status">${goal.status}</span>

            </div>


            <div class="goal-card-details">

                <p>

                    <strong>Category:</strong>

                    ${goal.goal_type}

                </p>


                <p>

                    <strong>Target Date:</strong>

                    ${goal.target_date}

                </p>


            <button
             onclick="completeGoal(${goal.goal_id})"
             ${goal.status === "Completed" ? "disabled" : ""}
            >
            ${goal.status === "Completed" ? "Completed ✓" : "Mark as Completed"}
            </button>

                <button

                    class="delete-goal-btn"

                    onclick="deleteGoal(${goal.goal_id})">

                    Delete Goal

                </button>

            </div>

        `;


        goalList.appendChild(div);

    });

}



// Complete Goal

async function completeGoal(goalId) {

    try {

        const response = await fetch(

            `${API_URL}/complete-goal/${goalId}`,

            {

                method: "PUT",
                credentials: "include"


            }
        

        );


        const result = await response.json();


        if (!response.ok) {

            throw new Error(result.message || "Could not complete goal.");

        }


       


        loadGoals();


    } catch (error) {

        console.error("Complete Goal Error:", error);

        alert(error.message);

    }

}



// Delete Goal

async function deleteGoal(goalId) {


    const confirmDelete = confirm(

        "Are you sure you want to delete this goal?"

    );


    if (!confirmDelete) {

        return;

    }


    try {

        const response = await fetch(

            `${API_URL}/delete-goal/${goalId}`,

            {

                method: "DELETE",
                credentials: "include"

            }

        );


        const result = await response.json();


        if (!response.ok) {

            throw new Error(result.message || "Could not delete goal.");

        }


        


        loadGoals();


    } catch (error) {

        console.error("Delete Goal Error:", error);

        alert(error.message);

    }

}
// ==========================================
// 7. SIGNUP AND LOGIN
// ==========================================

// Switch to Signup Form
function showSignup() {
    document.getElementById("loginFormContainer").hidden = true;
    document.getElementById("signupFormContainer").hidden = false;
    document.getElementById("authMessage").textContent = "";
}


// Switch to Login Form
function showLogin() {
    document.getElementById("signupFormContainer").hidden = true;
    document.getElementById("loginFormContainer").hidden = false;
    document.getElementById("authMessage").textContent = "";
}


// Signup Functionality
const signupForm = document.getElementById("signupForm");

signupForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const data = {
        name: document.getElementById("signupName").value,
        email: document.getElementById("signupEmail").value,
        password: document.getElementById("signupPassword").value
    };

    try {

        const response = await fetch(`${API_URL}/signup`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message);
        }

        alert("Signup successful! Please login.");

        signupForm.reset();
        showLogin();

    } catch(error) {

        document.getElementById("authMessage").textContent = error.message;

    }

});


// Login Functionality
const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const data = {
        email: document.getElementById("loginEmail").value,
        password: document.getElementById("loginPassword").value
    };

    try {

        const response = await fetch(`${API_URL}/login`, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message);
        }

        document.getElementById("auth-section").hidden = true;
        document.getElementById("dashboard").hidden = false;

        loginForm.reset();

        alert("Welcome " + result.name + "!");

        loadTasks();
        loadGoals();

    } catch(error) {

        document.getElementById("authMessage").textContent = error.message;

    }

});

// ==========================================
// 8. LOGOUT FUNCTIONALITY
// ==========================================

const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click", async function() {

    try {

        const response = await fetch(`${API_URL}/logout`, {
            method: "POST",
            credentials: "include"
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message);
        }

        document.getElementById("dashboard").hidden = true;
        document.getElementById("auth-section").hidden = false;

        showLogin();

        alert("Logout successful!");

    } catch(error) {

        alert(error.message);

    }

});

// Check Existing Login Session on Page Refresh

async function checkSession() {

    try {
        const response = await fetch(`${API_URL}/check-session`, {
            credentials: "include"
        });

        if (response.ok) {
            const data = await response.json();

            document.getElementById("auth-section").hidden = true;
            document.getElementById("dashboard").hidden = false;

            loadTasks();
            loadGoals();

        } else {
            document.getElementById("auth-section").hidden = false;
            document.getElementById("dashboard").hidden = true;
        }

    } catch (error) {
        console.error("Session Check Error:", error);
    }
}

checkSession();

// ==========================================
// EXPLORE OPPORTUNITIES
// ==========================================

document.getElementById("opportunityForm").addEventListener("submit", function(event) {

    event.preventDefault();

    const skill = document.getElementById("preferredSkill").value;
    const category = document.getElementById("opportunityType").value;

    const results = document.getElementById("opportunityResults");

    let opportunities = [];

    // Only Python Opportunities

    if (skill === "Python" && category === "Courses") {

        opportunities = [
            {
                name: "Python for Data Science",
                platform: "NPTEL",
                link: "https://nptel.ac.in/courses"
            },
            {
                name: "The Joy of Computing using Python",
                platform: "NPTEL",
                link: "https://nptel.ac.in/courses"
            },
            {
                name: "Python Courses",
                platform: "SWAYAM",
                link: "https://swayam.gov.in/search_courses"
            }
        ];

    }

    else if (skill === "Python" && category === "Internships") {

        opportunities = [
            {
                name: "Python / Django Internships",
                platform: "Internshala",
                link: "https://internshala.com/internships/"
            }
        ];

    }

    else if (skill === "Python" && category === "Certifications") {

        opportunities = [
            {
                name: "PCEP - Certified Entry-Level Python Programmer",
                platform: "Python Institute",
                link: "https://www.pythoninstitute.org/pcep"
            }
        ];

    }

    if (opportunities.length === 0) {

    results.innerHTML = `
        <div class="coming-soon">
            <h3>Coming Soon!</h3>
            <p>More opportunities will be added in future updates.</p>
        </div>
    `;

    return;
}
    // Display Results

    results.innerHTML = `
        <h3>${skill} - ${category}</h3>

        <table>
            <tr>
                <th>Opportunity</th>
                <th>Platform</th>
                <th>Official Link</th>
            </tr>

            ${opportunities.map(item => `
                <tr>
                    <td>${item.name}</td>
                    <td>${item.platform}</td>
                    <td>
                        <a href="${item.link}" target="_blank">
                            Visit
                        </a>
                    </td>
                </tr>
            `).join("")}

        </table>
    `;

});

// Load Goals When Page Opens
// ==========================================
// END OF PATHWISE SCRIPT
// ==========================================