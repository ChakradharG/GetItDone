let tasks = null;

(async () => {
	const response = await fetch('/api', { method: 'GET' });
	tasks = await response.json();
	renderTasks();
})();

function renderTasks() {
	const tdl = document.getElementById('to-do-list');
	for (let i of tasks) {
		let task = document.createElement('div');
		task.className = 'task-card';
		task.innerHTML = `<p>${i.cont}<p style="color:gray;">${i.class}</p></p>`;
		tdl.append(task);
	}
}
