import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question) return;
    try {
      const resp = await axios.post("/ask", { question });
      setAnswer(resp.data.answer);
    } catch (err) {
      setAnswer("Error: " + err.message);
    }
  };

  return (
    <div className="App">
      <h1>AI Customer Support Chatbot 🤖</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button type="submit">Ask</button>
      </form>
      {answer && (
        <div className="answer">
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
