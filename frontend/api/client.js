/* eslint-disable unicorn/no-top-level-side-effects */
import axios from "axios";

const ApiClient = axios.create({
    validateStatus: (status) => status < 500,
    baseURL: "api/",
});

ApiClient.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");

    if (token) {
        config.headers.set("Authorization", `Bearer ${token}`);
    }
    return config;
});

ApiClient.interceptors.response.use(
    async (config) => {
        if (
            config.status == 403 &&
            config.config.headers.Authorization != undefined
        ) {
            let response = await ApiClient.post("user/update-token");
            if (response.status != 200) {
                localStorage.removeItem("token");
                config.config.headers.delete("Authorization");
                return ApiClient(config.config);
            }

            localStorage.setItem("token", response.data.access_token);
            return ApiClient(config.config);
        }

        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default ApiClient;
