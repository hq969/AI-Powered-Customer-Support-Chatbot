from flask import Flask, request, jsonify
from agents.agent_fetcher import CustomerSupportAgent

app = Flask(__name__)
agent = CustomerSupportAgent()

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "Question field is required"}), 400
    answer = agent.get_answer(question)
    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
