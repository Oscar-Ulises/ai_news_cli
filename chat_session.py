import openai

openai.api_key = "your_api_key"

def openai_function(prompt):
    try:
        response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}] )
        
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error from AI: {e}"
