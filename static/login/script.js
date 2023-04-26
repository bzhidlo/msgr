"use strict";

async function login(event) {

    let name = document.getElementById('name');
    let password = document.getElementById('password');

    let user = {
        login: name.value,
        password: password.value
    }
    
    let response = await fetch('/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(user)
    });

    if (response.ok) {
        let json = await response.json();
    } else {
        alert("Ошибка HTTP: " + response.status);
    }

}

async function register(event) {
    let name = document.getElementById('name');
    let password = document.getElementById('password');

    let user = {
        name: name.value,
        password: password.value
    }

    let response = await fetch('/users/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(user)
    });

    if (response.ok) {
        let json = await response.json();
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}



