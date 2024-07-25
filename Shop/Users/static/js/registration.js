const username = document.querySelector("#username");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const repeatPassword = document.querySelector("#repeat-password");
const regForm = document.querySelector(".form");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

regForm.addEventListener("submit", (event) => {
	event.preventDefault();
	if (password.value == repeatPassword.value) {
		fetch("registration", {
			method: "POST",
            headers: {'X-CSRFToken': csrftoken},
			body: JSON.stringify({
				username: username.value,
				email: email.value,
				password: password.value,
			}),
		});
	}
});
