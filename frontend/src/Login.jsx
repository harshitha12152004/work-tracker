import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const nav = useNavigate();

  const login = async () => {
    const res = await axios.post("http://127.0.0.1:8000/api/login/", {
      email,
      password
    });

    if (res.data.role === "admin") nav("/admin");
    else nav("/member");
  };

  return (
    <div className="flex flex-col items-center mt-20">
      <input placeholder="Email" onChange={e => setEmail(e.target.value)} className="border p-2"/>
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} className="border p-2 mt-2"/>
      <button onClick={login} className="bg-blue-500 text-white p-2 mt-2">Login</button>
    </div>
  );
}