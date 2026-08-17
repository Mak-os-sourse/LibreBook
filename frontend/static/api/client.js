// import axios from "axios";

const ApiClient = axios.create({
    baseURL: "http://localhost:8000/api/",
})

const token = localStorage.getItem("token");

if (token !== null) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default ApiClient;