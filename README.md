# Sinthia AI

**Sinthia AI** is a lightweight AI assistant designed to help users prepare for English proficiency tests like **IELTS** and **TOEFL**, with a strong focus on **Speaking Test evaluation**.

---

## 🎯 Key Features

- Supports **Reading**, **Writing**, and **Speaking** test simulations
- **Speaking Test** includes deep analysis powered by LLMs
- Provides actionable feedback and **band score estimates** (IELTS format)

---

## 🧠 How It Works

Note: We would implement the reading and writing tests later

### 🔊 Speaking Test Flow:

1. **Prompt the user** with a question (spoken)
2. **Listen** to the user's response via microphone
3. **Transcribe** audio to text (using **Parakeet v2**)
4. **Analyze** response:
    - **Computational Metrics**:
        - Words spoken per minute
        - Awkward pauses, filler words
    - **Contextual (LLM-based)**:
        - Fluency & coherence
        - Lexical range
        - Grammar accuracy
        - Pronunciation analysis (experimental)
5. **Estimate IELTS Band Score (0–9)**
6. (Advanced) **Generate deep report**

Note: I also have a plan to have a conversational mode for the agent where you can directly talk with sinthia casually which will help you improve your listening skills as there would be options to choose from various voices and accents for sinthia

---

## 🛠️ Tech Stack

- 🎤 **Input**: Microphone via `sounddevice`
- ✍️ **Transcription**: `Parakeet v2` (word-level timestamps)
- 🧮 **Computation**: Custom metrics (WSPM, pauses)
- 🤖 **LLMs** (not decided yet, but planned):
    - Qwen 3 / 3.1
    - LLaMA 3.2 (1B & 3B)
    - Gemma 3 (1B-it, 4B-it)
    - Phi-4 Mini (for deep reasoning)
    - Framework: **LangGraph**
- 🗣️ **TTS**: Kyutai TTS
- 📄 **Output**: Text + optional PDF report with visualizations
- **API**: FastAPI to expose a REST API to build a frontend

---

## 🗺️ Roadmap

- [ ]  Microphone input
- [ ]  Word-level transcription
- [ ]  Compute metrics (WSPM, pauses)
- [ ]  Basic LLM setup for the analysis (System prompt, and prompt injection)
- [ ]  Advanced agentic LLM for deep analysis
- [ ]  Next steps….

---

## 📌 Notes

- **Pronunciation analysis** is experimental and challenging—will require signal-level processing or advanced models. which will require Phoneme-Level Analysis
- Focused on **small, efficient LLMs** for cost-effective local or edge deployment.
