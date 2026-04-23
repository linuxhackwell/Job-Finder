# 🔍 Job Finder

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![API](https://img.shields.io/badge/API-Remotive-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A desktop application that searches and displays remote job listings from the Remotive API. Built with Python and Tkinter, this tool helps developers find remote opportunities quickly with a clean, responsive interface.

## 📸 Screenshot
<img width="1366" height="768" alt="Screenshot From 2026-04-23 18-42-03" src="https://github.com/user-attachments/assets/ddabbc70-4a5c-4cbb-9b59-74486a79b1df" />


## ✨ Features

- **Real-time search** with 500ms debounce delay (prevents API spam)
- **Case-insensitive filtering** by job title and company name
- **Responsive layout** that adapts to window resizing
- **Double-click** any job to open application link in browser
- **Clear button** to reset search instantly
- **Status bar** showing search results count and feedback
- **Scrollable results** for handling large job listings

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| Tkinter | GUI framework |
| Requests | API communication |
| Remotive API | Remote job data source |
| Webbrowser | Open job links |

## 📋 Prerequisites

- Python 3.8 or higher
- Internet connection (for API requests)

## 🚀 Installation

### 1. Clone the repository
git clone https://github.com/linuxhackwell/job-finder.git
cd job-finder

### 2. Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows

### 3. Install dependencies

pip install requests

### 4. Run the application

python job_finder.py

📦 Dependencies

Create a requirements.txt file:
text

requests>=2.28.0

🎮 Usage Guide

    Launch the application

    Type a search term (e.g., "python", "developer", "remote")

        Search automatically triggers after 0.5 seconds of inactivity

    View matching jobs in the results table

    Double-click any job to open the application link in your default browser

    Click Clear to reset the search and start over

Example Searches

    python - Find Python-related jobs

    react - Find React developer positions

    javascript - Find JavaScript opportunities

    senior - Find senior-level roles

📁 Project Structure
text

job-finder/
│
├── job_finder.py        # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules

🔄 How It Works

    User types a search term in the entry field

    Application waits 500ms after typing stops (debounce)

    Fetches all remote jobs from Remotive API

    Filters jobs where search term appears in title or company name

    Displays matching jobs in a scrollable table

    Double-clicking a job opens its URL in the browser

🐛 Known Issues

    API rate limits may apply with rapid searches (debounce minimizes this)

    No offline mode (requires internet connection)

    Large job lists load instantly but API response time varies

🔮 Future Improvements

    Add category/job type filters

    Save favorite jobs locally

    Export results to CSV

    Add loading progress indicator

    Pagination for large result sets

    Keyboard shortcuts for navigation

🤝 Contributing

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit changes (git commit -m 'Add some AmazingFeature')

    Push to branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📄 License

This project is licensed under the MIT License.
👨‍💻 Author

Anuu (linuxhackwell)

    GitHub: @linuxhackwell

🙏 Acknowledgments

    Remotive for providing the remote jobs API

    Python requests library developers

    Tkinter community

📞 Support

For issues or questions:

    Open an issue on GitHub

⭐ Star this repository if you find it useful!

Built with Python and ☕
text


## Instructions to Add This README:

1. **Create the file** in your project folder: `README.md`
2. **Add a screenshot** by running the app, taking a screenshot, saving as `screenshot.png`, and replacing the ASCII art with:
![Job Finder Screenshot](screenshot.png)

### 4.Commit and push:

git add README.md
git commit -m "Add professional README documentation"
git push origin main
