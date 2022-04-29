function addComment(comment_id, username, userid){
    text = document.getElementById("comment").value;
    $.ajax({
        type: "POST",
        url: "/comment_video/",
        data: {
            'text' : text,
            'comment_id' : comment_id,
            'user_id' : userid,
            'user_name' : username,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(msg){
            document.getElementById("comment").value = '';
        }
    });
}



function likeVideo(video_id, username, userid, exam_name){

    $.ajax({
        type: "POST",
        url: "/like_video/",
        data: {
            'exam_name' : exam_name,
            'video_id' : video_id,
            'user_id' : userid,
            'user_name' : username,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(msg){
            response = JSON.parse(msg);
            document.getElementById("likeCount").innerText = response['liked_value'];
        }
    });
}

