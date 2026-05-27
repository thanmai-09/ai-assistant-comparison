# AI Assistant Comparison

## Project Overview

AI Assistant Comparison is a Streamlit-based chatbot application developed to compare the behavior and performance of two different AI assistants:

- OSS Assistant (Open Source Local Model)
- Frontier Assistant (Gemini API-Based Assistant)

The project evaluates conversational memory, factual accuracy, reasoning ability, hallucinations, safety behavior, and API limitations.

The OSS assistant uses the Qwen2.5-0.5B-Instruct model running locally through HuggingFace Transformers, while the Frontier assistant uses the Google Gemini API.

---

## Features

- Interactive chatbot interface using Streamlit
- Assistant selection between OSS and Frontier assistants
- Conversational memory handling
- Factual question answering
- Reasoning capability testing
- Hallucination detection
- Safety behavior evaluation
- API quota error handling

---

## Technologies Used

- Python
- Streamlit
- HuggingFace Transformers
- Qwen2.5-0.5B-Instruct
- Google Gemini API
- Git & GitHub

---

## Project Architecture

User Input  
↓  
Streamlit User Interface  
↓  
Assistant Selection  
↓  
OSS Assistant / Frontier Assistant  
↓  
Memory Handling  
↓  
Response Generation  
↓  
Chat Display

---

## Project Structure

```text
ai-assistant-comparison/
│
├── app.py
├── requirements.txt
├── assistants/
│   ├── oss_assistant.py
│   ├── frontier_assistant.py
│   └── memory.py
│
├── screenshots/
│   ├── home_ui.png
│   ├── memory_test.png
│   ├── factual_qa.png
│   ├── reasoning_test.png
│   ├── hallucination_test.png
│   ├── safety_test.png
│   └── frontier_quota_error.png
│
└── README.md
```

---

## Screenshots

## Home UI

![Home UI](screenshots/home_ui.png)

---

## Memory Test

![Memory Test](screenshots/memory_test.png)

---

## Factual Question Answering

![Factual QA](screenshots/factual_qa.png)

---

## Reasoning Test

![Reasoning Test](screenshots/reasoning_test.png)

---

## Hallucination Test

![Hallucination Test](screenshots/hallucination_test.png)

---

## Safety Test

![Safety Test](screenshots/safety_test.png)

---

## Frontier Assistant Quota Error

![Frontier Assistant Quota Error](screenshots/frontier_quota_error.png)

---

## OSS Assistant Evaluation

| Evaluation Aspect | Observation |
|-------------------|-------------|
| Conversational Ability | Moderate |
| Memory Retention | Partial |
| Factual Accuracy | Moderate |
| Reasoning Ability | Imperfect |
| Safety Alignment | Weak |
| Response Speed | Fast |
| Hallucination Presence | Present |

---

## Key Findings

- The OSS assistant was able to remember recent user information in short conversations.
- The model occasionally generated factual hallucinations.
- Reasoning performance was inconsistent during logical comparison tasks.
- The OSS assistant showed weak safety filtering for harmful prompts.
- The Frontier assistant could not be fully tested because of API quota limitations.

---

## Limitations

- Small OSS model size (0.5B) caused factual inaccuracies and hallucinations.
- Conversational memory was limited.
- Frontier assistant depended on external API quota availability.
- Safety alignment in the OSS assistant was not strong enough.

---

## Future Improvements

- Use larger open-source language models
- Add persistent database memory
- Improve UI design and responsiveness
- Add streaming response generation
- Implement stronger safety filtering
- Add performance benchmarking metrics

---

## How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/thanmai-09/ai-assistant-comparison.git
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Application

```bash
streamlit run app.py
```

---

## Conclusion

This project demonstrates the practical differences between a local open-source AI assistant and a frontier API-based assistant. The evaluation highlights important aspects such as conversational memory, factual accuracy, reasoning capability, hallucinations, safety behavior, and API limitations in modern AI systems.