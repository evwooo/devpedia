# Devpedia

**Devpedia** is a developer-friendly platform that offers categorized guides, tips, and common command references for various tools, languages, and frameworks — starting with Git.
---

## Tech Stack

| Layer    | Tools                                  |
|----------|----------------------------------------|
| Frontend | React, React Router, Tailwind CSS      |
| Backend  | Flask, Flask-CORS                      |
| Data     | JSON (e.g., `git.json`)                |
| DevOps   | Git + GitHub (Repo: [evwooo/devpedia](https://github.com/evwooo/devpedia)) |

---

## Getting Started

### Backend Setup (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python run.py              # Runs at http://localhost:5000
```

### Frontend Setup (React + Tailwind)

```bash
cd frontend
npm install
npm start                  # Runs at http://localhost:3000
```

---

## Structure

```
git_guide/
├── backend/
│   ├── app/
│   │   ├── cheatsheets/      # JSON data
│   │   ├── routes.py         # API route
│   │   └── __init__.py       # App factory + blueprint registration
│   ├── run.py
│   └── requirements.txt
├── frontend/
│   └── (React project with pages/Home.jsx, pages/Git.jsx, etc.)
├── README.md
```

---

## Roadmap

- [ ] Implement Git cheatsheet
- [ ] Create modern, dynamic UI for pages
- [ ] Add cheat sheets for Docker, React, Flask, etc.
- [ ] Add user authentication
- [ ] Create database to store cheatsheet data
- [ ] Potentially use API to retrieve info on documentation

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License

This project is licensed under the [MIT License](LICENSE).
