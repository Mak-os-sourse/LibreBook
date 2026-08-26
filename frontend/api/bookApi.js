import BaseApi from "./baseApi.js";
import ApiClient from "./client.js";

class BookApi extends BaseApi {
    constructor() {
        super("/book/");
    }

    async updateImage(bookId, image) {
        return await ApiClient.post(
            `${this.url}update-image`,
            {
                book_id: bookId,
                file: image,
            },
            {
                headers: { "Content-Type": "multipart/form-data" },
            }
        );
    }

    async updateDocument(bookId, document) {
        ApiClient.post;
        return await ApiClient.post(
            `${this.url}update-document`,
            {
                book_id: bookId,
                file: document,
            },
            {
                headers: { "Content-Type": "multipart/form-data" },
            }
        );
    }
}

export default new BookApi();
