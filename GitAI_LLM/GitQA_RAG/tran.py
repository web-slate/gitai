import json

def combine_jsonl_to_qa_pairs(input_files, output_file):
    qa_pairs = []
    
    for input_file in input_files:
        with open(input_file, 'r') as f:
            jsonl_data = f.readlines()
        
        for line in jsonl_data:
            json_data = json.loads(line)
            messages = json_data.get("messages", [])
            
            for i in range(len(messages) - 1):
                if messages[i]["role"] == "user" and messages[i+1]["role"] == "assistant":
                    question = messages[i]["content"]
                    answer = messages[i+1]["content"]
                    qa_pairs.append({"question": question, "answer": answer})
    
    with open(output_file, 'w') as f:
        for qa_pair in qa_pairs:
            f.write(json.dumps(qa_pair) + '\n')

# Example usage:
input_files = ['stackoverflow_qa_github.jsonl', 'stackoverflow_qa_gitlab.jsonl', 'stackoverflowgit.jsonl','data.jsonl']
output_file = 'GitHub_QA.jsonl'
combine_jsonl_to_qa_pairs(input_files, output_file)
