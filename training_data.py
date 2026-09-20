training_data = [ #each element in list is dictionary that has two individual keys, prompt & label
    {"prompt" : "Implement a BST and red-black tree and illustrate their performance benefits and use cases.",
     "labels" : ["coding", "reasoning"]},
   
    {"prompt" :  "Analyze this document and write a blog synthesizing its observations with my existing ideas.",
     "labels" : ['reading', 'reasoning', 'writing']},
    
    {"prompt" : "Fix this Python function so it correctly handles duplicate values.",
     "labels" : ["coding"]},
    
    {"prompt" : "Create a Java program that simulates a basic elevator system." ,
     "labels" : ["coding"]},
    
    {"prompt" : "Summarize the attached research paper in five bullet points.",
     "labels" : ["reading"]},
    
    {"prompt" : "Read these two articles and identify where their factual claims disagree.",
     "labels" : ["reading", "reasoning"]},
    
    {"prompt" : "Draft a polite email asking my professor for an extension.",
     "labels" : ["writing"]},
    
    {"prompt" : "Turn these rough notes into a polished LinkedIn post.",
     "labels" : ["reading", "writing"]},
    
    {"prompt" : "Which data structure would be better here, a heap or balanced BST? Explain the tradeoffs.",
     "labels" : ["reasoning"]},
    
    {"prompt" : "Determine why this proposed business strategy might fail and suggest alternatives.",
     "labels" : ["reasoning"]},
    
    {"prompt" : "Write an essay about the history of computer programming.",
     "labels" : ["writing"]},
    
    {"prompt" : "Examine this Java method, determine why its runtime is unexpectedly high, and rewrite it more efficiently.",
     "labels" : ["reading", "coding", "reasoning"]},
    ]

from collections import Counter
random_data = "write code read code write essay"


def vector_output(data : str, input: str):
    sorted_data = sorted(set(data.split()))
    vector = []
    count_of_words = Counter(input.split())
    
    for word in sorted_data:
        vector.append(count_of_words[word])
    print(vector)
    
vector_output(random_data, "write code for this essay")

