import userApi from "../api/userApi.js";

const LoginForm = document.getElementById("LoginForm");
LoginForm.addEventListener("submit", login);

async function login(event) {
    event.preventDefault();
    let data = new FormData(LoginForm);

    let res = await userApi.login(Object.fromEntries(data));

    if (res.status !== 200) {
        document.getElementById("LoginInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        Incorrect password or login.</div>`;
        return;
    }

    localStorage.setItem("token", res.data.access_token);
    window.location.href = "/";
}
