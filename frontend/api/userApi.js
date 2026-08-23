import BaseApi from "./baseApi.js";
import ApiClient from "./client.js";

class UserApi extends BaseApi {
    constructor() {
        super("/user/");
    }

    create = undefined;

    async getMe() {
        return await ApiClient.get(`${this.url}get/me`);
    }

    async regist(data = { name, username, email, password }) {
        return await ApiClient.post(`${this.url}regist`, data);
    }

    async login(data = { field, password }) {
        return await ApiClient.post(`${this.url}login`, data);
    }
}

export default new UserApi();
