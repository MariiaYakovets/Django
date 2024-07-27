const username = document.querySelector("#username");
const password = document.querySelector("#password");
const logForm = document.querySelector(".form");
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

// слушатель события (сабмит и сам обработчик -> функция)
logForm.addEventListener("submit", (event) => {
	// отменяем действие формы по умолчанию
	event.preventDefault();
	// fetch - запрос6 функция, позволяющая его отправить
	// первый параметр - ссылка
	fetch("login", {
		// данные о запросе
		// тип запроса
		method: "POST",
		// токен безопасности
		headers: { "X-CSRFToken": csrftoken },
		// сами данные, которые отправляются
		// JSON.stringify - превращает в строковой json тип данных
		body: JSON.stringify({
			username: username.value,
			password: password.value,
		}),
	})
		.then((response) => {
			console.log(response);
            window.location.assign("/user/")
            
		})
		.catch((response) => {
			alert(response.statusText);
			console.log(response);
		});
});
