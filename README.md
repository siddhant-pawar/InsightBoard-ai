
<p align="center"><h1 align="center">INSIGHTBOARD-AI</h1></p>

<br>

---

## Overview

**InsightBoard-AI** is an AI-powered analytics and task management platform designed to provide actionable insights, automate task tracking, and generate intelligent summaries. It integrates AI services for text analysis and task optimization, making it easier for teams and individuals to manage workflows efficiently.

---

## Features

- **AI Task Management**: Automate task creation, assignment, and prioritization using AI algorithms.
- **Transcript Analysis**: Extract key information and actionable insights from meetings, calls, or documents.
- **Database Migrations**: Maintain your database schema with Alembic support.
- **Dockerized Deployment**: Easily deploy using Docker containers.
- **REST APIs**: Access and manage tasks, transcripts, and insights programmatically.
- **Testing Suite**: Verify your project functionality with included tests.

---

## Project Structure

```sh
└── InsightBoard-ai/
    ├── Dockerfile
    ├── Procfile
    ├── __pycache__/
    ├── alembic/
    ├── alembic.ini
    ├── apis_docs.txt
    ├── app/
    ├── main.py
    ├── migrate.py
    ├── pyproject.toml
    └── req.txt
````

### Project Index

Refer to the [GitHub repository](https://github.com/siddhant-pawar/InsightBoard-ai) for full file documentation.

* `main.py`: Entry point for the application.
* `migrate.py`: Script to run database migrations.
* `alembic.ini` & `alembic/`: Manage database migrations and schema changes.
* `req.txt` & `pyproject.toml`: Python dependencies and project configuration.
* `Dockerfile` & `Procfile`: Deployment configuration.
* `app/`: Core application code including APIs, models, services, utilities, and tests.
* `apis_docs.txt`: API reference documentation.

###  Project Index
<details open>
	<summary><b><code>INSIGHTBOARD-AI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/migrate.py'>migrate.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic.ini'>alembic.ini</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/req.txt'>req.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/Procfile'>Procfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/apis_docs.txt'>apis_docs.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- alembic Submodule -->
		<summary><b>alembic</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic/script.py.mako'>script.py.mako</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic/env.py'>env.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>versions</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic/versions/7f0d14d07938_update_model.py'>7f0d14d07938_update_model.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic/versions/44d41aba24a1_import_model.py'>44d41aba24a1_import_model.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/alembic/versions/27217aa64bbf_import_model.py'>27217aa64bbf_import_model.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<details>
				<summary><b>schemas</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/schemas/task.py'>task.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/schemas/task_filter.py'>task_filter.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/schemas/transcript.py'>transcript.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>core</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/core/db.py'>db.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>test</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/test/tralateapi.py'>tralateapi.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/test/taskmodel.py'>taskmodel.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/test/checkdbconnect.py'>checkdbconnect.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>models</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/models/task.py'>task.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/utils/text.py'>text.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/utils/exact_details.py'>exact_details.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/services/ai_service.py'>ai_service.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/services/task_service.py'>task_service.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>api</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/api/tasks.py'>tasks.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/siddhant-pawar/InsightBoard-ai/blob/master/app/api/transcripts.py'>transcripts.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>


---

## Getting Started

### Prerequisites

Before getting started, ensure your environment includes:

* **Python 3.10+**
* **Docker** (optional for containerized deployment)
* **Git**

### Installation

**Build from source:**

```sh
git clone https://github.com/siddhant-pawar/InsightBoard-ai
cd InsightBoard-ai
pip install -r req.txt
```

**Using Docker:**

```sh
docker build -t insightboard-ai .
docker run -it insightboard-ai
```

---

### Usage

Start the application:

```sh
python main.py
```

Or with Docker:

```sh
docker run -it insightboard-ai
```

---

### Testing

Run tests using:

```sh
pytest app/test/
```

---

## Project Roadmap

* [x] **Task 1**: Implement AI-based task management.
* [ ] **Task 2**: Enhance transcript analysis features.
* [ ] **Task 3**: Build advanced analytics dashboard.

---

## Contributing

* **💬 [Join Discussions](https://github.com/siddhant-pawar/InsightBoard-ai/discussions)**
* **🐛 [Report Issues](https://github.com/siddhant-pawar/InsightBoard-ai/issues)**
* **💡 [Submit Pull Requests](https://github.com/siddhant-pawar/InsightBoard-ai/blob/main/CONTRIBUTING.md)**

<details closed>
<summary>Contributing Guidelines</summary>

1. Fork the repository.
2. Clone locally:

   ```sh
   git clone https://github.com/siddhant-pawar/InsightBoard-ai
   ```
3. Create a new branch:

   ```sh
   git checkout -b feature-name
   ```
4. Make and test changes.
5. Commit changes:

   ```sh
   git commit -m "Description of feature"
   ```
6. Push and submit a Pull Request.

</details>

---

## Acknowledgments

* Inspired by AI-driven workflow optimization solutions.
* [Alembic](https://alembic.sqlalchemy.org/) for database migrations.
* Open-source contributors in Python AI and web frameworks.

