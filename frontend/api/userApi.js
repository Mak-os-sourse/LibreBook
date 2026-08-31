import BaseApi from "./baseApi.js";
import ApiClient from "./client.js";

class UserApi extends BaseApi {
    constructor() {
        super("/user/");
        this.create = undefined;
    }

    async getMe() {
        return await ApiClient.get(`${this.url}get/me`);
    }

    async regist(data) {
        return await ApiClient.post(`${this.url}regist`, data);
    }

    async login(data) {
        return await ApiClient.post(`${this.url}login`, data);
    }
}

export default new UserApi();
