from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def get_oss_response(prompt):

    response = pipe(
        prompt,
        max_new_tokens=100,
        do_sample=True
    )

    return response[0]["generated_text"]