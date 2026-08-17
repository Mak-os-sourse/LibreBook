import bookApi from "./api/bookApi.js";

async function get_cards() {
    const urlParams = new URLSearchParams(window.location.search);
    let res = await bookApi.search(urlParams.get("search"), urlParams.get("ordering"));
    console.log(res);
}

function get_user() {
    const token = localStorage.getItem("token");
    let element = document.getElementById("NavBarButtons")

    if (token === null) {
        element.innerHTML = '<li><a class="btn btn-outline-ligh" href="/login">Log in</a></li>'
    }
    else {
        element.innerHTML = `<li><button class="btn rounded-circle">+</button></li>
        <li><image src="static/files/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</li>`
    }

}

get_cards()
get_user()