const todoList = document.getElementById('todo-list');
let tasks = null;

(async () => {
	const response = await fetch('/api', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email'), 'sync': false}),
		headers: { 'Content-type': 'application/json' }
	});
	tasks = await response.json();
	renderTasks();
})();

function customElement({ tag, className, id, innerText, innerHTML, style, onclick }) {
	let elem = document.createElement(tag);

	if (className) elem.className = className;
	if (id) elem.id = id;
	if (innerHTML) elem.innerHTML = innerHTML;
	if (innerText) elem.innerText = innerText;
	if (style) elem.style = style;
	if (onclick) elem.onclick = onclick;

	return elem;
}

function renderTasks() {
	for (let i of tasks) {
		let task = customElement({tag: 'div', className: 'todo'});
		task.append(customElement({tag: 'p', innerText: i.cont}));
		task.append(customElement({tag: 'p', innerText: i.class, style: 'color: gray'}));
		task.append(ctrlButtons());
		task.append(checkBox(i.done));
		todoList.append(task);
	}
}

function ctrlButtons() {
	let btnContainer = customElement({tag: 'div', className: 'btn-container'});

	btnContainer.append(customElement({
		tag: 'button',
		innerText: 'E',
		onclick() {
			let task = this.closest('.todo');
			addTask(true, task.childNodes[0].innerText, task.childNodes[1].innerText, task);
		}
	}));
	btnContainer.append(customElement({
		tag: 'button',
		innerText: 'D',
		onclick() {
			this.closest('.todo').remove();
			saveToServer();
		}
	}));

	return btnContainer;
}

function checkBox(done) {
	let check = customElement({tag: 'input', className: 'check'});
	check.type = 'checkbox';
	check.checked = done;
	check.addEventListener('change', () => {
		saveToServer();
	});
	
	return check;
}

function addTask(replace, text1, text2, element) {
	let task = customElement({tag: 'div', className: 'todo'});

	let inp1 = customElement({tag: 'input', className: 'input-task'});
	if (replace) inp1.value = text1;
	let inp2 = customElement({tag: 'input', className: 'input-task-class'});
	if (replace) inp2.value = text2;

	inp1.addEventListener('keydown', (event) => {
		if (event.key === 'Enter') inp2.focus();
	});

	inp2.addEventListener('keydown', (event) => {
		if (event.key === 'Enter') inp2.blur();
	});

	inp2.addEventListener('focusout', () => {
		task.innerHTML = '';
		task.append(customElement({tag: 'p', innerText: inp1.value}));
		task.append(customElement({tag: 'p', innerText: inp2.value, style: 'color: gray'}));
		task.append(ctrlButtons());
		task.append(checkBox());
		saveToServer();
	});

	task.append(inp1);
	task.append(inp2);

	if (replace) {
		element.before(task);
		element.remove();
	} else {
		todoList.append(task);
	}
	inp1.focus();
}

function saveToServer() {
	tasks = Array.from(todoList.children);
	tasks = tasks.map(elem => {
		return {done: elem.children[3].checked, 'class': elem.children[1].innerText, cont: elem.children[0].innerText};
	});

	fetch('/api', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email'), 'taskList': tasks, 'sync': true}),
		headers: { 'Content-type': 'application/json' }
	});
}

function logOut() {
	localStorage.removeItem('email');
	window.location.href = '/';
}
