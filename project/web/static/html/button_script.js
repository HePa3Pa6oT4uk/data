function onRegisterButtonClick() {
    const url = "http://localhost:8000/";

    const user_name = document.getElementById("type_of").value;
    const n_of_chunks = document.getElementById("n_of_chunks").value;
    const chunks_length = document.getElementById("chunks").value;
    const height = document.getElementById("height").value;

    fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
        },
        "body": JSON.stringify({
                'type_of_generation': user_name,
                "chunks": n_of_chunks,
                "length": chunks_length,
                'height': height
        }),
    })
}