import ApiClient from "./client.js";

class bookApi {
    async search(data, ordering) {
        let res = await ApiClient.get("book", {
            params: {
                search: data,
                ordering: ordering,
            }
        })
        return res.data
    }
}

export default new bookApi();