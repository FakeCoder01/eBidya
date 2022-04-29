function getYtVideo(){
    document.getElementById("bws_btn").style.display = 'none';
    document.getElementById("upload").style.backgroundColor = 'White';
    document.getElementById("youtube").style.backgroundColor = 'Blue';
    document.getElementById("yt_url").style.display = 'block';
}

function getDeVideo(){
    document.getElementById("yt_url").style.display = 'none';
    document.getElementById("youtube").style.backgroundColor = 'White';
    document.getElementById("upload").style.backgroundColor = 'Blue';
    document.getElementById("bws_btn").style.display = 'block';
}