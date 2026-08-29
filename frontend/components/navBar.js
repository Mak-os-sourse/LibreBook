import UserApi from "../api/userApi";

export default async function renderAuthUser() {
    const res = await UserApi.getMe();
    let element = document.querySelector("#NavBarButtons");

    element.innerHTML = res.status == 200 ? `<li><a class="btn rounded-circle" href="/add-book">+</a></li>
        <li><a href="/profile"><image src="assets/user-image.jpg" class="d-inline-block align-text-top mx-auto" height="35"</a></li>` : '<li><a class="btn btn-outline-ligh" href="/login">Log in</a></li>';
}
