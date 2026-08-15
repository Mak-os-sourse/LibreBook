import axios from "axios";

const ApiClient = axios.create({
    baseUrl: "http://localhost:8000/",
})

export default ApiClient;
