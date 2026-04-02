import { useEffect, useState } from "react";
import axios from "axios";

export default function Member() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/tasks/")
      .then(res => setTasks(res.data));
  }, []);

  const updateProgress = async (id, progress) => {
    await axios.put(`http://127.0.0.1:8000/api/tasks/update/${id}/`, {
      progress
    });
  };

  return (
    <div className="p-6">
      <h1>Member</h1>

      {tasks.map(t => (
        <div key={t.id} className="border p-3 mt-2">
          <h2>{t.title}</h2>

          <input
            type="range"
            min="0"
            max="100"
            onChange={e => updateProgress(t.id, e.target.value)}
          />
        </div>
      ))}
    </div>
  );
}