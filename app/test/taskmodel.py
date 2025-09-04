import sys
import os
import importlib
import sqlalchemy as sa

# Step 1: Add the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

try:
    # Step 2: Dynamically import the task module
    m = importlib.import_module("app.models.task")
    print("✅ Imported 'app.models.task' successfully.")

    # Step 3: Check for expected attributes
    base = getattr(m, "Base", None)
    task_cls = getattr(m, "Task", None)

    print("Base:", base if base else "❌ 'Base' not found.")
    print("Task class:", task_cls if task_cls else "❌ 'Task' class not found.")

    # Step 4: Confirm SQLAlchemy is functioning
    print("SQLAlchemy Column is callable:", callable(sa.Column))

except Exception as e:
    print("❌ Import failed:", e)
    raise
