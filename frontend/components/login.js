import UserApi from "../api/userApi.js";

const LoginForm = document.querySelector("#LoginForm");
LoginForm.addEventListener("submit", login);

/**
 * @param {Event} event
 */
async function login(event) {
    event.preventDefault();
    const data = new FormData(LoginForm);

    const res = await UserApi.login(Object.fromEntries(data));

    if (res.status !== 200) {
        document.querySelector("#LoginInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        Incorrect password or login.</div>`;
        return;
    }

    localStorage.setItem("token", res.data.access_token);
    location.assign("/");
}
