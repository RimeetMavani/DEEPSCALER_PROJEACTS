import ollama 
import gradio as gr


# funcation to process user queries 

def solve_math_probleam(probleam):
    responce = ollama.chat( model="deepscaler", messages=[{'role':'user', 'content':probleam }])
    return responce['message']



# define gradio interface

interface = gr.Interface(
    fn = solve_math_probleam,
    inputs = gr.Textbox(label="enter a math probeam"),
    outputs = gr.Textbox(label ="solution"),
    title="AI power math solver ",
    description="Ask any math qustion , and Deepscaler provide a step-by-step solution",
)

 #luanch the application

interface.launch()
