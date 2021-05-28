const tdl = document.getElementById('to-do-list');
let tasks = null;

(async () => {
	const response = await fetch('/api', { method: 'GET' });
	tasks = await response.json();
	renderTasks();
})();

function renderTasks() {
	for (let i of tasks) {
		let task = document.createElement('div');
		task.className = 'task-card';
		task.innerHTML = `<p>${i.cont}</p><p style="color:gray;">${i.class}</p>`;
		tdl.append(task);
	}
}

function addTask() {
	let task = document.createElement('div');
	task.className = 'task-card';
	let inp = document.createElement('input');
	inp.className = 'enter-task';
	let inp2 = document.createElement('input');
	inp2.className = 'enter-task-class';
	inp.addEventListener('keydown', (event) => {
		if (event.key === 'Enter') {
			inp2.focus();
		}
	});
	inp2.addEventListener('keydown', (event) => {
		if (event.key === 'Enter') {
			task.innerHTML = `<p>${inp.value}</p><p style="color:gray;">${inp2.value}</p>`;
		}
	});
	task.appendChild(inp);
	task.appendChild(inp2);
	tdl.append(task);
	inp.focus();
}
