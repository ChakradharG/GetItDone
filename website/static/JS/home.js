const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

(async () => {
	const response = await fetch('/getuser', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email')}),
		headers: { 'Content-type': 'application/json' }
	});

	let name = await response.json();
	document.querySelector('#greet-user').innerText = `Hey there, ${name}`;
})();

(async () => {
	const response = await fetch('/gettasks', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email')}),
		headers: { 'Content-type': 'application/json' }
	});

	let tasks = await response.json();
	tasks.sort((t1, t2) => { t1 - t2 });
	tasks.forEach(renderTask);
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

function renderTask(task) {
	let div = customElement({tag: 'div', className: 'task'});
	div.dataset.dt = task.dt;
	div.append(checkBox(task.done));
	div.append(desc(task.cont));

	if (task.done) {
		let dt = new Date(task.dt);
		dt = `${String(dt.getDate()).padStart(2, '0')}-${String(dt.getMonth()+1).padStart(2, '0')}-${dt.getFullYear()}, ${days[dt.getDay()]}`;
		let container = document.querySelector(`.container-completed #d${dt}`) ?? dateElem(dt, document.querySelector('.container-completed > .task-list'));
		container.append(div);
	} else if ((Date.now() - task.dt) > 86400000) {	// 1 day
		let dt = new Date(task.dt);
		dt = `${String(dt.getDate()).padStart(2, '0')}-${String(dt.getMonth()+1).padStart(2, '0')}-${dt.getFullYear()}, ${days[dt.getDay()]}`;
		let container = document.querySelector(`.container-overdue #d${dt}`) ?? dateElem(dt, document.querySelector('.container-overdue > .task-list'));
		container.append(div);
	} else {
		let dt = new Date(task.dt);
		dt = `${String(dt.getDate()).padStart(2, '0')}-${String(dt.getMonth()+1).padStart(2, '0')}-${dt.getFullYear()}, ${days[dt.getDay()]}`;
		let container = document.querySelector(`.container-upcoming #d${dt}`) ?? dateElem(dt, document.querySelector('.container-upcoming > .task-list'));
		container.append(div);
	}
}

function dateElem(dateStr, taskList) {
	let div = customElement({
		tag: 'div',
		className: 'pc-task-container',
		id: 'd' + dateStr.slice(0, 10)
	});

	div.addEventListener('change', () => {
		if (div.children.length === 1) {
			div.remove();
		}
	});

	let _ = customElement({
		tag: 'div',
		className: 'date',
		innerHTML: `<span class="date-line"></span>${dateStr}<span class="date-line"></span>`
	});

	div.append(_);
	taskList.append(div);
	return div;
}

function checkBox(done) {
	let check = customElement({
		tag: 'div',
		className: 'task-check',
		innerHTML: `<input type="checkbox" name="task" ${done ? 'checked' : ''}>`
	});
	check.addEventListener('change', () => {
		check.parentElement.remove();
		renderTask(domElemToObj(check.parentElement));
		saveToServer();
	});

	return check;
}

function desc(cont) {
	let _ = customElement({
		tag: 'div',
		className: 'task-desc',
		innerText: cont
	});

	return _;
}

function domElemToObj(elem) {
	return {
		dt: +elem.dataset.dt,
		done: elem.querySelector('input[type="checkbox"]').checked,
		cont: elem.querySelector('.task-desc').innerText
	};
}

function saveToServer() {
	let tasks = Array.from(document.querySelectorAll('.task')).map(domElemToObj);

	fetch('/synctasks', {
		method: 'POST',
		body: JSON.stringify({'email': localStorage.getItem('email'), 'taskList': tasks}),
		headers: { 'Content-type': 'application/json' }
	});
}

function logOut() {
	localStorage.removeItem('email');
	window.location.href = '/';
}
