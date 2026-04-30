import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:5000/api/quote";

function App() {
  const [quote, setQuote] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchQuote = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      const data = await res.json();
      setQuote(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <div className="app">
      <h1>Quote of the Day</h1>
      <div className="card">
        {loading && <p>Loading…</p>}
        {error && <p className="error">Error: {error}</p>}
        {quote && !loading && !error && (
          <>
            <p className="quote">“{quote.quote}”</p>
            <p className="author">— {quote.author}</p>
          </>
        )}
      </div>
      <button onClick={fetchQuote} disabled={loading}>
        New Quote
      </button>
    </div>
  );
}

export default App;
