const username = document.querySelector("#username");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const repeatPassword = document.querySelector("#repeat-password");
const regForm = document.querySelector(".form");
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

// слушатель события (сабмит и сам обработчик -> функция)
regForm.addEventListener("submit", (event) => {
	// отменяем действие формы по умолчанию
	event.preventDefault();
	// валидация пароля
	if (password.value == repeatPassword.value) {
		// fetch - запрос6 функция, позволяющая его отправить
		// первый параметр - ссылка
		fetch("registration", {
			// данные о запросе
			// тип запроса
			method: "POST",
			// токен безопасности
			headers: { "X-CSRFToken": csrftoken },
			// сами данные, которые отправляются
			// JSON.stringify - превращает в строковой json тип данных
			body: JSON.stringify({
				username: username.value,
				email: email.value,
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
	}
});
