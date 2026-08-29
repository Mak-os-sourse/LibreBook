import ApiClient from "./client.js";

export default class BaseApi {
    constructor(url) {
        this.url = url;
    }

    async create(data) {
        return await ApiClient.post(this.url, data);
    }

    async search(data = { page, search, ordering }) {
        return await ApiClient.get(this.url, { params: data });
    }

    async get(id) {
        return await ApiClient.get(`${this.url}${id}/`);
    }

    async update(id, data) {
        return await ApiClient.update(`${this.url}${id}/`, data);
    }

    async delete(id) {
        return await ApiClient.delete(`${this.url}${id}/`);
    }
}
