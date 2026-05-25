# from transformers import pipeline

# pipe = pipeline(
#     "text-generation",
#     model="Qwen/Qwen2.5-0.5B-Instruct"
# )

# def get_oss_response(prompt):

#     response = pipe(
#         prompt,
#         max_new_tokens=50,
#         do_sample=True,
#         temperature=0.7
#     )

#     generated_text = response[0]["generated_text"]

#     final_response = generated_text[len(prompt):]

#     return final_response.strip()

from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def get_oss_response(prompt):

    formatted_prompt = f"""
You are a helpful AI assistant.

Give short, clear, and direct answers.

User: {prompt}

Assistant:
"""

    response = pipe(
        formatted_prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.3
    )

    generated_text = response[0]["generated_text"]

    final_response = generated_text.split("Assistant:")[-1]

    return final_response.strip()