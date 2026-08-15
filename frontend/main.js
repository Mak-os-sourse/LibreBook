// import ApiClient from "./api/client";


function get_user() {
    let token = localStorage.getItem("token");
    let element = document.getElementById("NavBarButtons")

    if (token === null) {
        element.innerHTML = '<li><button class="btn btn-outline-ligh">Log in</button></li>'
    }
    else {
        element.innerHTML = `<li><button class="btn rounded-circle">+</button></li>
        <li><image src="static/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</li>`
    }

}

get_user()