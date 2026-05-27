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
- Respond naturally and briefly.
- Do not repeat things in the same answer.

User:
{prompt}

Assistant:
"""

    response = pipe(
        formatted_prompt,
        max_new_tokens=40,
        do_sample=True,
        temperature=0.3
    )

    generated_text = response[0]["generated_text"]

    final_response = generated_text.split("Assistant:")[-1].strip()

    # Remove incomplete ending sentence
    if final_response and final_response[-1] not in [".", "!", "?"]:

        last_dot = max(
            final_response.rfind("."),
            final_response.rfind("!"),
            final_response.rfind("?")
        )

        if last_dot != -1:
            final_response = final_response[:last_dot + 1]

    return final_response.strip()