from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# ML Model Import
from ml_model.recommend import generate_learning_path

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
CORS(app, supports_credentials=True)


# MySQL Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )



# Home API
@app.route("/")
def home():
    return "PathWise Backend and MySQL Connected Successfully!"


# =====================================
# LEARNING PATH RECOMMENDATION API
# =====================================

@app.route("/recommend-learning-path", methods=["POST"])
def recommend_learning_path():

    if "student_id" not in session:
        return jsonify({"error": "Please login first."}), 401

    data = request.get_json(silent=True) or {}

    conn = None
    cursor = None

    try:
        student_id = session["student_id"]

        goal = data["goal"]
        sub_goal = data["sub_goal"]
        available_days = int(data["available_days"])
        daily_hours = int(data["daily_hours"])

        if available_days <= 0 or daily_hours <= 0:
            return jsonify({
                "error": "Days and daily hours must be greater than zero."
            }), 400

        # Generate Learning Path (ML unchanged)
        path = generate_learning_path(
            goal,
            sub_goal,
            available_days,
            daily_hours
        )

        if isinstance(path, str):
            return jsonify({"error": path}), 404

        if path.empty:
            return jsonify({
                "error": "No learning path found."
            }), 404

        # Calculate Study Time
        total_days = int(path["estimated_days"].sum())
        total_hours = total_days * 2

        required_days = total_hours / daily_hours

        if required_days <= available_days:
            status = "Achievable"
        else:
            status = "More study time required"

        # Convert Learning Path into JSON
        learning_path = path.to_dict(orient="records")

        # Save Learning Path in MySQL
        conn = get_db_connection()
        cursor = conn.cursor()

        # Replace previous generated path for this student
        cursor.execute(
            "DELETE FROM learning_paths WHERE student_id = %s",
            (student_id,)
        )

        insert_query = """
            INSERT INTO learning_paths
            (student_id, goal_id, subject, recommended_topic,
             priority, estimated_hours, status)
            VALUES (%s, NULL, %s, %s, %s, %s, %s)
        """

        values = []

        for topic in learning_path:
            estimated_hours = float(topic["estimated_days"]) * 2

            values.append((
                student_id,
                goal,
                topic["topic"],
                topic["priority"],
                estimated_hours,
                "Pending"
            ))

        cursor.executemany(insert_query, values)

        conn.commit()

        return jsonify({
            "message": "Learning Path saved successfully!",
            "goal": goal,
            "sub_goal": sub_goal,
            "total_topics": len(path),
            "total_hours": total_hours,
            "available_days": available_days,
            "daily_hours": daily_hours,
            "required_days": round(required_days, 1),
            "status": status,
            "learning_path": learning_path
        })

    except KeyError as e:
        if conn:
            conn.rollback()

        return jsonify({
            "error": f"Missing field: {e}"
        }), 400

    except ValueError:
        if conn:
            conn.rollback()

        return jsonify({
            "error": "Please enter valid numeric values for days and hours."
        }), 400

    except Exception as e:
        if conn:
            conn.rollback()

        print("LEARNING PATH ERROR:", e)

        return jsonify({
            "error": "Unable to generate and save Learning Path."
        }), 500

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

          
# =====================================
# DELETE LEARNING PATH API
# =====================================

@app.route("/delete-learning-path", methods=["DELETE"])
def delete_learning_path():

    if "student_id" not in session:
        return jsonify({"error": "Please login first."}), 401

    conn = None
    cursor = None

    try:
        student_id = session["student_id"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM learning_paths WHERE student_id = %s",
            (student_id,)
        )

        conn.commit()

        return jsonify({
            "message": "Learning Path deleted successfully!"
        }), 200

    except Exception as e:
        if conn:
            conn.rollback()

        print("DELETE LEARNING PATH ERROR:", e)

        return jsonify({
            "error": "Unable to delete Learning Path."
        }), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()    
# =====================================
# DAILY PLANNER APIs
# ============================ 

@app.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    if len(password) < 8:
        return jsonify({"message": "Password must be at least 8 characters"}), 400

    hashed_password = generate_password_hash(password)

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO students (full_name, email, password_hash)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, email, hashed_password))
        conn.commit()

        return jsonify({"message": "Signup successful!"}), 201

    except mysql.connector.IntegrityError:
        return jsonify({"message": "Email already registered"}), 409

    except Exception as e:
        print("SIGNUP ERROR:", e)
        return jsonify({"message": "Signup failed"}), 500

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

# =====================================
# LOGIN API
# =====================================

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True) or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT student_id, full_name, email, password_hash
            FROM students
            WHERE email = %s
        """

        cursor.execute(query, (email,))
        student = cursor.fetchone()

        if student and check_password_hash(
            student["password_hash"], password
        ):

            session["student_id"] = student["student_id"]
            session["student_name"] = student["full_name"]

            return jsonify({
                "message": "Login successful!",
                "student_id": student["student_id"],
                "name": student["full_name"]
            }), 200

        return jsonify({
            "message": "Invalid email or password"
        }), 401

    except Exception as e:
        print("LOGIN ERROR:", e)
        return jsonify({"message": "Login failed"}), 500

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()       

 # Logout API
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()

    return jsonify({
        "message": "Logout successful!"
    }), 200

# Check Login Session API

@app.route("/check-session", methods=["GET"])
def check_session():

    if "student_id" in session:
        return jsonify({
            "logged_in": True,
            "name": session["student_name"]
        }), 200

    return jsonify({
        "logged_in": False
    }), 401                
# Add Task API

@app.route("/add-task", methods=["POST"])
def add_task():

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    data = request.json

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    INSERT INTO daily_tasks
    (student_id, task_name, subject, task_date)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        student_id,
        data["name"],
        data["subject"],
        data["date"]
    )

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "message": "Task saved successfully!"
    }), 201

# Get Tasks API

@app.route("/get-tasks", methods=["GET"])
def get_tasks():

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM daily_tasks WHERE student_id = %s",
        (student_id,)
    )

    tasks = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(tasks), 200




# Complete Task API

@app.route("/complete-task/<int:task_id>", methods=["PUT"])
def complete_task(task_id):

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    UPDATE daily_tasks
    SET is_completed = TRUE
    WHERE task_id = %s AND student_id = %s
    """

    cursor.execute(query, (task_id, student_id))
    db.commit()

    if cursor.rowcount == 0:
        cursor.close()
        db.close()
        return jsonify({
            "message": "Task not found!"
        }), 404

    cursor.close()
    db.close()

    return jsonify({
        "message": "Task completed successfully!"
    }), 200

# Delete Task API
@app.route("/delete-task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    DELETE FROM daily_tasks
    WHERE task_id = %s AND student_id = %s
    """

    cursor.execute(query, (task_id, student_id))
    db.commit()

    if cursor.rowcount == 0:
        cursor.close()
        db.close()
        return jsonify({
            "message": "Task not found!"
        }), 404

    cursor.close()
    db.close()

    return jsonify({
        "message": "Task deleted successfully!"
    }), 200


# =====================================
# MY GOALS APIs
# =====================================

# Add Goal API

@app.route("/add-goal", methods=["POST"])
def add_goal():

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    data = request.json

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    INSERT INTO learning_goals
    (student_id, goal_name, goal_type, target_date)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        student_id,
        data["name"],
        data["type"],
        data["date"]
    )

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "message": "Goal saved successfully!"
    }), 201

# Get Goals API
@app.route("/get-goals", methods=["GET"])
def get_goals():

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM learning_goals WHERE student_id = %s",
        (student_id,)
    )

    goals = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(goals), 200


# Complete Goal API
@app.route("/complete-goal/<int:goal_id>", methods=["PUT"])
def complete_goal(goal_id):

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    UPDATE learning_goals
    SET status = 'Completed'
    WHERE goal_id = %s AND student_id = %s
    """

    cursor.execute(query, (goal_id, student_id))
    db.commit()

    if cursor.rowcount == 0:
        cursor.close()
        db.close()
        return jsonify({
            "message": "Goal not found!"
        }), 404

    cursor.close()
    db.close()

    return jsonify({
        "message": "Goal completed successfully!"
    }), 200


# Delete Goal API
@app.route("/delete-goal/<int:goal_id>", methods=["DELETE"])
def delete_goal(goal_id):

    student_id = session.get("student_id")

    if not student_id:
        return jsonify({
            "message": "Please login first!"
        }), 401

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    DELETE FROM learning_goals
    WHERE goal_id = %s AND student_id = %s
    """

    cursor.execute(query, (goal_id, student_id))
    db.commit()

    if cursor.rowcount == 0:
        cursor.close()
        db.close()
        return jsonify({
            "message": "Goal not found!"
        }), 404

    cursor.close()
    db.close()

    return jsonify({
        "message": "Goal deleted successfully!"
    }), 200

# =====================================
# RUN FLASK APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True)