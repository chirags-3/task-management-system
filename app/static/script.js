// Add event listener to task list items
document.addEventListener("DOMContentLoaded", function() {
    const taskList = document.getElementById("task-list");
    taskList.addEventListener("click", function(event) {
      if (event.target.tagName === "LI") {
        const taskId = event.target.dataset.taskId;
        // TO DO: implement task details view
        console.log(`Task ${taskId} clicked`);
      }
    });
  });