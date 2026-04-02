/*import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/tasks/")
      .then(res => setTasks(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Work Tracker</h1>

      {tasks.map(t => (
        <div key={t.id} className="border p-3 mt-2">
          <h2>{t.title}</h2>
          <p>{t.status}</p>
        </div>
      ))}
    </div>
  );
}*/
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Admin from "./Admin";
import Member from "./Member";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/member" element={<Member />} />
      </Routes>
    </BrowserRouter>
  );
}