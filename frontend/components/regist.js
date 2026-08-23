import userApi from "../api/userApi.js";

const RegistForm = document.getElementById("RegistForm");
RegistForm.addEventListener("submit", regist);

async function regist(event) {
    event.preventDefault();
    let data = new FormData(RegistForm);

    let res = await userApi.regist(Object.fromEntries(data));

    if (res.status === 401) {
        document.getElementById("RegistInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        The user already exists with a unique email and username.</div>`;
        return;
    }
    if (res.status === 400) {
        document.getElementById("RegistInfo").innerHTML =
            `<div class="alert alert-danger pt-2" role="alert">
        Your username or name must be 4-100 characters long, your password must be 6-30 characters long, 
        contain letters and numbers, and must not contain spaces, special characters, or emojis.</div>`;
        return;
    }

    localStorage.setItem("token", res.data.access_token);
    window.location.href = "/";
}
