import UserApi from "../api/userApi";

async function renderAuthUser() {
    const res = await UserApi.getMe();
    let element = document.getElementById("NavBarButtons");

    if (res.status != 200) {
        element.innerHTML =
            '<li><a class="btn btn-outline-ligh" href="/login">Log in</a></li>';
    } else {
        element.innerHTML = `<li><a class="btn rounded-circle" href="/add-book">+</a></li>
        <li><image src="assets/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</li>`;
    }
}

export default renderAuthUser;
