const name = document.querySelector("#name");
const price = document.querySelector("#price");
const description = document.querySelector("#description");
const image = document.querySelector("#image");
const productForm = document.querySelector(".form");
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

productForm.addEventListener("submit", (event) => {
	event.preventDefault();
	fetch("create", {
		method: "POST",
		headers: { "X-CSRFToken": csrftoken },
		body: JSON.stringify({
			name: name.value,
			price: +price.value,
			description: description.value,
			image: image.value,
		}),
	}).then((response)=>{
        if (response.status == 200){
            alert(response.statusText)
            console.log(response)
        }
    }).catch((response)=>{
        alert(response.statusText)
        console.log(response)
    });
});
