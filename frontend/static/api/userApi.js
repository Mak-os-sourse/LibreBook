import ApiClient from "./client.js";

class userApi {
    async search(data, ordering) {
        let res = await ApiClient.get("user", {
            params: {
                search: data,
                ordering: ordering,
            }
        })
        return res.data
    }

    async regist(name, username, email, password) {
        let res = await ApiClient.post("user/regist", {
            name: name,
            email: email,
            username: username, 
            password: password,
        })
        return res.data
    }

    async login(field, password) {
        let res = await ApiClient.post("user/login", {
            field: field,
            password: password,
        })
        return res.data
    }
}


export default new userApi();