import userApi from "../api/userApi.js";

const RegistForm = document.getElementById("RegistForm");
RegistForm.addEventListener("submit", regist)

async function regist(event) {
    event.preventDefault();
    let data = new FormData(RegistForm);

    try {
        let res = await userApi.regist(
            data.get("name"), data.get("username"),
            data.get("email"), data.get("password"),
        )
        console.log(res)
        localStorage.setItem("token", res.access_token)
        window.location.href = "/"
    } catch (error) {
        let status = error?.response?.status;
        if(status === 401) {
            document.getElementById("RegistInfo").innerHTML = `<div class="alert alert-danger pt-2" role="alert">
            The user already exists with a unique email and username.</div>`
        }
        if (status === 400) {
            document.getElementById("RegistInfo").innerHTML = `<div class="alert alert-danger pt-2" role="alert">
            Your username or name must be 4-100 characters long, your password must be 6-30 characters long, 
            contain letters and numbers, and must not contain spaces, special characters, or emojis.</div>`
        }
    }
}