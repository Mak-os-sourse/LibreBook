import userApi from "../api/userApi.js";

const LoginForm = document.getElementById("LoginForm");
LoginForm.addEventListener("submit", login)

async function login(event) {
    event.preventDefault();
    let data = new FormData(LoginForm);

    try {
        let res = await userApi.login(
            data.get("field"), data.get("password"),
        )
        console.log(res)
        localStorage.setItem("token", res.access_token)
        window.location.href = "/"
    } catch (error) {
        let status = error?.response?.status;
        console.log(error)
        if(status !== 200) {
            document.getElementById("LoginInfo").innerHTML = `<div class="alert alert-danger pt-2" role="alert">
            Incorrect password or login.</div>`
        }
    }
}