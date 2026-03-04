import ollama
import time

def test_gpu_load():
    print("Sending request to Llama 3.2 Vision...")
    start_time = time.time()

    response = ollama.generate(
        model='llama3.2-vision',
        prompt='System check: Are you running on GPU? Describe your current state.'
    )

    duration = time.time() - start_time

    print(f"AI Response: {response['response']}")
    print(f"Duration to get the response: {round(duration,2)} seconds")

if __name__=="__main__":
    test_gpu_load()