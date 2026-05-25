from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def get_oss_response(prompt):

    formatted_prompt = f"""
You are a helpful AI assistant.

Rules:
- Give short and accurate answers.
- Do not add unnecessary details.
- If answer is simple, answer in one sentence.
- Do not continue conversation unnecessarily.
- If you are unsure, say you are unsure.

User: {prompt}

Assistant:
"""

    response = pipe(
        formatted_prompt,
        max_new_tokens=40,
        do_sample=True,
        temperature=0.3
    )

    generated_text = response[0]["generated_text"]

    final_response = generated_text.split("Assistant:")[-1]

    return final_response.strip()