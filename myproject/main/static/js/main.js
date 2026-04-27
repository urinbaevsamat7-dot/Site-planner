function toggleTheme(){
    document.body.classList.toggle("dark");

    localStorage.setItem(
        "theme",
        document.body.classList.contains("dark")
    );
}

// загрузка темы при открытии страницы
window.addEventListener("load", function(){
    if(localStorage.getItem("theme") === "true"){
        document.body.classList.add("dark");
    }
});
function sendMsg(){
    let msg = document.getElementById('msg').value;

    if(!msg){
        alert("Напиши сообщение");
        return;
    }

    fetch(`/api/chat/?message=${encodeURIComponent(msg)}`)
    .then(res => res.json())
    .then(data => {
        document.getElementById('res').innerText = data.reply;
    })
    .catch(err => {
        console.error("Ошибка:", err);
    });
}

function startVoice(){
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'ru-RU';

    recognition.onresult = function(event){
        document.getElementById('msg').value =
            event.results[0][0].transcript;
    };

    recognition.start();
}