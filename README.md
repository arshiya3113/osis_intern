# OSIS Internship Tasks

This repository contains the projects I completed during my internship at **OSIS**.
Each task focuses on Python programming, GUI development, or speech recognition.

---

## 📌 Tasks

### 1. BMI Calculator (Tkinter)

A simple **GUI-based BMI Calculator** that allows users to input their height and weight, then calculates the BMI and displays the health category.

**Features:**

* User-friendly interface using Tkinter
* Displays BMI value with category (Underweight, Normal, Overweight, Obesity)
* Input validation with error handling

---

### 2. Password Generator (Tkinter)

A **secure password generator** with multiple strength options.

**Features:**

* Options for Weak, Medium, and Strong passwords
* Customizable password length (3–64 characters)
* Clipboard copy support (via **pyperclip** or Tkinter fallback)
* User-friendly GUI with radio buttons and spinbox

---

### 3. Voice Assistant (Speech Recognition + pyttsx3)

A basic **voice-controlled assistant** that listens to commands and responds.

**Features:**

* Speech-to-text using Google Speech Recognition
* Text-to-speech responses with **pyttsx3**
* Supports simple commands like:

  * Greeting (`hello`)
  * Introduction (`what is your name`)
  * Open Google and tell current time
  * Exit program
* Handles background noise and errors gracefully

---

## 🚀 Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/osis-internship-tasks.git
   cd osis-internship-tasks
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run each task:

   * **BMI Calculator**

     ```bash
     python bmi_calculator.py
     ```
   * **Password Generator**

     ```bash
     python password_generator.py
     ```
   * **Voice Assistant**

     ```bash
     python voice_assistant.py
     ```

---

## 📂 Project Structure

```
osis-internship-tasks/
│── bmi_calculator.py
│── password_generator.py
│── voice_assistant.py
│── requirements.txt
│── README.md
```

---

## 🛠️ Requirements

* Python 3.8+
* tkinter
* speechrecognition
* pyttsx3
* pyperclip (optional)

Install them using:

```bash
pip install speechrecognition pyttsx3 pyperclip
```

---

## 📌 Notes

* These projects are developed as part of my **internship learning tasks** at OSIS.
* Contributions and suggestions for improvements are welcome!

---

## 📄 License

This repository is licensed under the **MIT License**.
You are free to use, modify, and distribute these projects with attribution.
