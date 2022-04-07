import API from "./base";

export default async function UploadFileService(data) {
    return await API.post("/image-check", data, {
        mode: 'same-origin',
    })
}
