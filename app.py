from transformers import pipeline

# Initialize the text generation pipeline
print("Loading the AI model... (This may take a moment on the first run)")
generator = pipeline("text-generation", model="gpt2")
print("Model loaded successfully!\n")

# Take dynamic input from the user
user_prompt = input("Type the beginning of your sentence and press Enter: ")

# Generate the text based on your prompt
print("\nGenerating text...")
output = generator(
    user_prompt,
    max_length=50,
    num_return_sequences=1
)

# Print out the generated text clearly
print("\n--- AI Generated Completion ---")
print(output[0]['generated_text'])
print("--------------------------------")