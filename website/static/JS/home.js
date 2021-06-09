const todoList = document.getElementById('todo-list');
let tasks = null;

(async () => {
	const response = await fetch('/api', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email')}),
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
		let check = customElement({tag: 'input', className: 'check'});
		check.type = 'checkbox';
		check.checked = i.done;
		task.append(check);
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
		}
	}));

	return btnContainer;
}

function addTask(replace=false, text1, text2, element) {
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
		let check = customElement({tag: 'input', className: 'check'});
		check.type = 'checkbox';
		task.append(check);
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
	// console.log('saving...');
}

function logOut() {
	localStorage.removeItem('email');
	window.location.href = '/';
}

// setInterval(saveToServer, 15000)
