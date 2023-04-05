import re
import os
import random
import requests

from flask import Flask, jsonify, request

app = Flask(__name__)

class HuggingFaceSuperAPI:
  def __init__(self, agbrain_endpoint, gpt2_large_endpoint, summary_endpoint, \
               bearer_token, num_return_sequences, temperature):
    self.endpoint = agbrain_endpoint
    self.gpt2_large_endpoint = gpt2_large_endpoint
    self.summary_endpoint = summary_endpoint
    self.num_return_sequences = num_return_sequences
    self.temperature = temperature
    self.headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

  def solve(self, prompt):
    reply = self.prompt_response(prompt)
    while reply == "--loading:":
      reply = self.prompt_response(prompt)
    return reply

  def prompt_response(self, prompt, context=None):
    fine_grained = self._gpt2_large(prompt, context)
    while fine_grained == "--loading:":
      fine_grained = self._gpt2_large(prompt, context)
    payload={
            "inputs": fine_grained, 
            "parameters": {
                "temperature": self.temperature, 
                "num_return_sequences": self.num_return_sequences
            }
        }
    response = requests.post(self.endpoint, 
                             headers=self.headers, json=payload)
    outputs = response.json()
    reply = []
    if type(outputs) == list:
      for output in outputs:
        summary = self._summary(output["generated_text"])
        while summary == "--loading:":
          summary = self._summary(output["generated_text"])
        reply.append(summary)
      reply = ". ".join(reply)
      return reply
    else: return "--loading:"

  def _gpt2_large(self, prompt, context=None):
    if not context == None and type(context) == str:
      prompt = f"{context}{prompt}"
    payload={
            "inputs": prompt, 
            "parameters": {
                "temperature": self.temperature, 
                "num_return_sequences": self.num_return_sequences
            }
        }
    response = requests.post(self.gpt2_large_endpoint, 
                             headers=self.headers, json=payload)
    outputs = response.json()
    reply = []
    if type(outputs) == list:
      for output in outputs:
        if type(prompt) == str and len(prompt) > 0:
          reply.append(output["generated_text"])
      return ". ".join(reply)
    else: return '--loading:'

  def _summary(self, content):
    payload={
            "inputs": content, 
            "parameters": {
                "temperature": self.temperature, 
                "num_return_sequences": 1
            }
        }      
    response = requests.post(self.summary_endpoint, 
                             headers=self.headers, json=payload)
    outputs = response.json()
    summary = []
    if type(outputs) == list:
      for output in outputs:
        summary.append(output["summary_text"])
      return ". ".join(summary)
    else: return "--loading:"

tokens = [
    os.environ.get('A'), 
    os.environ.get('B'), 
    os.environ.get('C'), 
    os.environ.get('D'), 
    os.environ.get('E'), 
    os.environ.get('F'), 
    os.environ.get('G'), 
    os.environ.get('H'), 
    os.environ.get('I'), 
    os.environ.get('J')
]   

endpoint = os.environ.get('AGBRAIN')
gpt2_large_endpoint = os.environ.get('GPT2_LARGE')
summary_endpoint = os.environ.get('SUMMARIZER')

@app.route('/', methods=['GET'])
def welcome():
    return "Endpoint Ready for inferencing:"

# Endpoint for generating solutions/ answers
@app.route('/solve', methods=['POST'])
def solve():
    token = tokens[random.randint(0, len(tokens) - 1)]

    api = HuggingFaceSuperAPI(endpoint, gpt2_large_endpoint, summary_endpoint, token, 5, 1)

    prompt = request.json["prompt"]
    
    solution = api.solve(prompt=prompt)
    
    return jsonify({"solution": solution})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8765)))