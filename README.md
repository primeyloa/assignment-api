# Assignment API

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/) for managing assignments. It allows you to create, retrieve, and delete assignments stored in memory.

Each assignment has:
- `id` — auto-generated integer ID
- `title` — string (2–50 characters)
- `due_date` — date in `YYYY-MM-DD` format
- `done` — boolean (defaults to `false`)

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/assignments` | List all assignments |
| `GET` | `/assignments/{id}` | Get a single assignment by ID |
| `POST` | `/create` | Create a new assignment |
| `DELETE` | `/assignments/{id}` | Delete an assignment by ID |

> **Note:** The spec example uses `POST /assignments`, but this project implements creation at `POST /create`.

## Requirements

- Python 3.10+ (tested with Python 3.14)
- pip

## How to Install

1. Clone the repository:

```bash
git clone <repo-url>
cd assignment-api
```

2. (Recommended) Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
fastapi[standard]
pydantic
typing
```

## How to Run

Start the FastAPI development server with Uvicorn (included via `fastapi[standard]`):

```bash
fastapi dev main.py
```

Or directly with Uvicorn:

```bash
uvicorn main:app --reload
```

The server will start at:

- API: http://127.0.0.1:8000
- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- Alternative docs (ReDoc): http://127.0.0.1:8000/redoc

## Example Request

Create a new assignment:

```bash
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '{
    "id": 0,
    "title": "Complete FastAPI exercise",
    "due_date": "2026-08-30",
    "done": false
  }'
```

If following the spec's `POST /assignments` convention, the request body is the same:

```http
POST /assignments HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "title": "Complete FastAPI exercise",
  "due_date": "2026-08-30",
  "done": false
}
```

**Example response** (`201 Created`):

```json
{
  "item": {
    "id": 0,
    "title": "Complete FastAPI exercise",
    "due_date": "2026-08-30",
    "done": false
  },
  "status": "successful!"
}
```

### Other examples

List all assignments:

```bash
curl http://127.0.0.1:8000/assignments
```

Get one assignment:

```bash
curl http://127.0.0.1:8000/assignments/0
```

Delete an assignment:

```bash
curl -X DELETE http://127.0.0.1:8000/assignments/0
```
