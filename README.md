# **PopQuiz Pro**

PopQuiz Pro is an engaging quiz app that tests your knowledge of pop culture, films, and series. Dive into questions about iconic movies, trending TV shows, and unforgettable pop culture moments in a fun, interactive format. Perfect for fans who love to challenge their trivia skills! 🎥📺🎶

---

### **Features**
1. **Pop Culture Focus**: Questions tailored to the world of entertainment, including movies, series, and music.
2. **Dynamic Question Bank**: Easily customizable to include your favorite topics.
3. **Interactive UI**: User-friendly design to make quizzing fun and effortless.
4. **Real-Time Scoring**: Keep track of your progress with instant feedback.
5. **Modular Design**: Streamlined structure for easy maintenance and updates.

---

### **How It Works**
1. **Setup Your Quiz**: The app loads questions from the `question_data` module, with topics covering blockbuster films, hit TV series, and trending pop culture moments.
2. **Test Your Knowledge**: Answer true/false questions via an interactive GUI.
3. **Score and Feedback**: See your score grow as you answer correctly and get immediate feedback on your answers.

---

### **Requirements**
- **Python Libraries**: 
  - `tkinter` for GUI functionality.
- **Project Files**:
  - `question_model.py`: Manages individual quiz questions.
  - `data.py`: Houses pop culture trivia questions.
  - `quiz_brain.py`: Handles quiz logic and scoring.
  - `ui.py`: Brings the app to life with an intuitive GUI.

---

### **Setup Instructions**
1. Clone the repository and navigate to the project directory.
2. Ensure all required files (`question_model.py`, `data.py`, `quiz_brain.py`, `ui.py`) are present.
3. Run the main script:
   ```bash
   python main.py
   ```
4. Answer pop culture questions via the GUI and track your score.

---

### **Customization**
- **Add Your Favorites**: Update `data.py` with new pop culture questions, like:
  ```python
  {"question": "Is 'Friends' the longest-running sitcom?", "correct_answer": "False"}
  ```
- **Themes**: Modify questions to focus on specific genres like sci-fi, fantasy, or rom-coms.

---

### **Limitations**
- Supports only true/false questions for now.
- Requires `tkinter`, pre-installed with most Python distributions.

---

### **Who Is It For?**
- Movie buffs and binge-watchers.
- Trivia enthusiasts and quiz night organizers.
- Fans of all things pop culture!

---

### **Future Upgrades**
- Include multiple-choice questions for deeper challenges.
- Add a "name that quote" or "guess the song" feature.
- Support for multiplayer quizzes with leaderboards.

---

Ready to prove you're the ultimate pop culture expert? 🎬✨ Play **PopQuiz Pro** now!
