import { useState, useEffect } from "react";
import axios from "axios";

export default function Admin() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const fetchTasks = async () => {
    const res = await axios.get("http://127.0.0.1:8000/api/tasks/");
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const createTask = async () => {
    await axios.post("http://127.0.0.1:8000/api/tasks/create/", {
      title,
      description: "Demo",
      priority: "high",
      assigned_to: 1,
      progress: 0,
      status: "blocked"
    });
    fetchTasks();
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Admin</h1>

      <input onChange={e => setTitle(e.target.value)} className="border p-2"/>
      <button onClick={createTask} className="bg-green-500 text-white p-2 ml-2">Create</button>

      {tasks.map(t => (
        <div key={t.id} className="border p-3 mt-2">
          {t.title} - {t.status}
        </div>
      ))}
    </div>
  );
}