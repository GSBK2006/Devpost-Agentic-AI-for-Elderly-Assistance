import React, { useState } from "react";
import axios from "axios";

function TaskForm() {
  const [task, setTask] = useState("");
  const [plan, setPlan] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:8000/plan_task/", { task });
    setPlan(response.data.plan);
  };

  return (
    <div className="p-4">
      <form onSubmit={handleSubmit} className="flex flex-col gap-2">
        <input 
          type="text" 
          placeholder="Enter task" 
          value={task} 
          onChange={(e) => setTask(e.target.value)} 
          className="border p-2 rounded"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">Generate Plan</button>
      </form>
      <div className="mt-4 p-2 border rounded bg-gray-100">
        {plan}
      </div>
    </div>
  );
}

export default TaskForm;
