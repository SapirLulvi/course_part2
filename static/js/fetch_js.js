function getUserFrontend(){
    let user_id = document.getElementById("id2").value;
    fetch('https://reqres.in/api/users/'+user_id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    const curr_main = document.querySelector("main");
    curr_main.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
    <div>
        <span>ID: ${response_obj_data.id}</span><br>
        <span>Email: ${response_obj_data.email}</span><br>
        <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span><br>
        <br>
        <a href="mailto:${response_obj_data.email}">Send Email</a>
    </div>
    `;

}