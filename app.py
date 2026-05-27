from transformers import pipeline

# 1. Initialize the text generator (downloads GPT-2 by default)
print("Loading the text generation model... Please wait.")
generator = pipeline("text-generation", model="gpt2")
print("Model loaded successfully!\n")

# 2. Ask the user for input via the terminal
user_input = input("Enter the beginning of your sentence: ")

# 3. Generate text based on what YOU typed
print("\nThinking... Generating response...")
output = generator(
    user_input,
    max_length=50,
    num_return_sequences=1
)

# 4. Print the clean result
print("\n--- AI Generated Result ---")
print(output[0]['generated_text'])
print("---------------------------")