$('#unlike').click(function(){
    var postid;
    postid = $(this).attr("data-postid");
    $.get('/blog/unlike_post/', {postid: postid}, function(data){
	$("#like").show();        
	$("#like").html(data);
        $("#unlike").hide();
    });
});
