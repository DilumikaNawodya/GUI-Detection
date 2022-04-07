import API from "./base";

export default async function GetComponentItem(data, name){
    console.log(data)
    return await API.post("/add-annotation", 
    {
        data: data,
        name: name
    }, 
    { mode: 'same-origin'}
    )
}