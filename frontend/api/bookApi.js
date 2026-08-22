import BaseApi from "./baseApi.js";

class BookApi extends BaseApi {
    constructor() {
        super("/book/")
    }
}

export default new BookApi();